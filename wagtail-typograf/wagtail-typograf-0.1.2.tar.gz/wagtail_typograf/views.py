import json
import logging
from importlib import import_module


from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt


logger = logging.getLogger(__name__)


TYPOGRAF_CLASS = getattr(
    settings,
    "WAGTAIL_TYPOGRAF",
    "wagtail_typograf.handlers.Typograf",
)


@csrf_exempt
@staff_member_required
def typograf_api(request, **kwargs):
    if request.method != "POST":
        logger.debug("Typograf bad request")
        return HttpResponse(status=405)

    try:
        data_json = json.loads(request.body)

        # import
        module_name, cls_name = TYPOGRAF_CLASS.rsplit(".", 1)
        module_obj = import_module(module_name)
        cls_obj = getattr(module_obj, cls_name)

        # process
        for block in data_json["blocks"]:
            block["text"] = cls_obj(block["text"]).process()
    except Exception as exc:
        response = JsonResponse(
            {
                "success": False,
                "error": exc.__str__(),
            }
        )
    else:
        response = JsonResponse(
            {
                "success": True,
                "data": data_json,
            }
        )

    logger.debug(
        "Typograf response: %s...",
        response.content[:100],
    )

    return response
