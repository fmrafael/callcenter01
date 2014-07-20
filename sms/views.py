from django.shortcuts import render
from django_twilio.decorators import twilio_view
from twilio.twiml import Response
from django.http import HttpResponseRedirect
from sms.forms import ClienteForm

@twilio_view
def sms(request):
    r = Response()
    r.message('Hello World!')
    return r 
    
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


    
# Create your views here.
