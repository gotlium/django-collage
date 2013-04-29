from django.views.generic import ListView
from models import Entity


class EntityView(ListView):
    template_name = 'collage/list.html'
    context_object_name = 'entity_list'
    model = Entity
