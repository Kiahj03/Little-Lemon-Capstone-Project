from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from .views import MenuItemView, SingleMenuItemView

urlpatterns = [
    path('', views.index, name='index'),
    path('api-token-auth/', obtain_auth_token),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view()),
]