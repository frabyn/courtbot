from django.urls import path

from . import views

app_name = 'case_manager'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_data, name="upload"),
    path('search/', views.case_search, name="search"),
    path('case_manager/<str:pk>', views.CaseDetail.as_view(), name="view_case")
]
