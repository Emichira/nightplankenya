from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

def contact_page(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']

        contact = Contact(name=name, email=email, phone=phone, message=message, user_id=user_id )

        contact.save()

        # Send email
        send_mail(
            'Night Plan Kenya Contact Us Message',
            'There has been a Night Plan Kenya message received from '+ name +'. \nSign into the Night Plan Kenya Admin Panel for more info. The message reads as follows: \n' + message,
            'nightplankenya@gmail.com',
            ['nightplankenya@gmail.com'],
            fail_silently=False
        )

        messages.success(request, 'Your message has been submitted. Thank You ')


    context = {
    }

    return render(request, "pages/contacts.html", context)
