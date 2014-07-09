from django.shortcuts import render
from django_twilio.decorators import twilio_view
from twilio.twiml import Response
#from django.http import HttpResponse

@twilio_view
def sms(request):
    r = Response()
    r.message('Hello World!')
    return r 
    
def home(request):
    return render(request, 'index.html',{})
   
   


    
# Create your views here.
