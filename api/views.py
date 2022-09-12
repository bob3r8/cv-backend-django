# from django.shortcuts import render
from django.http import JsonResponse, Http404
# from django.template import loader
from django.utils.translation import get_language

import json
import traceback

from .models import Worker
from .serializers import *

def index(request):
    try:
        worker = Worker.objects.all()[0]
    except:
        raise Http404("Resume does not exist")
    education = EducationSerializer(worker.education,
        context={'request': request})
    work_experience_list = WorkExperienceSerializer(worker.workexperience_set.all(),
        many=True, context={'request': request})
    skills_list = SkillsListSerializer(worker.skillslist,
        context={'request': request})
    worker = WorkerSerializer(worker,
        context={'request': request})

    context = {
        'worker': worker.data,
        'work_experience_list': work_experience_list.data,
        'skills_list': skills_list.data,
        'education': education.data
    }
    return JsonResponse(context, content_type="application/json")
