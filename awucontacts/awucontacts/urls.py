from django.conf.urls.defaults import patterns
from django.views.generic import list_detail

import awucontacts.views
import awucontacts.models

# magic to enable generic list views
# def info_for_model(model):
#     return {
#         'queryset':   model.objects.all(),
#         'allow_empty': True,
#         'extra_context' : {'object_type' : model.__name__,}
#         }




urlpatterns = patterns(
    '',

    (r'^$', awucontacts.views.index),
    )
