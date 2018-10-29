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
router.register('products', views.CRUD_products)
router.register('orders', views.CRUD_orders)
router.register('current_orders', views.CRUD_orders)
router.register('current_user', views.CRUD_orders)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/session', TokenObtainPairView.as_view()),
    path('api/v1/', include(router.urls)),
]
