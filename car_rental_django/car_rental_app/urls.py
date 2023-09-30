from django.urls import path
from . import views
car=views.car_rental()
urlpatterns = [
    path('login/',car.login,name="login"),
    path('login/<str:error>',car.login,name="login"),
    path('signup/',car.register,name="signup"),
    path('home/',car.home,name="home"),
    path("forgot_password/",car.forgot,name="forgot"),
    path("change_password/",car.change_passwd,name="change_passwd"),
    path("select_car/",car.car_select,name="select_car"),
    path("profile/",car.profile,name="profile"),
    path("signout/",car.signout,name="signout"),
    path("car_single/<str:car_name>/",car.single_car,name="car_single"),
    path("payment/",car.payment,name="payment"),
    path("success/",car.success,name="success")
]
