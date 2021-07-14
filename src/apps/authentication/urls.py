from django.urls import include, path
from djoser.views import UserViewSet

from .views import TestAPI

app_name = "authentication"

# Djoser viewset displatch
# https://github.com/sunscrapers/djoser/blob/master/djoser/views.py
SignUpAPIView = UserViewSet.as_view({"post": "create"})

# TODO: Finish with only required routes from Djoser


urlpatterns = [
    # path("", include("djoser.urls")),
    path("", include("djoser.urls.jwt")),
    path("signup/", SignUpAPIView, name="signup"),
    path("test/", TestAPI.as_view(), name="test"),
    # re_path("^test/$", TestAPI.as_view(), name="test"),
]
