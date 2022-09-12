from modeltranslation.translator import register, TranslationOptions
from .models import WorkExperience, Worker, Education, SkillsList

@register(WorkExperience)
class WorkExperienceTranslationOpts(TranslationOptions):
    fields = ('organization_name', 'position', 'description')

@register(Worker)
class WorkerTranslationOpts(TranslationOptions):
    fields = ('desired_position', 'summary', 'name')

@register(Education)
class EducationTranslationOpts(TranslationOptions):
    fields = ('institution', 'degree', 'speciality', 'qualification')

@register(SkillsList)
class SkillsListTranslationOpts(TranslationOptions):
    fields = ('languages', 'soft_skills')
