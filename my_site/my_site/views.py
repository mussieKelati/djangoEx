from django.http import HttpResponse


def newtab(request):
    return HttpResponse("welcome to new tab")