
from django.shortcuts import render

def handler404(request, exception, template_name='404.html'):
    return render(request, template_name, status=404,context={ exception: exception})

def handler500(request, template_name='500.html'):
    return render(request, template_name, status=404)

def handler403(request, exception, template_name='403.html'):
    return render(request, template_name, status=403,context={ exception: exception})