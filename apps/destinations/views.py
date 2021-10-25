from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status

from apps.users.authentication_mixins import Authentication
from .api.serializers import DestinationApiSerializer

class DestinationViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class = DestinationApiSerializer

    def get_queryset(self, pk = None):
        if pk == None:
            return self.get_serializer().Meta.model.objects.filter(activate = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(activate = True, id = pk).first()

    def list(self, request):
        product_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(product_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Destino creado correctamente', 'destino':serializer.validated_data},
                status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk = None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response({'message':'Destino actualizado correctamente','destino':product_serializer.data,}, status=status.HTTP_200_OK)
        return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk = None):
        product = self.get_queryset().filter(id = pk).first()
        if product:
            product.activate = False
            product.save()
            return Response({'message':'Producto eliminado correctamente'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un producto con esos datos'})


# Metodo con decorador @api_view, solamente para listado de destinos
'''
@api_view(['GET'])
def destination_api_view(request):
    if request.method == 'GET':
        destinations = Destination.objects.all().filter(activate = True)
        destinationsSerializer = DestinationApiSerializer(destinations, many = True)
        return Response(destinationsSerializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'message':'Error, el endpoint solo permite get'}, status=status.HTTP_400_BAD_REQUEST)
'''