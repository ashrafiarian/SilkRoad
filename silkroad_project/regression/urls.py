from django.urls import path
from . import views

app_name = 'regression'

urlpatterns = [
    path("", views.index, name="index")
]