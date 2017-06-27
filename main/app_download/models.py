from django.db import models

# Create your models here.
class File_model(models.Model):
    xlsx=models.FileField(upload_to="%m/%d")
    storage=models.FileField(upload_to="storage")
    now=models.DateTimeField(auto_now_add=True)