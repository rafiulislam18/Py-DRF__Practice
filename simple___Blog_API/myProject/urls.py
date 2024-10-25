"""
URL configuration for myProject project.

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

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# Configure Swagger/OpenAPI schema view for the simple Blog API documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Blog API (Simple)",
        default_version='v1'
    ),
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),

    # Configure URL for 'blog_api_simple' app
    path('', include(('blog_api_simple.urls'))),

    # Configure URL for Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
]
