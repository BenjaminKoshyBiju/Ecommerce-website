from django.db import models


# Create your models here.


class Table1(models.Model):
    name = models.CharField(max_length=50)
    price= models.IntegerField(default=0)
    img=models.ImageField(upload_to='img', null=True)

class Table2(models.Model):
    desc=models.TextField()
    images=models.ImageField(upload_to='T2img', null=True)
    table1 = models.ForeignKey(Table1, on_delete=models.CASCADE)
    
