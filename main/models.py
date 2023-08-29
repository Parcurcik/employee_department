from django.db import models


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name='Название департамента')
    director = models.CharField(max_length=100, verbose_name='Контакты директора департамента')

    def __str__(self):
        return self.name


class Employee(models.Model):
    initials = models.TextField(max_length=50, verbose_name='ФИО')
    photo = models.ImageField(upload_to='upload/employee_photos/', verbose_name='Фото работника')
    position = models.TextField(max_length=20, verbose_name='Должность')
    salary = models.IntegerField(verbose_name='Зарплата')
    age = models.IntegerField(verbose_name='Возраст')
    departament = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.initials
