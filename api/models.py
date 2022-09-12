from django.db import models
import json

class Worker(models.Model):
    desired_position =  models.CharField(max_length=32)
    summary =           models.CharField(max_length=1024)
    name =              models.CharField(max_length=32)
    birth_date =        models.DateField()
    phone =             models.CharField(max_length=32)
    e_mail =            models.EmailField()
    site =              models.CharField(max_length=32)
    
    def __str__(self):
        return '%s' % (self.name, )

class SkillsList(models.Model):
    program_langs =     models.JSONField()
    other =             models.JSONField()
    languages =         models.JSONField()
    soft_skills =       models.JSONField()
    worker =            models.OneToOneField(
                            Worker,
                            on_delete=models.CASCADE,
                            primary_key=True)
    def __str__(self):
        return "%s's skills" % (self.worker.name)#'Skills [%s]' % (self.program_langs, )

class Education(models.Model):
    institution =       models.CharField(max_length=64)
    start_date =        models.DateField()
    graduation_date =   models.DateField()
    degree =            models.CharField(max_length=32)
    speciality =        models.CharField(max_length=32)
    qualification =     models.CharField(max_length=32)
    worker =            models.OneToOneField(
                            Worker,
                            on_delete=models.CASCADE,
                            primary_key=True)

    def __str__(self):
        return '%s, %s' % (self.institution, self.qualification)

class WorkExperience(models.Model):
    organization_name = models.CharField(max_length=32)
    position =          models.CharField(max_length=32, blank=True)
    hire_date =         models.DateField(null=True, blank=True)
    fire_date =         models.DateField(null=True, blank=True)
    description =       models.CharField(max_length=512)
    worker =            models.ForeignKey(Worker,
                            on_delete=models.CASCADE)

    def __str__(self):
        return '%s at %s' % (self.position, self.organization_name)

