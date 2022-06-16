from django.shortcuts import render


# Create your views here.

def show_data(request):
    company = 'Apple Inc'
    return render(request, 'first_page.html')


def show_list_company(request):
    context = {'a': 1, 'b': 2}
    return render(request, 'detail_company.html', context=context)


def show_detail_company(request, id=1):
    context = {'a': 1, 'b': 2}
    return render(request, 'detail_company.html', context=context)
