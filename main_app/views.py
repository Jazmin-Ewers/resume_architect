from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import ResumeForm, EducationForm, ContactForm

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
      return redirect('home')
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
  return render(request, 'skills/index.html', {'skills': skills})


class SkillCreate(CreateView):
  model = Skill
  fields = '__all__'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class SkillUpdate(UpdateView):
  model = Skill
  fields = '__all__'

class ResumeCreate(CreateView):
  model = Resume
  fields = '__all__'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

def resumes_detail(request, resume_id):
  resume = Resume.objects.all()
  # skills = Resume.objects.get()
  resume_form = ResumeForm()
  return render(request, 'resumes/detail.html',  {
    'resume': resume,
    'resume_form': resume_form,
    # 'skills': skills
    })

def assoc_skill(request, resume_id, skill_id):
  resume=Resume.objects.get(id=resume_id)
  resume.skills.add(skill_id)
  return redirect('resumes_detail', resume_id=resume_id)

def educations_index(request):
  educations = Education.objects.all()
  return render(request, 'educations/index.html', {'educations': educations}) 

class EducationCreate(CreateView):
  model= Education
  fields= '__all__'
  
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

