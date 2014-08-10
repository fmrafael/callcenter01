# -*- coding: utf-8 -*- 

from django.shortcuts import render
from django_twilio.decorators import twilio_view
from twilio.twiml import Response
from django_twilio.client import twilio_client
from django.http import HttpResponseRedirect
from sms.forms import ClienteForm


    
#Page views   
    
def home(request):
    if request.method == 'POST': 
        form = ClienteForm(request.POST) 
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect('/thanks/') 
    else:
        form = ClienteForm() 
    return render(request, 'index.html', {'Cliente_sms':form})
   
   
def thanks(request):
    return render(request, 'thanks.html')   

    

# Twilio controller
# r= Twilio Response

r = Response()

@twilio_view
def gather(request):
    with r.gather(action='/response/', numDigits=1) as i:
        i.play('http://bit.ly/phaltsw')
        
        
    return r
        
@twilio_view
def handle_response(request):        
    digits = request.POST.get('Digits', '')
    r = Response()
    if digits == '1':
        r.say(voice="alice", language="pt-BR", text= u"Esta ligação está sendo gravada")
        r.dial(callerId="+5511983600707", record = 'true', number = "+551233228415")
    if digits == '2':
        r.say("+5511983600707")
            
        
    return r


