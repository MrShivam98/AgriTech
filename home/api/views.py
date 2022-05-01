from home.api.serializers import TechnologySerializers
from home.api.serializers import ContactSerializers
from home.api.serializers import ServiceSerializers
from home.models import technology
from home.models import driver
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


class TechnologyViewSet(viewsets.ViewSet):

    def list(self, request):
        tech = technology.objects.all()
        serializer = TechnologySerializers(tech, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ContactViewSet(viewsets.ViewSet):

    def create(self, request):
        serializer = ContactSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceViewSet(viewsets.ViewSet):

    def create(self, request):
        try:
            if len(request.data) != 0:
                if int(request.data['weight']) <= 8:
                    driveby = driver.objects.filter(vehicle='BajajTempo').first()
                elif int(request.data['weight']) <= 15:
                    driveby = driver.objects.filter(vehicle='Tractor').first()
                elif int(request.data['weight']) >= 25:
                    driveby = driver.objects.filter(vehicle='Truck').first()
                request.data['driveby'] = driveby.email
            request.data['user'] = request.user.id
            serializer = ServiceSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Data Created'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)