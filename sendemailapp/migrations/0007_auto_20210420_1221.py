# Generated by Django 3.2 on 2021-04-20 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sendemailapp', '0006_delete_patiententry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='groups',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
