from djongo import models
from PIL import Image
# class name represents the collection name
class DataPatinet(models.Model):
    # no primary key is chosen so the databse will chose for us. By default it
    # 'id'.
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50,default='NA')
    patient_id = models.CharField(max_length=50)
    email = models.EmailField(default='')
    phone = models.CharField(max_length=12, null=True)
    age = models.IntegerField(null=True)
    image = models.ImageField(default='default.png', upload_to='retina_images')
    # comments = models.CharField(max_length=150)

    def __str__(self):
        return f"Created Patient with ID: {self.patient_id}"

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class DataDiabetic(models.Model):
    patient_info = models.OneToOneField(
        DataPatinet,
        default=0,
        on_delete=models.CASCADE, primary_key=True,
    )
    result = models.IntegerField()
    ai_score = models.DecimalField(default=0.0,max_digits=5, decimal_places=2)
    tested_on = models.DateField(max_length=50, null=True, blank=True)  # datefield = datetime.date
    def __str__(self):
        return f"Diabetic Result: Severity {self.result} with AI score {self.ai_score}"




