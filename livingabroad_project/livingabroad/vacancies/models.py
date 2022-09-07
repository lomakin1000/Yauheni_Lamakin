import csv
from django.db import models
import csv

# Create your models here.


# with open("data.csv", newline = '') as csvfile:
#     reader = csv.DictReader(csvfile, delimiter=";")
#     for row in reader:
#         print(row['link'], '|', row['price'])

class Vacancies(models.Model):  # создаём таблицу базы данных
    title = models.CharField('Title',max_length=50)
    salary = models.CharField('Salary',max_length=20)
    description = models.TextField('Description')
    remote = models.CharField('Remote',max_length=20)
    link = models.URLField('Link')
    city = models.CharField('City',max_length=50)
    
    def __str__(self):
        return self.title  # возвращает название объекта
    

    
    