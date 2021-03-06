from django.db import models
from django.urls import reverse
from datetime import date, datetime
from django.contrib.auth.models import User

# Create your models here.

TYPES = (
  ('L', 'Language'),
  ('F', 'Framework'),
  ('D', 'Database'),
)

DEGREES =  (
  ('BA', 'Bachelors of Arts'),
  ('BS', 'Bachelors of Science'),
  ('MA', 'Masters of Arts'),
  ('MS', 'Masters of Science'),
  ('CC', 'Certificate of Completion'),
  ('PH', 'PHD'),
  ('OT', 'Other')
)

class Contact(models.Model):
  first_name = models.CharField(max_length= 200)
  last_name = models.CharField(max_length= 200)
  email = models.EmailField(max_length= 255)
  linkedin = models.URLField(max_length= 200)
  github =  models.URLField(max_length= 200)
  portfolio = models.URLField(max_length= 200)
  location = models.CharField(max_length= 200)
  job_title = models.CharField(max_length= 200)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def get_absolute_url(self):
      return reverse('contacts_index')

class Skill(models.Model):
  name = models.CharField(max_length= 200)
  type = models.CharField(
      max_length = 1,
      choices = TYPES,
      default = TYPES[0][0]) 
  description = models.TextField(max_length= 500)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
      return f"{self.get_type_display()}, {self.name} {self.description}"    

  def get_absolute_url(self):
      return reverse('skills_index')

class Experience(models.Model):
  workplace = models.CharField(max_length=200)
  location = models.CharField(max_length=200)
  start_date = models.DateField('Start Date')
  end_date = models.DateField('End Date')
  description = models.TextField(max_length = 2000)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
      return self.workplace
  
  def get_absolute_url(self):
      return reverse('experiences_index')

class Education(models.Model):
  institution = models.CharField(max_length=200)
  graduation = models.DateField('Graduation Date')         
  location = models.CharField(max_length=200)
  degree = models.CharField(
      choices=DEGREES,
      default=DEGREES[6][0],
      max_length=2
  )
  degree_description = models.CharField(max_length= 300)
  user = models.ForeignKey(User, on_delete=models.CASCADE) 

  def __str__(self):
      return self.get_degree_display()

  def get_absolute_url(self):
      return reverse('educations_index')      

class Project(models.Model):
  name = models.CharField(max_length= 200)
  locations = models.CharField(max_length= 200)
  date = models.DateField('Project Date')
  technologies = models.TextField(max_length = 800)
  description = models.TextField(max_length = 2000)
  user = models.ForeignKey(User, on_delete=models.CASCADE) 

  def __str__(self):
      return self.name

  def get_absolute_url(self):
      return reverse('projects_index')    

class Resume(models.Model):
  name = models.CharField(max_length=200)
  date = models.DateField(default=datetime.now())
  contacts = models.ManyToManyField(Contact)
  skills = models.ManyToManyField(Skill)
  projects = models.ManyToManyField(Project)
  experiences = models.ManyToManyField(Experience)
  educations = models.ManyToManyField(Education)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.name  

  def get_absolute_url(self):
    return reverse('resumes_index')  