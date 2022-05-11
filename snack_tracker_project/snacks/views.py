from tempfile import tempdir
from django.shortcuts import render
from django.views.generic import ListView,DetailView,TemplateView
from .models import Snack


class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack
    context_object_name = 'snack_list'       
    print(context_object_name)
class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack
    
class SnackBaseView(TemplateView):
    template_name = "base.html"
