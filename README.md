
# Car Rental

## Description
This project comprises a specific admin panel session and an authentication system. The user may create an account, log in, and access their profile. The user's information, two options to reset their password and sign out, and information about their transactions are all found on the profile page. 

The user can reset their password by selecting the forgot password link on the login page or the reset button on the profile page. After the user enters their email address, an OTP is sent to that email address, and the user can change their password after entering the OTP.

Users may choose their preferred pick-up and drop-off locations, as well as the pick-up and drop-off times, before choosing the automobile of their choice. After making all of the necessary selections, the user may eventually move on to the payment session, where all the information will be shown. The user will receive their bill in their email following a successful payment.


## Installation

```
$ git clone https://github.com/Tarunpurohit146/car_rental.git
$ cd car_rental
$ cd bin
$ source activate
$ pip install django
```
Change the EMAIL and PASSWD field in ```mail.py```
```
EMAIL= 'Enter_you_Email'
PASSWD= 'Enter_password'
```
Run the code
```
python3 manage.py runserver
```
