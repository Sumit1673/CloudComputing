import sys
sys.path.append('../')
import os
from datetime import date
from django.shortcuts import render, HttpResponse
from .models import DataPatinet, DataDiabetic
from django.contrib.auth.decorators import login_required
from users.views import login

pkg_dir = 'model/pretrained/pretrained-models.pytorch-master/'
import sys
sys.path.insert(0, pkg_dir)
sys.path.append('../')
from PIL import Image
from model import pretrained
import torch
import torch.nn as nn
import torchvision
from torchvision import transforms
import torch.nn.functional as F
from torchvision import transforms

def home(request):

    return render(request, 'eyecare_app/home.html')  # returns http response in background


def about(request):
    return render(request, 'eyecare_app/about.html')

@login_required
def workspace(request):
    # Fill the patient database with all the data in the db
    try:
        # Fill the patient database with all the data in the db
        patient_list = list(DataPatinet.objects.values_list('id', 'patient_id', 'first_name', 'last_name'))
        db_res = list(DataDiabetic.objects.values_list('patient_info_id', 'ai_score', 'result', 'tested_on'))
        new_list = []
        # p_id, f_name, l_name, res, data, ai_Score, comm
        for j, p_lst in enumerate(patient_list):
            for i_ib_res, val in enumerate(db_res):
                val = ['-' if i == None else i for i in val]
                p_id = val[0]
                if p_id in p_lst:
                    p_lst = list(p_lst)
                    p_lst.append(val[2])
                    p_lst.append(val[1])
                    p_lst.append(str(val[3]))
                    break
            new_list.append(list(p_lst))
        return render(request, 'eyecare_app/workspace.html', {'btn_clicked': 1, 'data': new_list})

    except:
        return render(request, 'eyecare_app/workspace.html')

def analyze_img(request):
    obj = RetinEyeModel('model.bin')
    id = int(request.POST.getlist("analysis")[0])
    patient_info = DataPatinet.objects.filter(patient_id=id).values_list('image', 'id')
    img_path = patient_info[0][0]
    patient_pid = patient_info[0][1]
    img_path = 'media/'+img_path
    # do analysis
    pred, confidence = obj.get_predictions(img_path)
    p_result = DataDiabetic(patient_info=DataPatinet.objects.get(pk=patient_pid),
                            result=int(pred[0]),
                            ai_score=float(confidence),
                            tested_on=str(date.today()))
    p_result.save()
    try:
        # Fill the patient database with all the data in the db
        patient_list = list(DataPatinet.objects.values_list('id', 'patient_id', 'first_name', 'last_name'))
        db_res = list(DataDiabetic.objects.values_list('patient_info_id', 'ai_score', 'result', 'tested_on'))
        new_list = []
        # p_id, f_name, l_name, res, date, ai_Score, comm

        for j, p_lst in enumerate(patient_list):
            for i_ib_res, val in enumerate(db_res):
                val = ['-' if i == None else i for i in val]
                p_id = val[0]
                if p_id in p_lst:
                    p_lst = list(p_lst)
                    p_lst.append(val[2])
                    p_lst.append(val[1])
                    p_lst.append(str(val[3]))
                    break
            new_list.append(list(p_lst))
        return render(request, 'eyecare_app/workspace.html', {'btn_clicked': 1, 'data': new_list})

    except Exception as e :
        print(e)
    return render(request, 'eyecare_app/workspace.html')


class RetinEyeModel():
    def __init__(self, m_path):
        self.model_path = m_path
        self.model = pretrained.__dict__['resnet101'](pretrained=None)

        self.model.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.model.last_linear = nn.Sequential(
                                  nn.BatchNorm1d(2048, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True),
                                  nn.Dropout(p=0.25),
                                  nn.Linear(in_features=2048, out_features=2048, bias=True),
                                  nn.ReLU(),
                                  nn.BatchNorm1d(2048, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True),
                                  nn.Dropout(p=0.5),
                                  nn.Linear(in_features=2048, out_features=1, bias=True),
                                 )
        if os.path.isfile(self.model_path):
            print(True)
        try:
            self.model.load_state_dict(torch.load(self.model_path, map_location=torch.device('cpu')))
            for param in self.model.parameters():
                param.requires_grad = False
        except FileNotFoundError as e:
            print(e)


    def get_predictions(self, image_path):
        image = Image.open(image_path)
        image = image.resize((256, 256), resample=Image.BILINEAR)
        image = transforms.ToTensor()(image)
        imgs = image.unsqueeze(0)
        self.model.eval()

        pred = self.model(imgs)[0]
        prob = F.softmax(pred, dim=-1)
        coef = [0.5, 1.5, 2.5, 3.5]

        if pred < coef[0]:
            test_preds = [0, 'No DR']
        elif pred >= coef[0] and pred < coef[1]:
            test_preds = [1, 'Mild']
        elif pred >= coef[1] and pred < coef[2]:
            test_preds = [2, 'Moderate']
        elif pred >= coef[2] and pred < coef[3]:
            test_preds = [3, 'Severe']
        else:
            test_preds = [4, 'Proliferative DR']

        return test_preds, prob.numpy()[0]