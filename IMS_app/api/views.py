from os import stat
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from IMS_app.models import Intern,Supervisor,Attendence,Assign_task,Task_for_intern
from IMS_app.api.serializers import InternListSerializer,SupervisorListSerializer,AttendenceListSerializer,TaskAssignedSerializer,TaskForInternSerializer
from rest_framework import status
from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated



# Model viewsets for Intern list and single instance of intern 
class InternViewSet(viewsets.ModelViewSet):
    queryset = Intern.objects.all()
    serializer_class=InternListSerializer
    # permission_classes = [IsAuthenticated]

    
    
class TaskForInternViewSet(viewsets.ModelViewSet):
    queryset = Task_for_intern.objects.all()
    serializer_class=TaskForInternSerializer
 

#Class Based view for  Attendence list

class AttendenceListAV(APIView):
    def get(self,request):
        attendence=Attendence.objects.all()
        serializer=AttendenceListSerializer(attendence,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=AttendenceListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

#Class Based view for  individual Attendence

class AttendenceDetilsAV(APIView):
    def get(self,request,pk):
        try:
            attendence=Attendence.objects.get(pk=pk)
        except Attendence.DoesNotExist:
            return Response({'error': 'not found'},status=status.HTTP_404_NOT_FOUND)
        serializer =AttendenceListSerializer(attendence)
        return Response(serializer.data)
    
    def put(self,request,pk):
        attendence=Attendence.objects.get(pk=pk)
        serializer=AttendenceListSerializer(attendence, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        attendence=Attendence.objects.get(pk=pk)
        attendence.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)   

#Class Based view for  Attendence list

class TaskListAV(APIView):
    def get(self,request):
        task=Assign_task.objects.all()
        serializer=TaskAssignedSerializer(task,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=TaskAssignedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

#Class Based view for  individual Task

class TaskDetilsAV(APIView):
    def get(self,request,pk):
        try:
            task=Assign_task.objects.get(pk=pk)
        except Assign_task.DoesNotExist:
            return Response({'error': 'not found'},status=status.HTTP_404_NOT_FOUND)
        serializer =TaskAssignedSerializer(task)
        return Response(serializer.data)
    
    def put(self,request,pk):
        task=Assign_task.objects.get(pk=pk)
        serializer=TaskAssignedSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        task=Assign_task.objects.get(pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  


#function based view for Supervisor lists
@api_view(['GET','POST',])
def supervisor_list(request):
    
    if request.method =='GET':
        supervisor = Supervisor.objects.all()
        serializer = SupervisorListSerializer(supervisor, many =True) #we defined may-true becaues as the serializer access multiple objects we have to write it 
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer = SupervisorListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

#Function Based View for individual Supervisor 
@api_view(['GET','PUT','DELETE'])
def supervisor_details(request, pk):
    if  request.method=='GET':
        try:
            supervisor=Supervisor.objects.get(pk=pk)
        except Supervisor.DoesNotExist:
            return Response({'Error': 'Supervisor not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer=SupervisorListSerializer(supervisor)
        return Response(serializer.data)
    
    if request.method=='PUT':
        supervisor=Supervisor.objects.get(pk=pk)
        serializer=SupervisorListSerializer(supervisor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    if request.method=='DELETE':
        supervisor=Supervisor.objects.get(pk=pk)
        supervisor.delete()
        return Response({'Succefully removerd '},status=status.HTTP_204_NO_CONTENT)
    
    
    


