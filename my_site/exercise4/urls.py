from . import views
from django.urls import path

urlpatterns = [                                         ## THIS (Texercise 4)DJANGO CODE IS EXERCISE FOR path converter####

  path('<str:month>',views.monthchalenge),
  path('<int:month>',views.month_chalenge_bynumber)



]