from django.urls import path
from .views import DogListView, DogDetailView, BreedListView, BreedDetailView

urlpatterns = [
    path('dog/', DogListView.as_view(), name="dog-list-create"),
    path('dog/<int:pk>/', DogDetailView.as_view(), name="dog-detail"),
    path('breeds/', BreedListView.as_view(), name="breed-list-create"),
    path('breeds/<int:pk>/', BreedDetailView.as_view(), name="breed-detail")
]
