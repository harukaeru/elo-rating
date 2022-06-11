from django.db import transaction
from rest_framework import serializers
from .models import Emoji
from .logics import calculate_elo

class EmojiSerializer(serializers.ModelSerializer):
    # has to be declared here to show up in the Browsable API
    id = serializers.IntegerField()

    class Meta:
        model = Emoji
        fields = ['id']
        read_only_fields = ['text', 'score']

    def get_field_names(self, declared_fields, info):
        field_names = super().get_field_names(declared_fields, info)
        return field_names + self.Meta.read_only_fields


class DoubleEmojiSerializer(serializers.Serializer):
    left = EmojiSerializer()
    right = EmojiSerializer()
    decided = EmojiSerializer()

    # It's actually not `create`,
    # but want to call it simply, using the save method.
    def create(self, validated_data):
        left_id = validated_data['left']['id']
        right_id = validated_data['right']['id']

        # sort in advance to avoid the possible deadlock
        if left_id > right_id:
            temp_id = left_id
            left_id = right_id
            right_id = temp_id

        with transaction.atomic():
            left = Emoji.objects.select_for_update().get(id=left_id)
            right = Emoji.objects.select_for_update().get(id=right_id)

            is_left_win = left_id == validated_data['decided']['id']

            left.score, right.score = calculate_elo(
                left.score, right.score, is_left_win
            )
            left.save()
            right.save()

        return {
            'left': left,
            'right': right,
            'decided': left
        }
