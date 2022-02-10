from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import AboutMe, Services, Contact
from myapp.forms import emailform
from django.core.mail import send_mail

# Create your views here.
def index(request):
    service = Services.objects.all()
    about_me = AboutMe.objects.all()
    if request.method == "POST":
        contact = Contact()
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        messages.success(request, 'Thanx for contacting, Message Sent Successfully.')
        return redirect('index')
    return render(request,'index.html', {'services' : service, 'aboutme': about_me})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used!')
                return redirect('register')
            elif User.objects.filter(username = username).exists():
                messages.info(request, 'Username is already taken, Please use different.')
                return redirect('register')
            else:
                user = User.objects.create(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Password is not same!')
            return redirect('register')
    else:
        return render(request, 'register.html')
    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
        
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def email(request):
    if request.method == 'GET':
        form = emailform()
    else:
        form = emailform(request.POST)
        if form.is_valid():
            frommail = form.cleaned_data['fromemail']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            data = {
                'frommail' : frommail,
                'subject' : subject,
                'message' : message
            }
            message = '''
            New message: {}
            
            From: {}
            '''.format(data['message'], data['frommail'])
            send_mail(subject,message,frommail,['msounjai@gmail.com'])
            return redirect('index')
    return render(request, 'email.html', {'form': form})

