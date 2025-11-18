from django.urls import path
from .views import RestaurantListCreateView, RestaurantRetrieveUpdateDestroyView

urlpatterns = [
    path('', RestaurantListCreateView.as_view()),
    path('<int:pk>/', RestaurantRetrieveUpdateDestroyView.as_view()),
]

