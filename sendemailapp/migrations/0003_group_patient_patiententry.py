# Generated by Django 3.2 on 2021-04-20 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sendemailapp', '0002_auto_20210420_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE')], default='male', max_length=100)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('groups', models.ManyToManyField(to='sendemailapp.Group')),
            ],
        ),
        migrations.CreateModel(
            name='PatientEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sendemailapp.group')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sendemailapp.patient')),
            ],
        ),
    ]
