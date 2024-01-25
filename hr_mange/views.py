from rest_framework import generics
from .models import Batch, Branch, Student, Staff, Certi_Skills, Projects, Achievements, Academic_Per
from .serializers import BatchSerializer, BranchSerializer, StudentSerializer, StaffSerializer, Certi_SkillsSerializer, ProjectsSerializer, AchievementsSerializer, Academic_PerSerializer

class BatchListCreateView(generics.ListCreateAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

class BatchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

class BranchListCreateView(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class BranchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StaffListCreateView(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class StaffDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class Certi_SkillsListCreateView(generics.ListCreateAPIView):
    queryset = Certi_Skills.objects.all()
    serializer_class = Certi_SkillsSerializer

class Certi_SkillsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certi_Skills.objects.all()
    serializer_class = Certi_SkillsSerializer

class ProjectsListCreateView(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

class ProjectsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

class AchievementsListCreateView(generics.ListCreateAPIView):
    queryset = Achievements.objects.all()
    serializer_class = AchievementsSerializer

class AchievementsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Achievements.objects.all()
    serializer_class = AchievementsSerializer

class Academic_PerListCreateView(generics.ListCreateAPIView):
    queryset = Academic_Per.objects.all()
    serializer_class = Academic_PerSerializer

class Academic_PerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Academic_Per.objects.all()
    serializer_class = Academic_PerSerializer
