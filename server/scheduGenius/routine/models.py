from django.db import models

class Faculty(models.Model):
    faculty_id = models.AutoField(primary_key=True)
    faculty_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=True, blank=True, default='not provided')  # Optional field with default value
    contact = models.CharField(max_length=15, null=True, blank=True, default='not provided') 

    def __str__(self):
        return self.faculty_name


class Course(models.Model):
    COURSE_TYPE_CHOICES = [
        ('theoretical', 'Theoretical'),
        ('sessional', 'Sessional'),
    ]
    course_id = models.AutoField(primary_key=True)
    course_no = models.CharField(max_length=20, unique=True)
    course_title = models.CharField(max_length=200)
    credit = models.IntegerField()
    course_type = models.CharField(
        max_length=15,
        choices=COURSE_TYPE_CHOICES,
        default='theoretical'
    )

    def __str__(self):
        return f"{self.course_no} - {self.course_title} ({self.get_course_type_display()})"


class FacultyCourse(models.Model):
    id = models.AutoField(primary_key=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.faculty} - {self.course}"


class Classroom(models.Model):
    id = models.AutoField(primary_key=True)
    classroom_no = models.CharField(max_length=20, unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return self.classroom_no


class Period(models.Model):
    id = models.AutoField(primary_key=True)
    period_no = models.CharField(max_length=10, default=1)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.period_no}: {self.start_time} - {self.end_time}"


class MasterRoutine(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ])

    def __str__(self):
        return f"{self.day} - {self.course} - {self.faculty} - {self.classroom}"
