from django.urls import path, include

from rest_framework import routers
from .viewsets import ReadonlyEmojiViewSet, EmojiViewSet

router = routers.DefaultRouter()
router.register(r'emojis', EmojiViewSet)
router.register(r'readonly-emojis', ReadonlyEmojiViewSet)

from pprint import pprint
print('emoji-router')
pprint(router.urls)

urlpatterns = [
    path('', include(router.urls)),
]
