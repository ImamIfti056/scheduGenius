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

class PeriodViewSet(ModelViewSet):
    queryset = Period.objects.all().order_by('start_time')
    serializer_class = PeriodSerializer

class ClassroomViewSet(ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer


class MasterRoutineViewSet(APIView):
    def get(self, request, *args, **kwargs):
        routines = MasterRoutine.objects.select_related(
            'course', 'faculty', 'classroom', 'period'
        )
        
        # Serialize the data using the MasterRoutineSerializer
        serializer = MasterRoutineSerializer(routines, many=True)
        
        # Return the serialized data as a JSON response
        return Response({"routines": serializer.data}, status=status.HTTP_200_OK)
