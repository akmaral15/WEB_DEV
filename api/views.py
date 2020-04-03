
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


@csrf_exempt
def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        return JsonResponse(company.to_json())
    elif request.method == 'POST':
        return JsonResponse({'data': 'post request'})


@csrf_exempt
def company_vacancies(request, company_id):
    if request.method == 'GET':
        vacancies = Vacancy.objects.filter(company_id=company_id)
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    elif request.method == 'POST':
        return JsonResponse({'data': 'post request'})



@csrf_exempt
def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    elif request.method == 'POST':
        return JsonResponse({'data': 'post request'})



@csrf_exempt
def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        return JsonResponse(vacancy.to_json())
    elif request.method == 'POST':
        return JsonResponse({'data': 'post request'})



@csrf_exempt
def vacancy_top(request):
    vac_top = Vacancy.objects.order_by('-salary')[:10]
    vac_json = [vacancy.to_json() for vacancy in vac_top]
    if request.method == 'GET':
        return JsonResponse(vac_json, safe=False)