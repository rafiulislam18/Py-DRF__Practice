from rest_framework.permissions import BasePermission


# Custom permission to allow only the author of a blog post to edit or delete it
class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return obj.author == request.user
