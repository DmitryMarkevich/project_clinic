import drf_yasg.generators
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Clinic', default_version='v1', description='Example test description',
        license=openapi.License(name='BSD License'),
        contact=openapi.Contact(email='markevich3214@tut.by')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    generator_class=drf_yasg.generators.OpenAPISchemaGenerator

)

urlpatterns = [
    path("swagger(?P<format>\.json|\.yaml)", schema_view.without_ui(cache_timeout=8), name="schema-json"),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name="schema-swagger-ui"),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name="schema-redoc")
]
