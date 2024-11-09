from django.db import models

# Create your models here.
class Product(models.Model):
      catagory = models.CharField(max_length=100, null=False, blank=False)
      num_of_products = models.IntegerField()

      def __str__(self):
          return f'{self.catagory}-{self.num_of_products}'


class AreaModel(models.Model):
    catagory = models.CharField(max_length=100, null=False, blank=False)
    num_of_products = models.IntegerField()

    def __str__(self):
        return f'{self.catagory}-{self.num_of_products}'

class BarModel(models.Model):
    catagory = models.CharField(max_length=100, null=False, blank=False)
    num_of_products = models.IntegerField()

    def __str__(self):
        return f'{self.catagory}-{self.num_of_products}'

class PieModel(models.Model):
    catagory = models.CharField(max_length=100, null=False, blank=False)
    num_of_products = models.FloatField()

    def __str__(self):
        return f'{self.catagory}-{self.num_of_products}'

class TableApp(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    position = models.CharField(max_length=30, null=False, blank=False)
    office = models.CharField(max_length=20, null=False, blank=False)
    age = models.IntegerField()
    startdate = models.DateField(null=True)
    salary = models.CharField(max_length=15, null=False, blank=False)

    def __str__(self):
        return f'{self.name}-{self.position}-{self.office}-{self.age}-{self.startdate}-{self.salary}'

class Samsung(models.Model):
    Date = models.DateField(null=False)
    Close_price = models.IntegerField(default=0)
    Individual = models.IntegerField(default=0)
    Foreigner = models.IntegerField(default=0)
    Organ =models.IntegerField(default=0)
    Finance = models.IntegerField(default=0)
    Insurance = models.IntegerField(default=0)
    Investment = models.IntegerField(default=0)
    Bank = models.IntegerField(default=0)
    Other_finance = models.IntegerField(default=0)
    Pension_fund = models.IntegerField(default=0)
    Other_corporations = models.IntegerField(default=0)
    Other_foreiner = models.IntegerField(default=0)
    Private_fund = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.Date}-{self.Close_price}-{self.Individual}' \
               f'-{self.Foreigner}-{self.Organ}-{self.Finance}' \
               f'-{self.Insurance}-{self.Investment}-{self.Bank}' \
               f'-{self.Other_finance}-{self.Pension_fund}-{self.Other_corporations}' \
               f'-{self.Other_foreiner}-{self.Private_fund}'
