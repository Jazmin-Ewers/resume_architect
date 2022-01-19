from ast import Delete
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import EducationForm, ContactForm, ResumeForm, SkillForm, ExperienceForm

from main_app.models import *

# Create your views here.
def home(request):
  return render(request, 'home.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('resumes_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def skills_index(request):
  # Filter skills once user model has been connected to Skill model
  # skill = Skill.objects.filter(user=request.user)
  skills = Skill.objects.all()
  skills_form = SkillForm()
  return render(request, 'skills/index.html', {
    'skills': skills,
    'skills_form': skills_form
    })

class SkillCreate(CreateView):
  model = Skill
  fields = '__all__'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class SkillUpdate(UpdateView):
  model = Skill
  fields = '__all__'

class  SkillDelete(DeleteView):
  model = Skill
  success_url = '/skills/'

class ResumeCreate(CreateView):
  model = Resume
  fields = ['name', 'date']

# def resume_create(request):
#   contacts = Contact.objects.all()
#   skills = Skill.objects.all()
#   projects = Projects.objects.all()
#   experiences = Experience.objects.all()
#   educations = Education.objects.all()

def resumes_index(request):
  resumes = Resume.objects.all()
  return render(request, 'resumes/index.html', {'resumes': resumes})

def resumes_detail(request, resume_id):
  resume = Resume.objects.get(id=resume_id)
  skills = Skill.objects.all()
  contacts = Contact.objects.all()
  projects = Projects.objects.all()
  experiences = Experience.objects.all()
  educations = Education.objects.all()
  resume_form = ResumeForm()
  skills_resume_doesnt_have = Skill.objects.exclude(id__in=resume.skills.all().values_list('id'))
  return render(request, 'resumes/detail.html',  {
    'resume': resume,
    'skills': skills_resume_doesnt_have,
    'contacts': contacts,
    'projects': projects,
    'experiences': experiences,
    'educations': educations,
    'resume_form': resume_form,
  })

def resumes_print(request, resume_id):
  resume = Resume.objects.get(id=resume_id)
  skills = resume.skills.all()
  return render(request, 'resumes/print.html', {
    'resume': resume,
    'skills': skills
    })  

# def cats_detail(request, cat_id):
#       cat = Cat.objects.get(id=cat_id)
#       if cat.user == request.user:
#     # instantiate FeedingForm to be rendered in the detail.html template
#     feeding_form = FeedingForm()
#     # find all toys not associated with this cat
#     toys_cat_doesnt_have = Toy.objects.exclude(id__in=cat.toys.all().values_list('id'))
#     return render(request, 'cats/detail.html', {
#       'cat': cat,
#       'feeding_form': feeding_form,
#       'toys': toys_cat_doesnt_have
#     })
#   else:
#     return redirect('cats_index')

def assoc_skill(request, resume_id, skill_id):
  resume=Resume.objects.get(id=resume_id)
  resume.skills.add(skill_id)
  return redirect('resumes_detail', resume_id=resume_id)

def educations_index(request):
  educations = Education.objects.all()
  educations_form = EducationForm()
  return render(request, 'educations/index.html', {
    'educations': educations,
    'educations_form': educations_form
    }) 

class EducationCreate(CreateView):
  model= Education
  fields= '__all__'

class EducationUpdate(UpdateView):
  model = Education
  fields = '__all__'

class EducationDelete(DeleteView):
  model = Education
  success_url = '/educations/'

  
def contacts_index(request):
  contacts = Contact.objects.all()
  contacts_form = ContactForm()
  return render(request, 'contacts/index.html', {
    'contacts': contacts,
    'contacts_form': contacts_form
  })

# def contacts_create(request):
#   if request.method == 'POST':
#     form = ContactForm(request.POST)
#     # Contact.objects.create(form)
#     if form.is_valid():
#       new_contact = form.save(commit=False)
#       new_contact.save()
#     return redirect('contacts_index')

class ContactCreate(CreateView):
  model= Contact
  fields= '__all__'

class ContactUpdate(UpdateView):
  model = Contact
  fields = '__all__'

class ContactDelete(DeleteView):
  model = Contact
  success_url = '/contacts/'


def experiences_index(request):
  experiences = Experience.objects.all()
  experiences_form = ExperienceForm()
  return render(request, 'experiences/index.html', {
    'experiences': experiences,
    'experiences_form': experiences_form
  })

class ExperienceCreate(CreateView):
  model = Experience
  fields = '__all__'

class ExperienceUpdate(UpdateView):
  model = Experience
  fields = '__all__'

class ExperienceDelete(DeleteView):
  model = Experience
  success_url = '/experiences/'