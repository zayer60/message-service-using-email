from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView, FormView
from django.views.generic.base import View
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .form import PatientForm


class PatientListView(ListView):
    model = Patient
    template_name = 'sendemailapp/patientlist.html'

class CreatePatient( CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'sendemailapp/patient-create.html'

class UpdatePatient( UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'sendemailapp/patient-update-form.html'


class DeletePatient( DeleteView):
    model = Patient
    template_name = 'sendemailapp/patient-delete.html'
    success_url = reverse_lazy('patient-list')


class GroupListView(ListView):
    model = Group
    template_name = 'sendemailapp/grouplist.html'

def groupdetail(request,id):
    group= Group.objects.get(pk=id)
    patients=group.patient_set.all()
    return render(request,'sendemailapp/groupdetail.html',{'group':group,'patients':patients})


class CreateGroup( CreateView):
    model = Group
    fields = '__all__'
    template_name = 'sendemailapp/group-create.html'

class UpdateGroup( UpdateView):
    model = Group
    fields = ('name',)
    template_name = 'sendemailapp/group-update-form.html'


class DeleteGroup( DeleteView):
    model = Group
    template_name = 'sendemailapp/group-delete.html'
    success_url = reverse_lazy('group-list')



