from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Company, Vacancy


def company_list(request):
    companies = Company.objects.all()
    companies_json = [c.to_json() for c in companies]
    return JsonResponse(companies_json, safe=False)

def company_detail(request, id):
    company = get_object_or_404(Company, id=id)
    data = company.to_json()
    return JsonResponse(data)

def company_vacancies(request, id):
    company = get_object_or_404(Company, id=id)
    vacancies = company.vacancies.all()
    data = [v.to_json() for v in vacancies]
    return JsonResponse(data, safe=False)

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    data = [v.to_json() for v in vacancies]
    return JsonResponse(data, safe=False)

def vacancy_detail(request, id):
    vacancy = get_object_or_404(Vacancy, id=id)
    data = vacancy.to_json()
    return JsonResponse(data)

def top_ten_vacancies(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    data = [v.to_json() for v in vacancies]
    return JsonResponse(data, safe=False)
