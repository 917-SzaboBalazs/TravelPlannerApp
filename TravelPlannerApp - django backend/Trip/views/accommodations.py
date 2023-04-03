from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from Trip.models.accommodations import Accommodation, AccommodationType
from Trip.models.trips import Trip
from Trip.serializers import AccommodationSerializer


class ListCreateAccommodationView(ListCreateAPIView):
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer


class RetrieveUpdateDestroyAccommodationView(RetrieveUpdateDestroyAPIView):
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer


class ListAddAccommodationView(APIView):

    def get(self, request, *args, **kwargs):
        trip_id = self.kwargs.get('pk')

        try:
            queryset = Trip.objects.get(id=trip_id).accommodations.values()

            for query in queryset:
                query['type'] = AccommodationType.objects.get(id=query['type_id'])
                del query['type_id']

            serializer = AccommodationSerializer(queryset, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Trip.DoesNotExist as dne:
            return Response(data={"detail": str(dne)}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        trip_id = self.kwargs.get('pk')

        try:
            accommodation = Accommodation.objects.get(id=request.data['accommodation_id'])

            Trip.objects.get(id=trip_id).accommodations.add(accommodation.id)
            serializer = AccommodationSerializer(accommodation)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except (Trip.DoesNotExist, Accommodation.DoesNotExist) as dne:
            return Response(data={"detail": str(dne)}, status=status.HTTP_404_NOT_FOUND)


class RemoveAccommodationFromTripView(APIView):

    def delete(self, request, *args, **kwargs):
        trip_id = self.kwargs.get('pk')
        accommodation_id = self.kwargs.get('acc_id')

        try:
            Trip.objects.get(id=trip_id).accommodations.remove(Accommodation.objects.get(id=accommodation_id))

            return Response(status=status.HTTP_204_NO_CONTENT)

        except Trip.DoesNotExist as dne:
            return Response(data={"detail": str(dne)}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, *arg, **kwargs):
        trip_id = self.kwargs.get('pk')
        accommodation_id = self.kwargs.get('acc_id')

        try:
            instance = Trip.objects.get(id=trip_id).accommodations.get(id=accommodation_id)
            serializer = AccommodationSerializer(instance=instance)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        except (Trip.DoesNotExist, Accommodation.DoesNotExist) as dne:
            return Response(data={"detail": str(dne)}, status=status.HTTP_404_NOT_FOUND)
