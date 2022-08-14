import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ads, Category


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        response = []
        for i in categories:
            response.append(
                {
                    "id": i.id,
                    "name": i.name
                }
            )
        return JsonResponse(response, safe=False, status=200)

    def post(self, request):
        new_cat = json.load(request)
        cat = Category()

        cat.name = new_cat["name"]

        cat.save()

        return JsonResponse(new_cat)



@method_decorator(csrf_exempt, name="dispatch")
class AdsView(View):
    def get(self, request):
        ads = Ads.objects.all()
        response = []
        for i in ads:
            response.append(
                {
                    "id": i.id,
                    "name": i.name,
                    "author": i.author,
                    "price": i.price,
                    "description": i.description,
                    "address": i.address,
                    "is_published": i.is_published
                }
            )
        return JsonResponse(response, safe=False, status=200)

    def post(self, request):
        new_ad = json.load(request)
        ad = Ads()

        ad.name = new_ad["name"]
        ad.author = new_ad["author"]
        ad.price = new_ad["price"]
        ad.description = new_ad["description"]
        ad.address = new_ad["address"]
        ad.is_published = new_ad["is_published"]

        ad.save()

        return JsonResponse(new_ad)



@method_decorator(csrf_exempt, name="dispatch")
class AdDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        try:
            ad = self.get_object()
        except Ads.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

        return JsonResponse({
                    "id": ad.id,
                    "name": ad.name,
                    "author": ad.author,
                    "price": ad.price,
                    "description": ad.description,
                    "address": ad.address,
                    "is_published": ad.is_published
                })


@method_decorator(csrf_exempt, name="dispatch")
class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        try:
            cat = self.get_object()
        except Category.DoesNotExist:
            return JsonResponse({"error": "Not Found"}, status=404)

        return JsonResponse({
            "id": cat.id,
            "name": cat.name
            })

