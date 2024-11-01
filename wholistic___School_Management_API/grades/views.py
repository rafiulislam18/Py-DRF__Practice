from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from .models import Grade
from .serializers import GradeSerializer


# Mixin-based API view for CRUD on Grade model
class GradeView(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 GenericAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
