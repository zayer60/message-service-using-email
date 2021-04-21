from django.urls import path
from .views import *

urlpatterns =[
    path('article/', PatientListView.as_view(), name='patient-list'),
    path('article/create/', CreatePatient.as_view(), name='create-patient'),
    path('article/<int:pk>/edit/', UpdatePatient.as_view(), name='update-patient'),
    path('article/<int:pk>/delete', DeletePatient.as_view(), name='delete-patient'),
    path('group/',GroupListView.as_view(),name='group-list'),
    path('group/<int:id>',groupdetail,name='group-details'),
    path('group/<int:pk>/edit',UpdateGroup.as_view(),name='group-update'),
    path('group/create',CreateGroup.as_view(),name='group-create'),
    path('group/<int:pk>/delete',DeleteGroup.as_view(),name='group-delete'),
]