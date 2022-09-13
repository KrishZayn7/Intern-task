from django.urls import path,include
from IMS_app.api.views import (supervisor_list,supervisor_details,AttendenceListAV,
                               AttendenceDetilsAV,TaskListAV,TaskDetilsAV,InternViewSet,TaskForInternViewSet)
from rest_framework.routers import DefaultRouter


router =DefaultRouter()
router.register('intern',InternViewSet,basename='intern')
router.register('taskforintern',TaskForInternViewSet,basename='Task for intern')


urlpatterns = [

    path('',include(router.urls)),
    
    path('supervisor/',supervisor_list,name='Supervisor-list'),
    path('supervisor/<int:pk>',supervisor_details,name='supervisor_details'),
    
    path('attendence/',AttendenceListAV.as_view(),name='attendence-list'),
    path('attendence/<int:pk>',AttendenceDetilsAV.as_view(),name='attendence-Details'),
    
    path('task/',TaskListAV.as_view(),name='task-list'),
    path('task/<int:pk>',TaskDetilsAV.as_view(),name='Task-Details'),
    

]  