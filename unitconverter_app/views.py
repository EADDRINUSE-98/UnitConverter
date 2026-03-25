from django.shortcuts import render
from django.http import HttpResponse
from .logic.converter import convert


# Create your views here.


def index(request):
    # context = {"result-flag": False}
    return render(request, "unitconverter_app/index.html")


def result(request):
    # return HttpResponse(request.GET.get("input-num"))
    # try:
    context = {
        "from-unit": request.GET.get("convert-from"),
        "to-unit": request.GET.get("convert-to"),
        "input-num": request.GET.get("input-num"),
    }
    converted_value = convert(
        context["from-unit"], context["to-unit"], context["input-num"]
    )

    # except Exception as e:
    #     return HttpResponse(e)
    # else:
    # return render(request, "unitconverter_app/result.html", context)
    return HttpResponse(converted_value)
