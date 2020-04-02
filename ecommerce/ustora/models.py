from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class categories(models.Model):
	c_id = models.AutoField(primary_key =True)
	c_name = models.CharField(max_length =30)
	c_image = models.ImageField()
	def __str__ (self):
		return self.c_name


class products(models.Model):
	p_id = models.AutoField(primary_key=True)
	p_name = models.CharField(max_length=120)
	p_image = models.ImageField()
	p_desc = models.TextField()
	p_quantity = models.IntegerField()
	p_date = models.DateTimeField(auto_now=True)
	p_price = models.FloatField()
	p_tags = models.TextField()
	p_discount = models.IntegerField()
	p_category = models.ForeignKey('categories',on_delete =models.CASCADE)
	def __str__ (self):
		return self.p_name


class cart(models.Model):
	cart_id = models.AutoField(primary_key=True)
	product_quantity = models.IntegerField(default=1)
	cart_products = models.ForeignKey('products',on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	
	
	

class reviews(models.Model):
	r_id =models.AutoField(primary_key=True)
	r_text = models.TextField()
	r_time = models.DateTimeField(auto_now=True)
	r_product = models.ForeignKey('products',on_delete = models.CASCADE)
	r_user = models.ForeignKey(settings.AUTH_USER_MODEL)



class checkout(models.Model):
	check_id=models.AutoField(primary_key=True)
	check_user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	u_name = models.CharField(max_length=120)
	checkout_products=models.ForeignKey('products',on_delete=models.CASCADE)
	cart = models.ForeignKey('cart',on_delete=models.CASCADE)
	u_email = models.EmailField()
	u_number = models.IntegerField()
	u_address = models.CharField(max_length=120)
	check_time = models.DateTimeField(auto_now=True)


	




# Create your models here.
