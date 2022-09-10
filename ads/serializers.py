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


class AdCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

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