from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  
  # Skills Paths
  path('skills/create/', views.SkillCreate.as_view(), name='skills_create'),
  path('skills/', views.skills_index, name='skills_index'),
  path('skills/<int:pk>/update/', views.SkillUpdate.as_view(), name='skills_update'),
  path('skills/<int:pk>/delete/', views.SkillDelete.as_view(), name='skills_delete'),
  
  #Resume Paths
  path('resumes/', views.resumes_index, name='resumes_index'),
  path('resumes/create/', views.ResumeCreate.as_view(), name='resumes_create'),
  path('resumes/<int:resume_id>/', views.resumes_detail, name='resumes_detail'),
  path('resumes/<int:resume_id>/print', views.resumes_print, name='resumes_print'),
  path('resumes/<int:resume_id>/assoc_skill/<int:skill_id>/', views.assoc_skill, name='assoc_skill'),
  path('resumes/<int:resume_id>/unassoc_skill/<int:skill_id>/', views.unassoc_skill, name='unassoc_skill'),
  path('resumes/<int:resume_id>/assoc_contact/<int:contact_id>/', views.assoc_contact, name='assoc_contact'),
  path('resumes/<int:resume_id>/unassoc_contact/<int:contact_id>/', views.unassoc_contact, name='unassoc_contact'),
  path('resumes/<int:resume_id>/assoc_education/<int:education_id>/', views.assoc_education, name='assoc_education'),
  path('resumes/<int:resume_id>/unassoc_education/<int:education_id>/', views.unassoc_education, name='unassoc_education'),
  path('resumes/<int:resume_id>/assoc_project/<int:project_id>/', views.assoc_project, name='assoc_project'),
  path('resumes/<int:resume_id>/unassoc_project/<int:project_id>/', views.unassoc_project, name='unassoc_project'),
  path('resumes/<int:resume_id>/assoc_experience/<int:experience_id>/', views.assoc_experience, name='assoc_experience'),
  path('resumes/<int:resume_id>/unassoc_experience/<int:experience_id>/', views.unassoc_experience, name='unassoc_experience'),

  # Education Paths
  path('educations/', views.educations_index, name='educations_index'),
  path('educations/create/', views.EducationCreate.as_view(), name='educations_create'),
  path('educations/<int:pk>/update/', views.EducationUpdate.as_view(), name='educations_update'),
  path('educations/<int:pk>/delete/', views.EducationDelete.as_view(), name='educations_delete'),
  
  # Contact Paths 
  path('contacts/', views.contacts_index, name='contacts_index'),
  path('contacts/create/', views.ContactCreate.as_view(), name='contacts_create'),
  path('contacts/<int:pk>/update/', views.ContactUpdate.as_view(), name='contacts_update'),
  path('contacts/<int:pk>/delete/', views.ContactDelete.as_view(), name='contacts_delete'),

  # Experiences Paths
  path('experiences/', views.experiences_index, name='experiences_index'),
  path('experiences/create/', views.ExperienceCreate.as_view(), name='experiences_create'),
  path('experiences/<int:pk>/update/', views.ExperienceUpdate.as_view(), name='experiences_update'),
  path('experiences/<int:pk>/delete/', views.ExperienceDelete.as_view(), name='experiences_delete'),

  # Projects Paths
  path('projects/', views.projects_index, name='projects_index'),
  path('projects/create/', views.ProjectCreate.as_view(), name='projects_create'),
  path('projects/<int:pk>/update/', views.ProjectUpdate.as_view(), name='projects_update'),
  path('projects/<int:pk>/delete/', views.ProjectDelete.as_view(), name='projects_delete'),

]