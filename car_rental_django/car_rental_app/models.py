from django.db import models

class credentials(models.Model):
    name=models.CharField("uname",max_length=100)
    email=models.EmailField("email",unique=True)
    password=models.CharField("passwd",max_length=100)

    def __str__(self):
        return self.name

class car_detail(models.Model):
    car_name=models.CharField("cname",max_length=100)
    cost_per_hr=models.IntegerField("cost_per_hr")
    seats=models.IntegerField("seats")
    fule_type=models.CharField("fule_type",max_length=100)
    model=models.CharField("model",max_length=100)
    stocks=models.IntegerField("stocks")
    def __str__(self):
        return self.car_name
class places(models.Model):
    place=models.CharField("place",max_length=100)

    def __str__(self):
        return self.place

class rental_detail(models.Model):
    user_name=models.ForeignKey(credentials,on_delete=models.CASCADE)
    car_name=models.ForeignKey(car_detail,on_delete=models.CASCADE)
    total_cost=models.IntegerField("tcost")
    start_date=models.DateField("sdate")
    end_date=models.DateField("edate")
    pick_place=models.CharField("pplace",max_length=100)
    drop_place=models.CharField("dplace",max_length=100)

class rental_history(models.Model):
    user_name=models.ForeignKey(credentials,on_delete=models.CASCADE)
    car_name=models.ForeignKey(car_detail,on_delete=models.CASCADE)
    total_cost=models.IntegerField("tcost")
    start_date=models.DateField("sdate")
    end_date=models.DateField("edate")
    pick_place=models.CharField("pplace",max_length=100)
    drop_place=models.CharField("dplace",max_length=100)

