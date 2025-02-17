from django.shortcuts import render


def project_management_doc(request):
    return render(request, "docs/project_management.html")

def deployment_doc(request):
    return render(request, "docs/centurion_deployment.html")

def best_practices_doc(request):
    return render(request, "docs/centurion_best_practices_and_standards.html")