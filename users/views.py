import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from users.models import User


class UserListView(ListView):
    model = User

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        response = []
        for i in self.object_list:
            response.append(
                {
                    "id": i.id,
                    "name": i.name
                }
            )
        return JsonResponse(response, safe=False, status=200)


class UserDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        try:
            user = self.get_object()
        except User.DoesNotExist:
            return JsonResponse({"error": "Not Found"}, status=404)

        return JsonResponse({
            "id": user.id,
            "name": user.name
        })


@method_decorator(csrf_exempt, name="dispatch")
class UserCreateView(CreateView):
    model = User
    fields = ["name"]

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        new_user = json.load(request.body)

        User = self.objects.create(
            first_name=new_user["first_name"],
            second_name=new_user["second_name"],
            username=new_user["username"],
            password=new_user["password"],
            role=new_user["role"],
            age=new_user["age"],
            location_id=new_user["location_id"]
        )

        return JsonResponse({
            "id": User["id"],
            "name": User["name"],
        })


class UserUpdateView(UpdateView):
    model = User
    fields = ["name"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        user = json.loads(request.body)

        self.object.name = user["name"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name
        })


class UserDeleteView(DeleteView):
    model = User
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({
            "status": "deleted"
        })
