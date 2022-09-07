from django.shortcuts import render
from .models import Vacancies
from django.views.generic import DetailView  # класс, который позволяет отслеживать динамические страницы
import csv,io


# Create your views here.

def vacancies(request):
    vacancies = Vacancies.objects.all()  # выводи все объекты из таблицы Vacancies
    return render(request,'vacancies/vacancies.html',{'vacancies':vacancies})

    