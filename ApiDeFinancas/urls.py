from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from financas.views import UserViewSet, FinanceViewSet, ListFinanceToUser

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('financas', FinanceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('user/<int:pk>/financas', ListFinanceToUser.as_view())
]
