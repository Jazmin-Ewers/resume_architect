from django.contrib import admin

from .models import Contact, Skill, Experience, Education, Projects, Resume

# Register your models here.
admin.site.register(Contact)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Projects)
admin.site.register(Resume)


