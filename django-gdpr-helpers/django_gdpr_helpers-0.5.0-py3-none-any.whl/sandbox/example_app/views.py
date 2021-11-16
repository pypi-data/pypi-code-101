from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from .forms import ExampleForm


class ExampleView(FormView):
    template_name = "example_app/example.html"
    form_class = ExampleForm
    success_url = reverse_lazy("example")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
