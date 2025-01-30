"""
URL configuration for scheduGenius project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from routine.views import CourseViewSet, FacultyViewSet, PeriodViewSet, ClassroomViewSet, MasterRoutineViewSet


urlpatterns = [
    path("admin/", admin.site.urls),
    # path('routine/', MasterRoutineViewSet.as_view({'get': 'list'}), name='master_routine'),
    path('routine/', MasterRoutineViewSet.as_view(), name='master_routine'),
    path('courses/', CourseViewSet.as_view({'get': 'list'}), name='courses'),
    path('faculties/', FacultyViewSet.as_view({'get': 'list'}), name='faculties'),
    path('periods/', PeriodViewSet.as_view({'get': 'list'}), name='periods'),
    path('classrooms/', ClassroomViewSet.as_view({'get': 'list'}), name='classrooms'),
]
