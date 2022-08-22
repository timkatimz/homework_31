import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from ads.models import Ads


class AdsListView(ListView):
    model = Ads

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        response = []
        for ad in self.object_list:
            response.append({
                "id": ad.id,
                "name": ad.name,
                "price": ad.price,
                "description": ad.description,
        })
        return JsonResponse(response, safe=False, status=200)


class AdsDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        try:
            ad = self.get_object()
        except Ads.DoesNotExist:
            return JsonResponse({"error": "Not Found"}, status=404)

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "price": ad.price,
            "description": ad.description,
        })


@method_decorator(csrf_exempt, name="dispatch")
class AdsCreateView(CreateView):
    model = Ads
    fields = ["name", "price", "description"]

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        new_ad = json.loads(request.body)

        ad = Ads.objects.create(
            name=new_ad["name"],
            price=new_ad["price"],
            description=new_ad["description"],

        )

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author_id": ad.author_id,
            "price": ad.price,
            "description": ad.description,
        })


class AdsUpdateView(UpdateView):
    model = Ads
    fields = ["name", "price", "description", "is_published"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        ad = json.loads(request.body)

        self.object.name = ad["name"]
        self.object.price = ad["price"]
        self.object.description = ad["description"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "price": self.object.price,
            "description": self.object.description,

        })


class AdsDeleteView(DeleteView):
    model = Ads
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({
            "status": "deleted"
        })
