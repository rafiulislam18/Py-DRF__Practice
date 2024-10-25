from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Teacher
from .serializers import TeacherSerializer
from ..permissions.permissions import CustomIsAdminOrReadOnly


# API view to handle GET (all) request for Teacher model (is admin or read-only)
@api_view(['GET'])
@permission_classes([CustomIsAdminOrReadOnly])
def teacher_list(request):
    teachers = Teacher.objects.all()
    serializer = TeacherSerializer(teachers, many=True)
    return Response(serializer.data)
