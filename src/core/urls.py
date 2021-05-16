from django.urls import path, include

from core.views import StudentListAPIView

student_api_patterns = [
    path('', StudentListAPIView.as_view()),
]

urlpatterns = [
    path('students/', include(student_api_patterns))
]
