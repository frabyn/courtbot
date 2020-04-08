from django.urls import path

from . import views

app_name = 'paper_pusher'

urlpatterns = [
    path('', views.BlankFormList.as_view(), name='index'),
    path('generate/<str:form_pk>/<str:case_pk>', views.generate_form, name='generate'),
    path('download/<str:form_pk>/blank', views.download_blank, name='blank_form'),

]
