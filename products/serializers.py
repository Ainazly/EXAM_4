from rest_framework.exceptions import NotFound
from rest_framework import serializers
from .models import Store, Product, Buy, Supply


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"


class StoresProductSerializer(serializers.ModelSerializer):
    store = serializers.CharField(source="store.title")

    class Meta:
        model = Store
        fields = "__all__"

        def get(self, request, format=None):
            serializer = StoreSerializer(Product.objects.all(), many=True)


class StoreProductSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    def get_products(self, obj):
        return StoresProductSerializer(obj.products.all(), many=True).data

    class Meta:
        model = Product
        fields = ('id', 'title', 'products')


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'price')
