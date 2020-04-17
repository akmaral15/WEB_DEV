
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from api.models import Company, Vacancy
from django.http import JsonResponse


@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_json = [company.to_json() for company in companies]
        return JsonResponse(companies_json, safe=False)
    elif request.method == 'POST':
        return JsonResponse({'data': ' post request'})


