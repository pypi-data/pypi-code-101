from django.views.generic import TemplateView
from apis_core.apis_entities.models import Institution, Person
from apis_core.apis_vocabularies.models import PersonInstitutionRelation
from django.http import JsonResponse
import json


class StartView(TemplateView):
    template_name = "vis_base.html"

    def get_context_data(self, **kwargs):
        vis_type = self.kwargs.get("vis_type", "tree")
        context = {"vis_type" : vis_type}
        return context


def autocomplete_view(request):
    insts = Institution.objects.all()
    pers = Person.objects.all()
    funcs = PersonInstitutionRelation.objects.exclude(name="am Hofstaat")

    temp = [(a.name, "Institution", a.pk) for a in insts] + \
             [(a.name+f", {a.first_name}", "Person", a.pk) for a in pers] + \
             [(a.name, "Funktion", a.pk) for a in funcs]

    result = [{"label":a[0], "value":list(a), "group":a[1], "pk":a[2]} for a in temp]

    response_data = json.dumps(result)
    return JsonResponse(response_data, safe=False)
