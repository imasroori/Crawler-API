from django.urls import path

from api import views

app_name = 'api'
urlpatterns = [
    path('', views.show_data, name='show_data'),
    path('corps/', views.show_list_company, name='ListCompany'),
    path('esgscore/<id>', views.show_detail_company, name='show_detail_company'),
]
