from django.db import models

# Create your models here.
class Product(models.Model):

	prod_name=models.CharField(max_length=100, blank=False)
	company=models.CharField(max_length=100, blank=False)
	quantity=models.IntegerField()
	price=models.IntegerField()
	prod_type=models.CharField(max_length=100)
	units=models.IntegerField()

	def __str__(self):
		return('Name:{0} Company: {1} Qty:{2} Price: {3} Type:{4} Units: {5}'.format(self.prod_name, self.company,self.quantity, self.price, self.prod_type, self.units))



