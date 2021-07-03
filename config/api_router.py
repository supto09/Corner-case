from django.conf import settings
from django.urls import include, path
from django.conf.urls import url

from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Corner Case API",
        default_version='v1',
        description="Api description for Corner Case",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="supto09apee@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

app_name = "api"
urlpatterns = router.urls

urlpatterns += [
    path("users/", include("corner_case.users.api.urls")),
]

# API Doc
urlpatterns += [
    url(r'^apidoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^apidoc/swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
