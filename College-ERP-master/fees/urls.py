from django.urls import path, include
from . import views
from django.contrib import admin


urlpatterns = [
    # path('fees/', views.fees, name='fees'),
    path('fees/<slug:student_usn>/',
         views.fees, name='fees'),
]