# from django.conf.urls import url
# from drf_yasg.views import get_schema_view
# from rest_framework.permissions import AllowAny
# from drf_yasg import openapi

# from django.urls import include
# # app_name ="docs"
# schema_url_v1_patterns = [
#     url(r'^v1/', include('docs.urls')),
# ]
 
# schema_view_v1 = get_schema_view(
#     openapi.Info(
#         title="Bongto API",
#         default_version='v1',
#         description="안녕하세요. 봉투의 Open API 문서 페이지 입니다.",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="petepp@likelion.org"),
#         license=openapi.License(name="Bongtoo's API"),
#     ),
#     validators=['flex'], #'ssv'],
#     public=True,
#     permission_classes=(AllowAny,),
#     patterns=schema_url_v1_patterns,
# )

# urlpatterns = [
#     # url(r'^admin/', admin.site.urls),
 
#     # Auto DRF API docs
#     url(r'^swagger(?P<format>\.json|\.yaml)/v1$', schema_view_v1.without_ui(cache_timeout=0), name='schema-json'),
#     url(r'^swagger/v1/$', schema_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     url(r'^redoc/v1/$', schema_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
# ]

