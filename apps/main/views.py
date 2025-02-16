from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from apps.main.models import Settings, Products, Characteristic
from apps.main.serializer import  ProductSerializer, CharacteristicSerializer
from apps.main.pagination import ProducPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

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
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    
    search_fields = ['title','description']
    ordering_fields = ['price', 'created_app']
    ordering = ['=created_att']
    
class CharacteristicViewSet(GenericViewSet,
                    mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.RetrieveModelMixin,
                     ):
    queryset = Characteristic.objects.all()
    serializer_class = CharacteristicSerializer    
    
