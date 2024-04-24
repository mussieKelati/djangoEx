from django.urls import path
from . import views

urlpatterns = [

path('<int:num_page>/',views.num_page_view),
    path('<topic>/', views.news_paper),
   
     path('<int:num1>/<int:num2>/',views.add_view),
]









