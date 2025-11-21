import random
from django.shortcuts import redirect, render
from django.core.mail import send_mail


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # Generate OTP
        otp = str(random.randint(1000, 9999))

        # Save to session
        request.session['email'] = email
        request.session['otp'] = otp

        # Send OTP email
        send_mail(
            'Your OTP Code',
            f'Your OTP is: {otp}',
            'pranathirudraraju80@gmail.com',
            [email],
        )

        return redirect('verify_otp')

    return render(request, 'app/login.html')


def verify_otp(request):
    if request.method == 'POST':
        user_otp = request.POST.get('user_otp')
        session_otp = request.session.get('otp')

        if user_otp == session_otp:
            return render(request, 'app/success.html')
        else:
            return render(request, 'app/failure.html')

    return render(request, 'app/verify_otp.html')
