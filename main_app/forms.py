from django.forms import ModelForm
from .models import Resume, Education, Contact

class ResumeForm(ModelForm):
  class Meta:
    model = Resume
    fields = ['skills']

class EducationForm(ModelForm):
  class Meta:
    model = Education 
    fields = '__all__'       

class ContactForm(ModelForm):
  class Meta:
    model = Contact 
    fields = '__all__'     