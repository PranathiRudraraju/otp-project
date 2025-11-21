import random
from django.shortcuts import redirect, render
from django.core.mail import send_mail

import OTP

# Create your views here.
def login_view(request):
    email=request.POST.get('email')
    otp=str(random.randint(1000,9999))
    request.session['email']=email
    request.session['otp']=otp
    send_mail(
        'your otp code',
        f'Your otp is:{otp}',
        'pranathirudraraju80@gmail.com',
        [email],
    )
    if request.method=='POST':
        return redirect('verify_otp')
    return render(request,'app/login.html')

def verify_otp(request):
    if  request.method=='POST':
        user_otp=request.POST.get('user_otp')
        session_otp=request.session.get('otp')
        if user_otp == session_otp:
            return render(request,'app/success.html')
        else:
            return render(request,'app/failure.html')
    return render(request,'app/verify_otp.html')
