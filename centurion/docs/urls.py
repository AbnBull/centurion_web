from django.urls import path
from .views import project_management_doc, best_practices_doc, deployment_doc

urlpatterns = [
    path('project_management/', project_management_doc, name='project_management_doc'),
    path('best_practices_and_standards/', best_practices_doc, name='best_practices_and_standards_doc'),
    path('deployment/', deployment_doc, name='deployment_doc'),
]