from django.db import models


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name='Название департамента')
    director = models.CharField(max_length=100, verbose_name='Контакты директора департамента')

    def __str__(self):
        return self.name


class Employee(models.Model):
    surname = models.CharField(max_length=20, verbose_name='Фамилия', db_index=True)
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=20, verbose_name='Отчество')
    photo = models.ImageField(upload_to='upload/employee_photos/', verbose_name='Фото работника')
    position = models.CharField(max_length=50, verbose_name='Должность')
    salary = models.IntegerField(verbose_name='Зарплата')
    birthday = models.DateField(verbose_name='Дата рождения')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.surname}, {self.position}, {self.department}'
