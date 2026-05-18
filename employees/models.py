from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.name


class Position(models.Model):
    title = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    cpf = models.CharField(max_length=11, unique=True)

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )

    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name