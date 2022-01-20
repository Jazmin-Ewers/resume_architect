from django.forms import ModelForm
from .models import Education, Contact, Skill, Resume, Experience

class EducationForm(ModelForm):
  class Meta:
    model = Education 
    fields= ['institution', 'graduation', 'location', 'degree', 'degree_description']    

class ContactForm(ModelForm):
  class Meta:
    model = Contact 
    fields = ['first_name', 'last_name', 'email', 'linkedin', 'github', 'portfolio', 'location', 'job_title']

class ResumeForm(ModelForm):
  class Meta:
    model = Resume 
    fields = ['name', 'date'] 

class SkillForm(ModelForm):
  class Meta:
    model = Skill
    fields = ['name', 'type', 'description']

class ExperienceForm(ModelForm):
  class Meta:
    model = Experience
    fields = ['workplace', 'location', 'start_date', 'end_date', 'description']