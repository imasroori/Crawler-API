import json

from django.http import HttpResponse
from django.shortcuts import render

from api.models import Company


def index(request):
    return render(request, 'first_page.html')


def show_list_company(request):
    context = Company.objects.all()
    return render(request, 'list_company.html', {'context': context})


def show_detail_company(request, id):
    context = Company.objects.filter(id=id)
    return render(request, 'detail_company.html', {'context': context})


def crawl_to_web(request):
    url_site = 'https://www.refinitiv.com/bin/esg/esgsearchresult'
    params = {'ricCode': 'AAPL.O'}
    import requests
    json_out = requests.get(url_site, params=params)

    return HttpResponse(json.dumps(json_out.json()))
