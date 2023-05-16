from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
  
from django.views.generic import FormView
from app.forms import *

class CBV_FormView(FormView):
    template_name='CBV_FormView.html'
    form_class=SchoolForm


    def form_valid(self, form):
        form.save()
        return HttpResponse('Form Data Is Submitted Successfully')
