from django.urls import path

from api import views

app_name = 'api'
urlpatterns = [
    path('', views.index, name='show_data'),
    path('crawl_to_web/', views.crawl_to_web, name='crawl_to_web'),
    path('corps/', views.show_list_company, name='ListCompany'),
    path('esgscore/<id>', views.show_detail_company, name='show_detail_company'),
]
