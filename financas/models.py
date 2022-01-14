from django.db import models

class User(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Finance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    salary = models.FloatField()
    #salario extra
    extra_income = models.FloatField()
    #gastos com aluguel
    rent_expenses = models.FloatField()
    #despesa de mercado
    market_expenses = models.FloatField()
    #renda extra
    extra_expenses = models.FloatField()
    #data de recebimento
    receipt_date = models.DateField()

