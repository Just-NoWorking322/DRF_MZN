from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from apps.main.models import Settings, Products, Characteristic
from apps.main.serializer import  ProductSerializer, CharacteristicSerializer


from apps.main.pagination import ProducPagination

class ProductMixins(GenericViewSet,
                    mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.RetrieveModelMixin,
                     ):
   
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProducPagination

class CharacteristicViewSet(GenericViewSet,
                    mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.RetrieveModelMixin,
                     ):
    queryset = Characteristic.objects.all()
    serializer_class = CharacteristicSerializer    
    
