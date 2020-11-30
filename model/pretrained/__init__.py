from .version import __version__

from . import models
# from . import datasets

# from .models.utils import pretrained_settings
from .models.utils import model_names

# # to support pretrainedmodels.__dict__['nasnetalarge']
# # but depreciated
# from .models.fbresnet import fbresnet152
# from .models.cafferesnet import cafferesnet101
# from .models.bninception import bninception
# from .models.resnext import resnext101_32x4d
# from .models.resnext import resnext101_64x4d
# from .models.inceptionv4 import inceptionv4
# from .models.inceptionresnetv2 import inceptionresnetv2
# from .models.nasnet import nasnetalarge
# from .models.nasnet_mobile import nasnetamobile
# from .models.torchvision_models import alexnet
# from .models.torchvision_models import densenet121
# from .models.torchvision_models import densenet169
# from .models.torchvision_models import densenet201
# from .models.torchvision_models import densenet161
# from .models.torchvision_models import resnet18
# from .models.torchvision_models import resnet34
# from .models.torchvision_models import resnet50
from .models.torchvision_models import resnet101
# from .models.torchvision_models import resnet152
# from .models.torchvision_models import inceptionv3
# from .models.torchvision_models import squeezenet1_0
# from .models.torchvision_models import squeezenet1_1
# from .models.torchvision_models import vgg11
# from .models.torchvision_models import vgg11_bn
# from .models.torchvision_models import vgg13
# from .models.torchvision_models import vgg13_bn
# from .models.torchvision_models import vgg16
# from .models.torchvision_models import vgg16_bn
# from .models.torchvision_models import vgg19_bn
# from .models.torchvision_models import vgg19
# from .models.dpn import dpn68
# from .models.dpn import dpn68b
# from .models.dpn import dpn92
# from .models.dpn import dpn98
# from .models.dpn import dpn131
# from .models.dpn import dpn107
# from .models.xception import xception
# from .models.senet import senet154
# from .models.senet import se_resnet50
from .models.senet import se_resnet101
# from .models.senet import se_resnet152
# from .models.senet import se_resnext50_32x4d
# from .models.senet import se_resnext101_32x4d
# from .models.pnasnet import pnasnet5large
# from .models.polynet import polynet
