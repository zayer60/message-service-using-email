# Generated by Django 3.2 on 2021-04-20 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sendemailapp', '0005_group_patient_patiententry'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PatientEntry',
        ),
    ]
