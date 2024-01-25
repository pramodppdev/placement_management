from django.urls import path
from .views import (
    BatchListCreateView, BatchDetail,
    BranchListCreateView, BranchDetail,
    StudentListCreateView, StudentDetail,
    StaffListCreateView, StaffDetail,
    Certi_SkillsListCreateView, Certi_SkillsDetail,
    ProjectsListCreateView, ProjectsDetail,
    AchievementsListCreateView, AchievementsDetail,
    Academic_PerListCreateView, Academic_PerDetail,
)

urlpatterns = [
    path('batch/', BatchListCreateView.as_view(), name='batch-list-create'),
    path('batch/<int:pk>/', BatchDetail.as_view(), name='batch-detail'),

    path('branch/', BranchListCreateView.as_view(), name='branch-list-create'),
    path('branch/<int:pk>/', BranchDetail.as_view(), name='branch-detail'),

    path('student/', StudentListCreateView.as_view(), name='student-list-create'),
    path('student/<int:pk>/', StudentDetail.as_view(), name='student-detail'),

    path('staff/', StaffListCreateView.as_view(), name='staff-list-create'),
    path('staff/<int:pk>/', StaffDetail.as_view(), name='staff-detail'),

    path('certi_skills/', Certi_SkillsListCreateView.as_view(), name='certi_skills-list-create'),
    path('certi_skills/<int:pk>/', Certi_SkillsDetail.as_view(), name='certi_skills-detail'),

    path('projects/', ProjectsListCreateView.as_view(), name='projects-list-create'),
    path('projects/<int:pk>/', ProjectsDetail.as_view(), name='projects-detail'),

    path('achievements/', AchievementsListCreateView.as_view(), name='achievements-list-create'),
    path('achievements/<int:pk>/', AchievementsDetail.as_view(), name='achievements-detail'),

    path('academic_per/', Academic_PerListCreateView.as_view(), name='academic_per-list-create'),
    path('academic_per/<int:pk>/', Academic_PerDetail.as_view(), name='academic_per-detail'),
]
