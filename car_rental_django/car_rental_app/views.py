from http.client import HTTPResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import *
from .models import *
import random
from . import mail
import os,datetime
class car_rental:
    def __init__(self):
        self.email=""
        self.name=""
        self.otp=0
        self.detail={}
    def home(self,request):
        if request.method=="POST":
            self.detail.clear()
            if len(request.POST)==5:
                detail=dict(request.POST)
                f=next(iter(detail))
                detail.pop(f)
                for i in detail:
                    self.detail[i]=str(detail[i][-1])
                return redirect("select_car")    
            else:
                self.detail
                return redirect("home")
        else:
            place=places.objects.all()
            if self.name:
                return render(request,"home.html",{"profile":"yes","data":place})
            else:
                return render(request,"home.html",{"profile":"no","data":place})
    def login(self,request,error=None):
        if request.method == "POST":
            form=login_form(request.POST)
            if form.is_valid():
                uname1=form.cleaned_data['name']
                passwd1=form.cleaned_data['password']
                try:
                    cr=credentials.objects.get(name=uname1)
                    if cr.name==uname1 and cr.password==passwd1:
                        self.name=uname1
                        self.email=cr.email
                        return redirect("home")
                    else:
                        return render(request,"login.html",{"error":"User Name or Password is wrong","form":form})
                except:
                    form=login_form
                    return render(request,"login.html",{"error":"User Name or Password is wrong","form":form})
            else:
                form=login_form
                error="Please enter valid credentials"
                return render(request,"login.html",{"error":error,"form":form})
        else:
            form=login_form
            return render(request,"login.html",{"form":form,"error":error})
    def register(self,request):
        if request.method=="POST":
            form=register_form(request.POST)
            if form.is_valid:
                try:
                    form.save()
                    return redirect("login")
                except:
                    form=register_form
                    return render(request,"register.html",{"form":form,"error":"Email Address already exist"})
            else:
                form=register_form
                return render(request,"register.html",{"form":form,"error":"Please enter valid credentials"})
        else:
            form=register_form
            return render(request,"register.html",{"form":form})
    count=0
    def forgot(self,request):
        if request.method == "POST":
            dat=request.POST
            if "email" in dat:
                self.email=dat["email"]
                try:
                    if credentials.objects.get(email=self.email):
                        self.otp=random.randint(1111,9999)
                        try:
                            mail.sendotp(self.otp,self.email)
                        except:
                            return render(request,"forgot.html",{"error":"Fail to send otp please try again"})
                        return render(request,"forgot.html",{"otp":"otp"})
                except:
                    return render(request,"forgot.html",{"error":"Email do not exist"})
            elif "otp" in dat:
                otp=request.POST["otp"]
                if self.otp==int(otp):
                    usr=credentials.objects.get(email=self.email)
                    return redirect("change_passwd")
                else:
                    self.count+=1
                    if self.count>=3:
                        self.count=0
                        return render(request,"forgot.html",{"error":"OTP verification fail"})
                    else:
                        return render(request,"forgot.html",{"otp":"otp"})
        else:
            return render(request,"forgot.html")
    def change_passwd(self,request):
        if request.method=="POST":
            pas=request.POST["password"]
            usr=credentials.objects.get(email=self.email)
            usr.password=pas
            usr.save()
            return redirect("home")
        else:
            return render(request,"change_password.html")
    def car_select(self,request):
        if request.method == "POST":
            self.detail["car_name"]=request.POST["car"]
            return redirect('payment')
        else:
            prices=car_detail.objects.all()
            data={}
            for i in prices:
                if i.stocks>0:
                    data[i.car_name]=i.cost_per_hr
                    data[i.car_name+"instock"]="yes"
                else:
                    data[i.car_name]=i.cost_per_hr
            if self.detail:
                if len(self.detail)>4:
                    self.detail.popitem()
                return render(request,"select_car.html",{"data":data})
            else:
                return redirect("home")
    def profile(self,request):
        if request.method=="POST":
            id=request.POST['id']
            try:
                value=rental_detail.objects.get(id=id)
                r=rental_history(user_name=credentials.objects.get(name=value.user_name),
                                car_name=car_detail.objects.get(car_name=value.car_name),
                                total_cost=value.total_cost,
                                start_date=value.start_date,
                                end_date=value.end_date,
                                pick_place=value.pick_place,
                                drop_place=value.drop_place
                                )
                r.save()
                stock=car_detail.objects.get(car_name=value.car_name)
                stock.stocks+=1
                stock.save()
                value.delete()
                return redirect("profile")
            except:
                return render(request,"profile.html",{"error":"ID do not exist"})
        else:
            data1=rental_detail.objects.all()
            data2=credentials.objects.get(name=self.name)
            data3=rental_history.objects.all()
            if self.name=="admin":
                return render(request,"profile.html",{"data1":data1,"admin":"admin","data2":data2,"data3":data3})
            else:
                content=[]
                for i in data3:
                    if str(i.user_name)==self.name:
                        content.append(i)
                print(content)
                return render(request,"profile.html",{"data3":content,"data2":data2})
    def signout(self,request):
        self.name=''
        self.email=''
        return redirect("home")
    def single_car(self,request,car_name):
        detail=car_detail.objects.get(car_name=car_name)
        return render(request,"car_single.html",{"name":car_name,"url":f'\static\images\{car_name}.jpg',"detail":detail})
    def payment(self,request):
        if request.method=="POST":
            mail.sendpaydetail(self.detail,self.name,self.email)
            create_record=rental_detail(user_name=credentials.objects.get(name=self.name),
                            car_name=car_detail.objects.get(car_name=self.detail.get("car_name")),
                            total_cost=self.detail.get("price"),
                            start_date=self.detail.get("pickupdate"),
                            end_date=self.detail.get("dropoffdate"),
                            pick_place=self.detail.get("pickup"),
                            drop_place=self.detail.get("dropoff"))
            create_record.save()
            stock=car_detail.objects.get(car_name=self.detail.get("car_name"))
            stock.stocks-=1
            stock.save()
            return redirect("success")
        else:
            if self.name:
                sd=list(map(int,str(self.detail.get("pickupdate")).split("-")))
                ed=list(map(int,str(self.detail.get("dropoffdate")).split("-")))
                value=(datetime.date(ed[0],ed[1],ed[2])-datetime.date(sd[0],sd[1],sd[2])).days
                if value<=0:
                    value=1
                cost=car_detail.objects.get(car_name=self.detail["car_name"])
                self.detail["price"]=cost.cost_per_hr*value
                return render(request,"payment.html",{"detail":self.detail,"name":self.name})
            else:
                return redirect("login","Please Login")
    def success(self,request):
        if len(self.detail)>5:
            return render(request,"success.html")
        else:
            return redirect("home")