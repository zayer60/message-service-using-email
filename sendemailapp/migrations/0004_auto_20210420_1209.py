# Generated by Django 3.2 on 2021-04-20 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sendemailapp', '0003_group_patient_patiententry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='patiententry',
            name='group',
        ),
        migrations.RemoveField(
            model_name='patiententry',
            name='patient',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
        migrations.DeleteModel(
            name='PatientEntry',
        ),
    ]
