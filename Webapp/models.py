from django.db import models


# Create your models here.

class ContactDB(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Subject = models.CharField(max_length=100, null=True, blank=True)
    Message = models.CharField(max_length=100, null=True, blank=True)


class LoginDB(models.Model):
    User_Name = models.CharField(max_length=100, null=True, blank=True)
    User_Email = models.EmailField(max_length=100, null=True, blank=True)
    User_Password = models.CharField(max_length=100, null=True, blank=True)


class RegisterDB(models.Model):
    UserName = models.CharField(max_length=100, null=True, blank=True)
    UserEmail = models.EmailField(max_length=100, null=True, blank=True)
    UserPassword = models.CharField(max_length=100, null=True, blank=True)


class cartDB(models.Model):
    Ct_username = models.CharField(max_length=100, null=True, blank=True)
    Ct_Product_Name = models.CharField(max_length=100, null=True, blank=True)
    Ct_Quantity = models.IntegerField(null=True, blank=True)
    Ct_Total_Price = models.IntegerField(null=True, blank=True)
