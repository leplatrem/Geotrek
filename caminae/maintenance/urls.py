from django.conf.urls import patterns

from .views import (
    InterventionLayer, InterventionList, InterventionDetail, InterventionCreate,
    InterventionUpdate, InterventionDelete, InterventionJsonList,
    ProjectLayer, ProjectList, ProjectDetail, ProjectCreate,
    ProjectUpdate, ProjectDelete, ProjectJsonList
)

from caminae.mapentity.urlizor import view_classes_to_url


urlpatterns = patterns('', *view_classes_to_url(
    InterventionLayer, InterventionList, InterventionDetail, InterventionCreate,
    InterventionUpdate, InterventionDelete, InterventionJsonList,
    ProjectLayer, ProjectList, ProjectDetail, ProjectCreate,
    ProjectUpdate, ProjectDelete, ProjectJsonList
))