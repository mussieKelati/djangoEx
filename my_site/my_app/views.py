from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect

articles = {
    'sportpage':'sportnews',
    'financepage':'monthlysalary',
    'poltics':'breaking news'

}

def news_paper(request,topic):   
    try:
        result= articles[topic]
        return HttpResponse(articles[topic])
    except:
       result = "NO PAGE FOR THIS TOPIC"
       return HttpResponseNotFound(result) 

def add_view(request,num1,num2):
     result = num1 + num2
     return HttpResponse(str(f'the result is {result}'))



