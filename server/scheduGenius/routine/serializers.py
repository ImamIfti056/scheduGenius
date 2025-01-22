from rest_framework import serializers
from .models import Faculty, Course, FacultyCourse, Classroom, Period, MasterRoutine

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class FacultyCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyCourse
        fields = '__all__'

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'

class PeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Period
        fields = '__all__'

# class MasterRoutineSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MasterRoutine
#         fields = '__all__'

class MasterRoutineSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.course_title')
    course_no = serializers.CharField(source='course.course_no')
    faculty = serializers.CharField(source='faculty.short_name')
    classroom = serializers.CharField(source='classroom.classroom_no')
    period = serializers.SerializerMethodField()
    year = serializers.SerializerMethodField()
    
    class Meta:
        model = MasterRoutine
        fields = ['id', 'day', 'course_title', 'course_no', 'faculty', 'classroom', 'period', 'year']
    
    def get_period(self, obj):
        # Return period details: period_no, start_time, end_time
        return {
            "period_no": obj.period.period_no,
            "start_time": obj.period.start_time,
            "end_time": obj.period.end_time
        }
    
    def get_year(self, obj):
        try:
            course_no = obj.course.course_no
            number_part = ''.join(filter(str.isdigit, course_no))
            if number_part and len(number_part) >= 1:
                return int(number_part[0])
        except (AttributeError, ValueError, TypeError):
            return None
        return None
        