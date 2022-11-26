from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .models import Store, Product, Buy, Supply
from .serializers import StoreSerializer, StoreProductSerializer, ProductCreateSerializer


class StoreListView(ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class StoreDetailView(RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreProductSerializer


class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductCreateSerializer
    queryset = Product






