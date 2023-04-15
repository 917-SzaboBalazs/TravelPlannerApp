from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from Trip.models.transportation import Transportation, TransportationType
from Trip.models.trip import Trip
from Trip.serializers.transportation_serializers import TransportationSerializer


class ListCreateTransportationView(ListCreateAPIView):
    serializer_class = TransportationSerializer

    def get_serializer_context(self):
        return {
            "depth": 1 if self.request.method == "GET" else 0,
        }
    
    def get_queryset(self):
        queryset = Transportation.objects.all()
        name_starts_with = self.request.query_params.get('name_starts_with')

        if name_starts_with is not None:
            queryset = queryset.filter(name__istartswith=name_starts_with)

        return queryset.order_by("-id")[:5]


class RetrieveUpdateDestroyTransportationView(RetrieveUpdateDestroyAPIView):
    queryset = Transportation.objects.all()
    serializer_class = TransportationSerializer

    def get_serializer_context(self):
        return {
            "depth": 1 if self.request.method == "GET" else 0,
        }


class ListAddTransportationView(APIView):

    def get(self, request, *args, **kwargs):
        trip_id = self.kwargs.get('pk')

        try:
            queryset = Trip.objects.get(id=trip_id).transportations.values()

            for query in queryset:
                query['type'] = TransportationType.objects.get(id=query['type_id'])
                del query['type_id']

            serializer = TransportationSerializer(queryset, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Trip.DoesNotExist as dne:
            return Response(data={"detail": str(dne)}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        trip_id = self.kwargs.get('pk')

        try:
            transportation = Transportation.objects.get(id=request.data['transportation_id'])

            Trip.objects.get(id=trip_id).transportations.add(transportation.id)
            serializer = TransportationSerializer(transportation)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except (Trip.DoesNotExist, Transportation.DoesNotExist) as dne:
            return Response(data={"detail": str(dne)}, status=status.HTTP_404_NOT_FOUND)


class RemoveTransportationFromTripView(APIView):

    def delete(self, request, *args, **kwargs):
        trip_id = self.kwargs.get('pk')
        transportation_id = self.kwargs.get('transport_id')

        try:
            Trip.objects.get(id=trip_id).transportations.remove(Transportation.objects.get(id=transportation_id))

            return Response(status=status.HTTP_204_NO_CONTENT)

        except Trip.DoesNotExist as dne:
            return Response(data={"detail": str(dne)}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, *args, **kwargs):
        trip_id = self.kwargs.get('pk')
        transportation_id = self.kwargs.get('transport_id')

        try:
            instance = Trip.objects.get(id=trip_id).transportations.get(id=transportation_id)
            serializer = TransportationSerializer(instance=instance)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        except (Trip.DoesNotExist, Transportation.DoesNotExist) as dne:
            return Response(data={"detail": str(dne)}, status=status.HTTP_404_NOT_FOUND)
