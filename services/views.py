from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from users.models import Address
from services.models import Request, Indicators, Counter


def request_detail(request, uuid):
    context = {
        "request": Request.objects.filter(number=uuid).first
    }
    return render(request, "account/request_detail.html", context)


def request_list(request):
    if request.method == "GET":
        context = {
            "requests": Request.objects.filter(user__id=request.user.id)
        }
        return render(request, "account/request_list.html", context)
    
    if request.method == "POST":
        title = request.POST.get("title")
        appeal = request.POST.get("appeal")
        Request.objects.create(
            user=request.user,
            title=title,
            appeal=appeal,
        )
        return redirect("/request-list/")

    return HttpResponse()


def indicators(request):

    if request.method == "GET":
        indicators = Indicators.objects.filter(
            user__id=request.user.id
        ).select_related(
            "user", 
            "address",
            "counter",
        )

        context = {
            "parameters": Counter.objects.all(),

            "INDICATORS_HOT_WATER": Indicators.objects.filter(
                counter__name = Counter.Parameter.INDICATORS_HOT_WATER.value
            ).select_related("address"),

            "INDICATORS_COLD_WATER": Indicators.objects.filter(
                counter__name = Counter.Parameter.INDICATORS_COLD_WATER.value
            ).select_related("address"),

            "INDICATORS_LIGHT_DAY": Indicators.objects.filter(
                counter__name = Counter.Parameter.INDICATORS_LIGHT_DAY.value
            ).select_related("address"),

            "INDICATORS_LIGHT_NIGHT": Indicators.objects.filter(
                counter__name = Counter.Parameter.INDICATORS_LIGHT_NIGHT.value
            ).select_related("address"),

        }

        return render(request, "account/indicators.html", context)

    if request.method == "POST":
        town = request.POST.get("town")
        street = request.POST.get("street")
        house = request.POST.get("house")
        apartment = request.POST.get("apartment")

        address = Address.objects.create(
            town=town,
            street=street,
            house=house,
            apartment=apartment,
        )
        INDICATORS_HOT_WATER = request.POST.get("INDICATORS_HOT_WATER")
        INDICATORS_COLD_WATER = request.POST.get("INDICATORS_COLD_WATER")
        INDICATORS_LIGHT_DAY = request.POST.get("INDICATORS_LIGHT_DAY")
        INDICATORS_LIGHT_NIGHT = request.POST.get("INDICATORS_LIGHT_NIGHT")

        if INDICATORS_HOT_WATER:
            Indicators.objects.create(
                user=request.user,
                counter=Counter.objects.get(name=Counter.Parameter.INDICATORS_HOT_WATER.value),
                indicator=INDICATORS_HOT_WATER,
                address=address,
                date_send=datetime.today(),
            )

        if INDICATORS_COLD_WATER:
            Indicators.objects.create(
                user=request.user,
                counter=Counter.objects.get(name=Counter.Parameter.INDICATORS_COLD_WATER.value),
                indicator=INDICATORS_COLD_WATER,
                address=address,
                date_send=datetime.today(),
            )

        if INDICATORS_LIGHT_DAY:
            Indicators.objects.create(
                user=request.user,
                counter=Counter.objects.get(name=Counter.Parameter.INDICATORS_LIGHT_DAY.value),
                indicator=INDICATORS_LIGHT_DAY,
                address=address,
                date_send=datetime.today(),
            )

        if INDICATORS_LIGHT_NIGHT:
            Indicators.objects.create(
                user=request.user,
                counter=Counter.objects.get(name=Counter.Parameter.INDICATORS_LIGHT_NIGHT.value),
                indicator=INDICATORS_LIGHT_NIGHT,
                address=address,
                date_send=datetime.today(),
            )

        return redirect("/indicators/")

    return HttpResponse()
