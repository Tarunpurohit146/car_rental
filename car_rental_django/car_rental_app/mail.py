import smtplib,ssl
EMAIL= "Enter_you_Email"
PASSWD= "Enter_password"
def sendotp(otp,email):
    msg=f"""
    Welcome to Car Rental
    Your OTP for Password Reset is {otp}
    Please do not share it to any one.
    """
    sl=ssl.create_default_context()
    smt=smtplib.SMTP("smtp.gmail.com",587)
    smt.starttls(context=sl)
    smt.login(user=EMAIL,password=PASSWD)
    smt.sendmail(EMAIL,email,msg)
    smt.close()
def sendpaydetail(detail,name,email):
    mes=f"""
        ~~~~~~~~~~ Car Rental ~~~~~~~~~~~~~

        User Name: {name}
        Car Name: {detail.get("car_name")}
        Pick-Up Date: {detail.get("pickupdate")}
        Pick-Up Place: {detail.get("pickup")}
        Drop Date: {detail.get("dropoffdate")}
        Drop Place: {detail.get("dropoff")}
        
        Total Price: {detail.get("price")}
        
        Thank you for using our services!!!
        """
    sl=ssl.create_default_context()
    smt=smtplib.SMTP("smtp.gmail.com",587)
    smt.starttls(context=sl)
    smt.login(user=EMAIL,password=PASSWD)
    smt.sendmail(EMAIL,email,mes)
    smt.close()
