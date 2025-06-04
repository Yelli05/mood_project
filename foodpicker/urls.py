from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='food_home'),
    path('random/', views.random_food, name='random_food'),
     path("by-mood/<int:mood_id>/", views.home_by_mood, name="food_by_mood"),
]
