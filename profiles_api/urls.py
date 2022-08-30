from django.urls import path, include
from profiles_api import views
from rest_framework .routers import DefaultRouter

router = DefaultRouter()

router.register('detail-viewset', views.DetailViewSet, base_name = 'detail-viewset')
router.register('profile', views.UserProfileViewSet)


urlpatterns = [
    path('detail/', views.Detail.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]