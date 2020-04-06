from django.urls import path
from . import views

app_name = 'temp_app'

urlpatterns = [
    path('other/',views.other, name="other"),
]
