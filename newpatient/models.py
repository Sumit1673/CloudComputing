from django.db import models
from eyecare_app.models import DataPatinet
from PIL import Image

# Create your models here.
class PatientImage(models.Model):
    user = models.OneToOneField(DataPatinet, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='retina_images')

    def __str__(self):
        return f"{self.user.first_name} Image"

    # def save(self):
    #     super().save()
    #
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)