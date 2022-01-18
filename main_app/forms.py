from django.forms import ModelForm
from .models import Resume, Education

class ResumeForm(ModelForm):
  class Meta:
    model = Resume
    fields = ['skills']

class EducationForm(ModelForm):
  class Meta:
    model = Education 
    fields = '__all__'       