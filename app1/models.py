from django.db import models

# Create your models here.
class Userregister(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    number=models.IntegerField()
    address=models.TextField(default="")
    password=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name
    
class Category(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to="category_Img")
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    categoryname=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    price=models.IntegerField()
    description=models.TextField()
    img=models.ImageField(upload_to="product_Img")
    quantity=models.IntegerField()

class Order(models.Model):
    userid=models.CharField(max_length=250)
    productid=models.CharField(max_length=250)
    quantity=models.CharField(max_length=250)
    paymentamt=models.CharField(max_length=250)
    paymentmethod=models.CharField(max_length=250)
    transactionid=models.CharField(max_length=250)
    datetime=models.DateTimeField(auto_now=True,auto_created=True)


class Contactus(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    number=models.IntegerField()
    message=models.TextField()
    def __str__(self) -> str:
        return self.name