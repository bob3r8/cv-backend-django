from django.contrib import admin

from .models import WorkExperience, Worker, Education, SkillsList

admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(Worker)
admin.site.register(SkillsList)