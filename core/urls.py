from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('cgpa/', views.cgpa_view, name="cgpa"),
    path('calendar/', views.calendar_view, name="calendar"),
    path('pomodoro/', views.pomodoro_view, name="pomodoro"),
    path('add-event/', views.add_event, name="add_event"),
]