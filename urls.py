from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quiz/', views.quiz, name='quiz'),
    path('get_quiz/', views.get_quiz, name='get_quiz'),
    path('submit_quiz/', views.submit_quiz, name='submit_quiz'),
    path('add_question/', views.add_question, name='add_question'),  # Add this line
]
