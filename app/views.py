from django.shortcuts import render
from app.forms import *
from django.core.mail import send_mail
from django.http import HttpResponse

def registration(request):
    Emptyuser=UserMF()
    Emptyprofile=ProfileMF()
    d={'Emptyuser':Emptyuser,'Emptyprofile':Emptyprofile}

    if request.method=='POST' and request.FILES:
        Notmodifyuser=UserMF(request.POST)
        Notmodifyprofile=ProfileMF(request.POST,request.FILES)

        if Notmodifyuser.is_valid() and Notmodifyprofile.is_valid():

            Modifyuser=Notmodifyuser.save(commit=False)
            PW=Notmodifyuser.cleaned_data['password']         
            Modifyuser.set_password(PW)                 # coverts 12345 → hashed password
            Modifyuser.save()

            Modifyprofile=Notmodifyprofile.save(commit=False)
            Modifyprofile.username=Modifyuser
            Modifyprofile.save()

            send_mail(
                    'Registration',
                    'Your registration is successfull',
                    'p282675@gmail.com',
                    [Modifyuser.email],
                    fail_silently=False
            )
            return HttpResponse('registration Done ')
        return HttpResponse('Invalid')
    
    return render(request,'registration.html',d)