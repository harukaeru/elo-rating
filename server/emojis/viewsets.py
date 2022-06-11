from rest_framework import viewsets, mixins
from rest_framework.schemas.openapi import AutoSchema

from .models import Emoji
from .serializers import EmojiSerializer, DoubleEmojiSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

class ReadonlyEmojiViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    schema = AutoSchema(operation_id_base='readonly-emoji')
    queryset = Emoji.objects.all().order_by('-score')
    serializer_class = EmojiSerializer


class EmojiViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Emoji.objects.all().order_by('-score')
    serializer_class = EmojiSerializer

    def get_serializer_class(self):
        if self.action == 'decide_one':
            return DoubleEmojiSerializer
        return self.serializer_class

    def list(self, request, format=None):
        # enough fast
        # SELECT "emojis_emoji"."id", "emojis_emoji"."text", "emojis_emoji"."score" FROM "emojis_emoji" ORDER BY RANDOM() ASC LIMIT 2
        randomized_queryset = self.queryset.order_by('?')[0:2]
        serializer = EmojiSerializer(randomized_queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], permission_classes=[])
    def decide_one(self, request, format=None):
        serializer = DoubleEmojiSerializer(data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
