from django.shortcuts import render

from django.conf import settings
import os
import markdown

from .models import Employee

# Create your views here.

def home(request):
    return render(request, 'home.html')

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def readme(request):
    readme_path = os.path.join(settings.BASE_DIR, 'README.md')
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    html_content = markdown.markdown(content)
    return render(request, 'readme.html', {'content': html_content})