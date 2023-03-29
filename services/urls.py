from django.urls import path, include

from .views import request_list, request_detail, indicators

urlpatterns = [
    path("request-list/", view=request_list, name="request_list",),
    path("request-detail/<uuid>/", view=request_detail, name="request_detail",),
    path("indicators/", view=indicators, name="indicators"),
]
