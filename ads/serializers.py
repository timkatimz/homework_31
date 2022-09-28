from django.core.exceptions import ValidationError
from rest_framework import serializers

from ads.models import Ads


class AdsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Ads
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Ads
        fields = '__all__'


def check_is_published(value: bool):
    if value:
        raise ValidationError("Неверное значение")


class AdCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    is_published = serializers.BooleanField(validators=[check_is_published])
    class Meta:
        model = Ads
        fields = ['id', "name", "author", "price", "description", "is_published", "image", "category"]


class AdUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Ads
        fields = ['id', "name", "author", "price", "description", "is_published", "image", "category"]


class AdDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = ['id']