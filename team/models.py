from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Applicant (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='img')
    gender = models.CharField(max_length=20)
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.user.first_name

class Company (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    image =  models.ImageField(upload_to='img')
    gender = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    company_name = models.CharField(max_length=150)

    def __str__(self):
        return self.user.username

class Job (models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=50)
    salary = models.FloatField()
    image = models.ImageField(upload_to='img')
    description = models.CharField(max_length=400)
    experience = models.CharField(max_length=500)
    location = models.CharField(max_length=400)
    skills = models.CharField(max_length=200)
    creation_date =models.DateField()

    def __str__(self):
        return self.title

class Application(models.Model):
    company = models.CharField(max_length=200)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    resume = models.ImageField(upload_to='img')
    apply_date = models.DateField()

    def __str__(self):
        return str(self.applicant) 
