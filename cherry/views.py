from django.shortcuts import render
from cherry.forms import *
from django.views.generic import FormView
from django.http import HttpResponse 
# Create your views here.

class cbv_form(FormView):
    template_name='cbv_form.html'
    form_class=StudentForm

    def form_valid(self,form):
        form.save()


        return HttpResponse('Form is Submitted')
    
    