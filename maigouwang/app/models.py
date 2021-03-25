from django.db import models


# Create your models here.


class Data(models.Model):
    dog_title = models.CharField(max_length=100, verbose_name='狗狗标题')
    salesLocation = models.CharField(max_length=100, verbose_name='售卖地址')
    dog_breed = models.CharField(max_length=50, verbose_name='狗狗品种')
    dog_age = models.CharField(max_length=50, verbose_name='狗狗年龄')
    vaccineSituation = models.CharField(max_length=50, verbose_name='疫苗情况')
    publisher = models.CharField(max_length=50, verbose_name='发布人')
    dog_price = models.CharField(max_length=20, verbose_name='狗狗价格')
    sellerPromise = models.CharField(max_length=200, verbose_name='卖家承诺')
    dog_detailedInterface = models.CharField(max_length=200,verbose_name='详情页面')
