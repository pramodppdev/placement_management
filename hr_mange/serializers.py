from rest_framework import serializers
from .models import Batch, Branch, Student, Staff, Certi_Skills, Projects, Achievements, Academic_Per

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

class Certi_SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certi_Skills
        fields = '__all__'

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class AchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievements
        fields = '__all__'

class Academic_PerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academic_Per
        fields = '__all__'

