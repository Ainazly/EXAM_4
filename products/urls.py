from django.urls import path
from .views import StoreListView, StoreDetailView, ProductCreateAPIView


urlpatterns = [
    path('all_store/', StoreListView.as_view()),
    path('store/<int:pk>/', StoreDetailView.as_view()),
path('create_product/', ProductCreateAPIView.as_view()),

    # path('stores/<int:id>/buy/', BuyAPIView.as_view()),
]