from ast import Delete
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import EducationForm, ContactForm, ResumeForm, SkillForm, ExperienceForm, ProjectForm
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin

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

@login_required
def skills_index(request):
  # Filter skills once user model has been connected to Skill model
  skills = Skill.objects.filter(user=request.user)
  skills_form = SkillForm()
  return render(request, 'skills/index.html', {
    'skills': skills,
    'skills_form': skills_form
    })

class SkillCreate(LoginRequiredMixin, CreateView):
  model = Skill
  fields = ['name', 'type', 'description']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class SkillUpdate(LoginRequiredMixin, UpdateView):
  model = Skill
  fields = ['name', 'type', 'description']

class  SkillDelete(LoginRequiredMixin, DeleteView):
  model = Skill
  success_url = '/skills/'

class ResumeCreate(LoginRequiredMixin, CreateView):
  model = Resume
  fields = ['name', 'date']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ResumeUpdate(LoginRequiredMixin, UpdateView):
  model = Resume
  fields = ['name', 'date'] 

class ResumeDelete(LoginRequiredMixin, DeleteView):
  model = Resume  
  success_url = '/resumes/'

@login_required
def resumes_index(request):
  resumes = Resume.objects.filter(user=request.user)
  resume_form = ResumeForm()
  return render(request, 'resumes/index.html', {
    'resumes': resumes,
    'resume_form': resume_form,
    })

@login_required
def resumes_detail(request, resume_id):
  resume = Resume.objects.filter(user=request.user).get(id=resume_id)
  contacts = Contact.objects.filter(user=request.user).exclude(id__in=resume.contacts.all().values_list('id'))
  projects = Project.objects.filter(user=request.user).exclude(id__in=resume.projects.all().values_list('id'))
  experiences = Experience.objects.filter(user=request.user).exclude(id__in=resume.experiences.all().values_list('id'))
  educations = Education.objects.filter(user=request.user).exclude(id__in=resume.educations.all().values_list('id'))
  resume_form = ResumeForm()
  skills = Skill.objects.filter(user=request.user).exclude(id__in=resume.skills.all().values_list('id'))
  return render(request, 'resumes/detail.html',  {
    'resume': resume,
    'skills': skills,
    'contacts': contacts,
    'projects': projects,
    'experiences': experiences,
    'educations': educations,
    'resume_form': resume_form,
  })

@login_required
def resumes_print(request, resume_id):
  resume = Resume.objects.get(id=resume_id)
  skills = resume.skills.all()
  contacts = resume.contacts.all()
  projects = resume.projects.all()
  experiences = resume.experiences.all()
  educations = resume.educations.all()
  return render(request, 'resumes/print.html', {
    'resume': resume,
    'skills': skills,
    'contacts': contacts,
    'projects': projects,
    'experiences': experiences,
    'educations': educations,
    })  

@login_required
def assoc_skill(request, resume_id, skill_id):
  resume=Resume.objects.get(id=resume_id)
  resume.skills.add(skill_id)
  return redirect('resumes_detail', resume_id=resume_id)

@login_required
def unassoc_skill(request, resume_id, skill_id):
  Resume.objects.get(id=resume_id).skills.remove(skill_id)
  return redirect('resumes_detail', resume_id=resume_id)

@login_required
def assoc_contact(request, resume_id, contact_id):
  resume=Resume.objects.get(id=resume_id)
  resume.contacts.add(contact_id)
  return redirect('resumes_detail', resume_id=resume_id)

@login_required
def unassoc_contact(request, resume_id, contact_id):
  Resume.objects.get(id=resume_id).contacts.remove(contact_id)
  return redirect('resumes_detail', resume_id=resume_id)

@login_required
def assoc_education(request, resume_id, education_id):
  resume=Resume.objects.get(id=resume_id)
  resume.educations.add(education_id)
  return redirect('resumes_detail', resume_id=resume_id)

@login_required
def unassoc_education(request, resume_id, education_id):
  Resume.objects.get(id=resume_id).educations.remove(education_id)
  return redirect('resumes_detail', resume_id=resume_id)

@login_required
def assoc_project(request, resume_id, project_id):
  resume=Resume.objects.get(id=resume_id)
  resume.projects.add(project_id)
  return redirect('resumes_detail', resume_id=resume_id)

@login_required
def unassoc_project(request, resume_id, project_id):
  Resume.objects.get(id=resume_id).projects.remove(project_id)
  return redirect('resumes_detail', resume_id=resume_id)

@login_required
def assoc_experience(request, resume_id, experience_id):
  resume=Resume.objects.get(id=resume_id)
  resume.experiences.add(experience_id)
  return redirect('resumes_detail', resume_id=resume_id)

@login_required
def unassoc_experience(request, resume_id, experience_id):
  Resume.objects.get(id=resume_id).experiences.remove(experience_id)
  return redirect('resumes_detail', resume_id=resume_id)

@login_required
def educations_index(request):
  educations = Education.objects.filter(user=request.user)
  educations_form = EducationForm()
  return render(request, 'educations/index.html', {
    'educations': educations,
    'educations_form': educations_form
    }) 

class EducationCreate(LoginRequiredMixin, CreateView):
  model= Education
  fields= ['institution', 'graduation', 'location', 'degree', 'degree_description']
 
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class EducationUpdate(LoginRequiredMixin, UpdateView):
  model = Education
  fields= ['institution', 'graduation', 'location', 'degree', 'degree_description']

class EducationDelete(LoginRequiredMixin, DeleteView):
  model = Education
  success_url = '/educations/'

@login_required  
def contacts_index(request):
  contacts = Contact.objects.filter(user=request.user)
  contacts_form = ContactForm()
  return render(request, 'contacts/index.html', {
    'contacts': contacts,
    'contacts_form': contacts_form
  })
  
class ContactCreate(LoginRequiredMixin, CreateView):
  model = Contact
  fields = ['first_name', 'last_name', 'email', 'linkedin', 'github', 'portfolio', 'location', 'job_title']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ContactUpdate(LoginRequiredMixin, UpdateView):
  model = Contact
  fields = ['first_name', 'last_name', 'email', 'linkedin', 'github', 'portfolio', 'location', 'job_title']

class ContactDelete(LoginRequiredMixin, DeleteView):
  model = Contact
  success_url = '/contacts/'

@login_required
def experiences_index(request):
  experiences = Experience.objects.filter(user=request.user)
  experiences_form = ExperienceForm()
  return render(request, 'experiences/index.html', {
    'experiences': experiences,
    'experiences_form': experiences_form
  })

class ExperienceCreate(LoginRequiredMixin, CreateView):
  model = Experience
  fields = ['workplace', 'location', 'start_date', 'end_date', 'description']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ExperienceUpdate(LoginRequiredMixin, UpdateView):
  model = Experience
  fields = ['workplace', 'location', 'start_date', 'end_date', 'description']

class ExperienceDelete(LoginRequiredMixin, DeleteView):
  model = Experience
  success_url = '/experiences/'

@login_required
def projects_index(request):
  projects = Project.objects.filter(user=request.user)
  projects_form = ProjectForm()
  return render(request, 'projects/index.html', {
    'projects': projects,
    'projects_form': projects_form
  })

class ProjectCreate(LoginRequiredMixin, CreateView):
  model = Project
  fields = ['name', 'locations', 'date', 'technologies', 'description']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ProjectUpdate(LoginRequiredMixin, UpdateView):
  model = Project
  fields = ['name', 'locations', 'date', 'technologies', 'description']

class ProjectDelete(LoginRequiredMixin, DeleteView):
  model = Project
  success_url = '/projects/'