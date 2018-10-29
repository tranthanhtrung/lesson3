from django.db import models


class customers(models.Model):
	forename = models.CharField(max_length=10)
	surname = models.CharField(max_length=10)
	add1 = models.CharField(max_length=50)
	add2 = models.CharField(max_length=50)
	add3 = models.CharField(max_length=50)
	postcode = models.CharField(max_length=20)
	phone = models.CharField(max_length=10)
	email = models.CharField(max_length=50)
	registered = models.CharField(max_length=50)
	def __str__(self):
		return "ID: " +str(self.id) + "- " + self.forename

class categories(models.Model):
	name = models.CharField(max_length=20)
	description = models.CharField(max_length=100)
	image = models.CharField(max_length=200)
	def __str__(self):
		return str(self.id)

class logins(models.Model):
	customer_id = models.ForeignKey(customers,on_delete=models.CASCADE)
	username = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	def __str__(self):
		return self.id

class delivery_addresses(models.Model):
	forename = models.CharField(max_length=10)
	surname = models.CharField(max_length=10)
	add1 = models.CharField(max_length=50)
	add2 = models.CharField(max_length=50)
	add3 = models.CharField(max_length=50)
	postcode = models.CharField(max_length=20)
	phone = models.CharField(max_length=10)
	email = models.CharField(max_length=50)
	def __str__(self):
		return "ID: " + str(self.id) + "- " + self.forename

class orders(models.Model):
	custumer_id = models.ForeignKey(customers, on_delete=models.CASCADE)
	registered = models.CharField(max_length=10)
	delivery_add_id = models.ForeignKey(delivery_addresses, on_delete=models.CASCADE)
	payment_type = models.IntegerField(default=0)
	date = models.DateTimeField("date published")
	status = models.IntegerField(default=0)
	session = models.CharField(max_length=50)
	total = models.FloatField(default=0)
	def __str__(self):
		return str(self.custumer_id) + " " + str(self.total)
		
class Products(models.Model):
	cat_id = models.ForeignKey(categories, related_name = "products" ,on_delete=models.CASCADE)
	name = models.CharField(max_length=20)
	description = models.CharField(max_length=100)
	image = models.CharField(max_length=200)
	price =  models.FloatField(default=0)
	def __str__(self):
		return self.name + " - " + str(self.price)

class order_items(models.Model):
	order_id = models.ForeignKey(orders, related_name = "items", on_delete=models.CASCADE)
	product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=0)
	def __str__(self):
		return str(self.id)
		
		
class admins(models.Model):
	username = models.CharField(max_length=50)
	password =models.CharField(max_length=20)
	def __str__(self):
		return self.id
		