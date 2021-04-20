from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Patient(models.Model):
    GENDER_CHOICES = (
        ('male', 'MALE'),
        ('female', 'FEMALE'),
    )
    name = models.CharField(max_length=100)
    gender=models.CharField(max_length=100,choices=GENDER_CHOICES, default='male')
    dob = models.DateField()
    email = models.EmailField()
    groups = models.ManyToManyField(Group)



    def __str__(self):
        return self.name













