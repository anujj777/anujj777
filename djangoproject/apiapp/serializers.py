from rest_framework import serializers
from .models import Teacher
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=['id','name','roll','city']  # or '__all__'