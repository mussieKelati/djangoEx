from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect

def simple_view(request):
    return render(request,'sec_app/example.html')





