from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Faculty, Course, FacultyCourse, Classroom, Period, MasterRoutine
from .serializers import FacultySerializer, CourseSerializer, FacultyCourseSerializer, ClassroomSerializer, PeriodSerializer, MasterRoutineSerializer

class FacultyViewSet(ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# class MasterRoutineViewSet(ModelViewSet):
#     queryset = MasterRoutine.objects.all()
#     serializer_class = MasterRoutineSerializer

class MasterRoutineViewSet(APIView):
    def get(self, request, *args, **kwargs):
        routines = MasterRoutine.objects.select_related(
            'course', 'faculty', 'classroom', 'period'
        )
        
        # Serialize the data using the MasterRoutineSerializer
        serializer = MasterRoutineSerializer(routines, many=True)
        
        # Return the serialized data as a JSON response
        return Response({"routines": serializer.data}, status=status.HTTP_200_OK)


# def routine_view(request):
#     # Query the MasterRoutine table with select_related to join related tables
#     routines = MasterRoutine.objects.select_related(
#         'course',  # Joins the course table
#         'faculty',  # Joins the faculty table
#         'classroom',  # Joins the classroom table
#         'period'  # Joins the period table
#     )
    
#     # Prepare data for the frontend
#     routine_data = []
#     for routine in routines:
#         routine_data.append({
#             "day": routine.day,
#             "course": {
#                 "course_no": routine.course.course_no,
#                 "course_title": routine.course.course_title
#             },
#             "faculty": {
#                 "faculty_name": routine.faculty.faculty_name
#             },
#             "classroom": {
#                 "classroom_no": routine.classroom.classroom_no
#             },
#             "period": {
#                 "start_time": routine.period.start_time,
#                 "end_time": routine.period.end_time
#             }
#         })
    
#     # Return the data as a JSON response
#     return JsonResponse({"routines": routine_data})