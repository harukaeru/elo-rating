from django.urls import path

from . import views

urlpatterns = [
    path('get_emojis', views.get_emojis, name='get_mojis'),
    path('decide_emoji', views.decide_emoji, name='decide_emoji'),
]
