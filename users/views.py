import json

from django.core.paginator import Paginator
from django.db.models import Count
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from homework_django import settings
from users.models import User


class UserListView(ListView):
    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        all_users = self.object_list.all().order_by("username").annotate(ads_count=Count("ads", is_published=True))

        paginator = Paginator(all_users, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page', 1)
        page_object = paginator.get_page(page_number)

        users = []
        for user in page_object:
            users.append({
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "username": user.username,
                "role": user.role,
                "age": user.age,
                "locations": list(map(str, user.locations.all())),
                "ads_count": user.ads_count,
            })

        response = {
            "items": users,
            "total": paginator.count,
            "num_pages": settings.TOTAL_ON_PAGE
        }
        return JsonResponse(response, status=200)


class UserDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        try:
            user = self.get_object()
        except User.DoesNotExist:
            return JsonResponse({"error": "Not Found"}, status=404)

        return JsonResponse({
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "password": user.password,
            "role": user.role,
            "age": user.age,

        })


@method_decorator(csrf_exempt, name="dispatch")
class UserCreateView(CreateView):
    model = User
    fields = ["first_name", "last_name", "username", "password", "role", "age", "locations"]

    def post(self, request, *args, **kwargs):
        new_user = json.loads(request.body)

        user = User.objects.create(
            id=new_user["id"],
            first_name=new_user["first_name"],
            last_name=new_user["last_name"],
            username=new_user["username"],
            password=new_user["password"],
            role=new_user["role"],
            age=new_user["age"],
            locations=new_user["locations"],

        )

        return JsonResponse({
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "password": user.password,
            "role": user.role,
            "age": user.age,
        })


@method_decorator(csrf_exempt, name="dispatch")
class UserUpdateView(UpdateView):
    model = User
    fields = ["first_name", "last_name", "username", "password", "role", "age", "locations"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        user = json.loads(request.body)

        self.object.first_name = user["first_name"]
        self.object.last_name = user["last_name"]
        self.object.username = user["username"]
        self.object.password = user["password"]
        self.object.role = user["role"]
        self.object.age = user["age"]

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "first_name": self.object.first_name,
            "last_name": self.object.last_name,
            "username": self.object.username,
            "password": self.object.password,
            "role": self.object.role,
            "age": self.object.age,
        })


@method_decorator(csrf_exempt, name="dispatch")
class UserDeleteView(DeleteView):
    model = User
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({
            "status": "deleted"
        })
