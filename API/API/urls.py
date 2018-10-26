from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from shop import views


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.SimpleRouter(trailing_slash = False)
router.register('categories', views.CRUD_categories)
router.register('products', views.CRUD_products)
router.register('orders', views.CRUD_orders)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/login', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/v1/logout', TokenRefreshView.as_view(), name="token_refresh"),
    path('api/v1/', include(router.urls)),

#     path('api/v1/orders')
#     path('api/v1/orders/:id')
#     path('api/v1/currtent-order')
#     path('api/v1/current-user')
#     path('api/v1/current-user/orders')
]
