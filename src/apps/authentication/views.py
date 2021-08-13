from django.http import JsonResponse
from rest_framework.generics import GenericAPIView


class TestAPI(GenericAPIView):
    http_method_names = ("get",)

    def get(self, request):
        return JsonResponse({"message": "Success"})
