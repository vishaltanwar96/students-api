from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework import filters

from core.models import Student
from core.serializers import StudentSerializer


class StudentListAPIView(ListAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['first_name', 'date_of_admission']
