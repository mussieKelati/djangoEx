from django.shortcuts import render
from django.http import HttpResponseNotFound,HttpResponse
def monthchalenge(request,month):                                ## THIS (THIRD_APP)DJANGO CODE IS EXERCISE FOR DYNAMIC PATH ####
    chalenge_list = None
    if month == 'jan':
        chalenge_list= 'its NEW YEAR CONGRATS'
    elif month == 'feb':
        chalenge_list = 'welcome to new febraruy '
    elif month == 'april':
        chalenge_list == 'MONTH OF FASTING'
    else:
        return HttpResponseNotFound('sorry ! we dont have data for this data')
    return HttpResponse(chalenge_list)