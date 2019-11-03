from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

# Create your views here.

def contact(request):
     if request.method == 'POST':
         listing_id = request.POST['listing_id']
         realtor_email = request.POST['realtor_email']
         listing = request.POST['listing']
         name = request.POST['realtor_email']
         email = request.POST['email']
         phone = request.POST['phone']
         message = request.POST['message']
         user_id = request.POST['user_id']
         
         contact = Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)
         contact.save()
         messages.success(request, 'We got your request. We will contact you soon')
         return redirect('/listings/' + listing_id )
