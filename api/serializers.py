from rest_framework import serializers
from .models import Worker, SkillsList, Education, WorkExperience

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ('id', 'name', 'birth_date', 'phone', 
            'e_mail', 'site', 'desired_position', 'summary')

class SkillsListSerializer(serializers.ModelSerializer):
    class Meta:
         model = SkillsList
         fields = ('worker_id', 'program_langs', 
            'other', 'languages', 'soft_skills')

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
         model = Education
         fields = ('worker_id', 'institution', 'start_date', 
            'graduation_date', 'degree', 'speciality', 'qualification')

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
         model = WorkExperience
         fields = ('id', 'worker_id', 'organization_name', 
            'position', 'hire_date', 'fire_date', 'description')
