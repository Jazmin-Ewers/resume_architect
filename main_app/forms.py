from django.forms import ModelForm
from django import forms 
from .models import Resume, Education, Contact, Skill

# class CustomModelMultipleChoiceField(forms.ModelMultipleChoiceField):
#     def label_from_instance(self, contact):
#         """ Customises the labels for checkboxes"""
#         return "%s" % contact.first_name

# class ResumeForm(forms.ModelForm):
#   class Meta:
#     model = Resume
#     fields = ['contact']

#     def __init__(self, *args, **kwargs):
#       super(ResumeForm, self).__init__(*args, **kwargs)
#       self.fields['contact'].widget = forms.widgets.CheckboxSelectMultiple()
#       self.fields['contact'].queryset = Contact.objects.all()

# class ResumeForm(forms.ModelForm):
#   # def __init__(self, *args, **kwargs):
#   #   self.request = kwargs.pop('request')
#   #   super(ResumeForm, self).__init__(*args, **kwargs)
#   #   self.fields['contacts'].queryset = Contact.objects.all() 

#   class Meta:
#     model = Resume
#     fields = ['contact']

#     # members = CustomModelMultipleChoiceField(
#     #   queryset=None,
#     #   widget=forms.CheckboxSelectMultiple

#     contact = forms.ModelMultipleChoiceField(
#       queryset = Contact.objects.all(),
#       widget = forms.CheckboxSelectMultiple
#     )

class EducationForm(ModelForm):
  class Meta:
    model = Education 
    fields = '__all__'       

class ContactForm(ModelForm):
  class Meta:
    model = Contact 
    fields = '__all__'     