from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    description =models.TextField
    city=models.CharField(max_length=200)
    address = models.TextField

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural ='Companies'


    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }





    # Create your models here.


class Vacancy(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'Vacancy id ={self.id} , name = {self.name}'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'salary': self.salary,
            'description': self.description,

        }

