from django.urls import path
from . import views


urlpatterns = [
    path('',views.house,name='house'),
    path('<int:mom_id>/',views.detail,name='detail'),
    ]