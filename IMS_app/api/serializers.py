from rest_framework import serializers
from IMS_app import models


#---Model Serializer----------------------------------------

class InternListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Intern
        fields = '__all__'

class SupervisorListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Supervisor
        fields = '__all__'

class TaskAssignedSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Assign_task
        fields = '__all__'
        
class TaskForInternSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Task_for_intern
        fields = '__all__'
        
class AttendenceListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Attendence
        fields = '__all__'

