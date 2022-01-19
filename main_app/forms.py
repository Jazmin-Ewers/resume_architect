from django.forms import ModelForm
from .models import Education, Contact, Skill, Resume

class EducationForm(ModelForm):
  class Meta:
    model = Education 
    fields = '__all__'       

class ContactForm(ModelForm):
  class Meta:
    model = Contact 
    fields = '__all__' 
