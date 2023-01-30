from django.urls import path
from django.urls import include
from car.views import BrandView
from car.views import BrandDetail

urlpatterns = [
    path('api/v1/brand/', BrandView.as_view()),
    path('api/v1/brand/<int:pk>/', BrandDetail.as_view({"get":"list"})),
]