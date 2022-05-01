from django.shortcuts import render, redirect
from home.models import Contact
from home.models import technology
from home.models import driver
from home.models import service
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from . tokens import generate_token


def sendEmail(sub, data, email):
    send_mail(sub, data, 'agritech1998@gmail.com', [email], fail_silently=True)


def home(request):
    return render(request, 'home/index.html')


def technologies(request):
    data = {'tech_list': list(technology.objects.values())}
    return render(request, 'home/technologies.html', data)


def about(request):
    return render(request, 'home/about.html')


@login_required(login_url='home')
def services(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        weight = request.POST['weight']
        if len(name) < 3:
            messages.error(request, 'Name should not be less than 3 characters!')
        if len(email) < 5:
            messages.error(request, 'email should not be less than 5 characters!')
        if len(phone) < 10:
            messages.error(request, 'Phone number should be atleast 10 digits!')
        if len(address) < 10:
            messages.error(request, 'Address should not be less than 10 characters!')
        if weight > '40':
            messages.error(request, 'Weight should not be more than 40!')
        else:
            if int(weight) <= 8:
                driveby = driver.objects.filter(vehicle='BajajTempo').first()
            elif int(weight) <= 15:
                driveby = driver.objects.filter(vehicle='Tractor').first()
            elif int(weight) >= 25:
                driveby = driver.objects.filter(vehicle='Truck').first()
            services = service(
                name=name, email=email, phone=phone, address=address, weight=weight, user=request.user, driveby=driveby)
            services.save()
            messages.success(request, 'Your data has been sent successfully!')
            email_add = driveby.email
        sendEmail('Collect Stubble', 'Name - {} \nPhone Number- {} \nAddress - {} \nWeight - {} \nCollect stubble as soon as possible.'.format(name, phone, address, weight), email_add)
        sendEmail('AgriTech Stubble Collection', 'Driver Name - {} \nPhone Number- {} \nVehicle - {} \nDriver will be in touch with you as soon as possible.'.format(driveby.name, driveby.phone, driveby.vehicle), email)
    return render(request, 'home/services.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 3 or len(email) < 5 or len(phone) < 10 or len(content) < 5:
            messages.error(request, 'Please fill the form correctly!')
        else:
            contact = Contact(name=name, email=email,
                              phone=phone, content=content)
            contact.save()
            messages.success(
                request, 'Your message has been successfully sent!')
    return render(request, 'home/contact.html')


def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        conpassword = request.POST['conpassword']
        if User.objects.filter(username=phone).exists():
            messages.error(request, 'Phone number already exists!')
            return redirect('/signup')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email address already exists!')
            return redirect('/signup')
        if len(phone) != 10:
            messages.error(request, 'Phone number should be of 10 digits!')
            return redirect('/signup')
        if len(password) < 8:
            messages.error(request, 'Password should be 8 characters long!')
            return redirect('/signup')
        if not password.isalnum():
            messages.error(request, 'Password should Alpha-Numeric!')
            return redirect('/signup')
        if password != conpassword:
            messages.error(request, 'Password do not match!')
            return redirect('/signup')
        myuser = User.objects.create_user(username=phone, password=password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.email = email
        myuser.is_active = False
        myuser.save()
        messages.success(request, 'Confirmation Email sent! Please confirm your email to activate your account!')
        current_site = get_current_site(request)
        email_subject = 'AgriTech - Email Confirmation!'
        email_message = render_to_string('email_confirmation.html', {
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
            email_subject,
            email_message,
            'agritech1998@gmail.com',
            [myuser.email]
        )
        email.fail_silently = True
        email.send()
        return redirect('/login')
    return render(request, 'home/signup.html')


def handlelogin(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        password = request.POST['password']
        user = authenticate(username=phone, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged In!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials, please try again!')
            return redirect('/login')
    return render(request, 'home/login.html')


def handlelogout(request):
    logout(request)
    messages.success(request, 'Successfully logged Out!')
    return redirect('home')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None
    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('home')
    else:
        return redirect(request, 'activation_failed.html')
