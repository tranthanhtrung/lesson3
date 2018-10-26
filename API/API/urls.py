from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from shop import views


router = routers.SimpleRouter(trailing_slash = False)
router.register('categories', views.CRUD_categories)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/sessions', TokenObtainPairView.as_view(), name="token_obtain_pair")
    # path('api/v1/current-sessions', TokenRefreshView.as_view(), name="token_refresh")
    path('api/v1/', include(router.urls))
#     path('api/v1/categories/:id')
#     path('api/v1/products')
#     path('api/v1/products/:id')
#     path('api/v1/orders')
#     path('api/v1/orders/:id')
#     path('api/v1/currtent-order')
#     path('api/v1/current-user')
#     path('api/v1/current-user/orders')
]
