from django.shortcuts import render
from django.http import HttpResponseNotFound,HttpResponse,HttpResponseRedirect


month_chalenge = {

    'JAN': 'IT IS NEW YEAR CONGRATS',
    'FEB' : 'WELCOME TO NEW MONTH OF FEBURARY',
    'APRIL': 'FASTING MONTH',
    'MAY': 'EDEPENDENCE DAY'
    
}

def month_chalenge_bynumber (request,month):
   months = list( month_chalenge.keys())
   redirect_month = months[month]
   return HttpResponseRedirect("/exercise4/"+ redirect_month)


def monthchalenge(request,month):                                ## THIS (Texercise 4)DJANGO CODE IS EXERCISE FOR path converter####
   try:
     chalenge_list = month_chalenge[month]
     return HttpResponse(chalenge_list)
   except:
     return HttpResponseNotFound('sorry ! we dont have data for this data')
    
