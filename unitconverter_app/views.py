from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from .logic.converter import convert


# Create your views here.


def index(request):
    return render(request, "unitconverter_app/index.html")


def result(request):
    try:
        context = {
            "from_unit": request.GET.get("convert-from"),
            "to_unit": request.GET.get("convert-to"),
            "input_num": request.GET.get("input-num"),
            "conversion_type": request.GET.get("conversion-type"),
        }
        converted_value, steps_of_conversion = convert(
            context["from_unit"],
            context["to_unit"],
            context["input_num"],
            context["conversion_type"],
        )
        context["converted_value"] = converted_value
        context["steps_of_conversion"] = steps_of_conversion
        if context["conversion_type"] == "temperature":
            context["from_unit"] = f"°{context['from_unit']}"
            context["to_unit"] = f"°{context['to_unit']}"

    except Exception as e:
        return HttpResponseBadRequest(f"{e}:Invalid input or unit supplied.")
    else:
        return render(request, "unitconverter_app/result.html", context)
