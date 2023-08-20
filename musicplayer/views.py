# Create your views here.
from django.shortcuts import render, redirect

# imported our models
from django.core.paginator import Paginator
from music.models import audio

def index(request):
    paginator= Paginator(audio.objects.all(),1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={"page_obj":page_obj}
    return render(request,"mp_template1.html",context)