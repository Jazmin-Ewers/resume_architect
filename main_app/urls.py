from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup/', views.signup, name='signup'),
  
  # Skills 

  path('skills/create/', views.SkillCreate.as_view(), name='skills_create'),
  path('skills/', views.skills_index, name='skills_index'),
  path('skills/<int:pk>/update/', views.SkillUpdate.as_view(), name='skills_update'),
  # path('skills/<int:pk>/delete/', views.SkillUpdate.as_view(), name='skills_update'),
  
  #Resume paths

  path('resumes/', views.resumes_index, name='resumes_index'),
  path('resumes/create/', views.ResumeCreate.as_view(), name='resumes_create'),
  path('resumes/<int:resume_id>/', views.resumes_detail, name='resumes_detail'),
  path('resumes/<int:resume_id>/assoc_skill/<int:skill_id>/', views.assoc_skill, name='assoc_skill'),
  
  #Education

  path('educations/', views.educations_index, name='educations_index'),
  path('educations/create/', views.EducationCreate.as_view(), name='educations_create'),

  # Contact Paths

  path('contacts/', views.contacts_index, name='contacts_index'),
  # path('contacts/create/', views.contacts_create, name='contacts_create'),
  path('contacts/create/', views.ContactCreate.as_view(), name='contacts_create'),
  path('contacts/<int:pk>/update/', views.ContactUpdate.as_view(), name='contacts_update'),
  path('contacts/<int:pk>/delete/', views.ContactDelete.as_view(), name='contacts_delete'),
]