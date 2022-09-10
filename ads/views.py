import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from ads.models import Ads
from ads.serializers import AdsSerializer, AdDetailSerializer, AdCreateSerializer, AdUpdateSerializer, \
    AdDestroySerializer


class AdsListView(ListAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer

    def get(self, request, *args, **kwargs):
        category_id = request.GET.get('cat', None)
        if category_id:
            self.queryset = self.queryset.filter(category__exact=category_id)

        name = request.GET.get("text", None)
        if name:
            self.queryset = self.queryset.filter(name__icontains=name)

        location = request.GET.get("location", None)
        if location:
            self.queryset = self.queryset.filter(author__locations__name__icontains=location)

        price_from = request.GET.get("price_from", None)
        price_to = request.GET.get("price_to", None)
        if price_from:
            self.queryset = self.queryset.filter(price__gte=price_from, price__lte=price_to)


        return super().get(request, *args, **kwargs)


    


class AdsDetailView(RetrieveAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdDetailSerializer


class AdsCreateView(CreateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdCreateSerializer


class AdsUpdateView(UpdateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdUpdateSerializer


class AdsDeleteView(DestroyAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdDestroySerializer


@method_decorator(csrf_exempt, name="dispatch")
class AdsUploadImageView(UpdateView):
    model = Ads
    fields = ["name", "author", "price", "description", "is_published", "image", "category"]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.image = request.FILES["image"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author_id": self.object.author_id,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "category": self.object.category,
            "image": self.object.image.url if self.object.image else None
        })
