from rest_framework import mixins, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import Grade
from .serializers import GradeSerializer
from permissions.permissions import CustomIsAdminOrReadOnly

class GradeListCreateView(mixins.ListModelMixin,
                         mixins.CreateModelMixin,
                         GenericAPIView):
    """
    API view for listing and creating Grade instances.
    GET: List all grades
    POST: Create a new grade
    """
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [CustomIsAdminOrReadOnly]
    
    def get_queryset(self):
        """
        Optionally restricts the returned grades by filtering against
        query parameters in the URL.
        """
        queryset = Grade.objects.all()
        # Example filter by grade title
        title = self.request.query_params.get('title', None)
        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        return queryset

    def get(self, request, *args, **kwargs):
        """List all grades"""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Create a new grade"""
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """Override create method to add custom response"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                'status': 'success',
                'message': 'Grade created successfully',
                'data': serializer.data
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )

class GradeDetailView(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     GenericAPIView):
    """
    API view for retrieving, updating and deleting individual Grade instances.
    GET: Retrieve a grade
    PUT: Update a grade
    PATCH: Partially update a grade
    DELETE: Delete a grade
    """
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [CustomIsAdminOrReadOnly]
    lookup_field = 'pk'  # you can change this to another field if needed

    def get(self, request, *args, **kwargs):
        """Retrieve a grade instance"""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Update a grade instance"""
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """Partially update a grade instance"""
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Delete a grade instance"""
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {
                'status': 'success',
                'message': 'Grade deleted successfully'
            },
            status=status.HTTP_204_NO_CONTENT
        )

    def update(self, request, *args, **kwargs):
        """Override update method to add custom response"""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(
            {
                'status': 'success',
                'message': 'Grade updated successfully',
                'data': serializer.data
            }
        )