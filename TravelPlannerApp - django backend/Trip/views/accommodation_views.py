from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from Trip.models.accommodation import Accommodation, AccommodationType
from Trip.models.trip import Trip
from Trip.serializers.accommodation_serializers import AccommodationSerializer


class ListCreateAccommodationView(ListCreateAPIView):
    serializer_class = AccommodationSerializer

    def get_queryset(self):
        queryset = Accommodation.objects.all()
        name_starts_with = self.request.query_params.get('name_starts_with')
        length = self.request.query_params.get('length')

        if name_starts_with is not None:
            queryset = queryset.filter(name__istartswith=name_starts_with)

        queryset = queryset.order_by("-id")

        if length is not None:
            queryset = queryset[:int(length)]

        return queryset

    def get_serializer_context(self):
        return {
            "depth": 1 if self.request.method == "GET" else 0,
        }


class RetrieveUpdateDestroyAccommodationView(RetrieveUpdateDestroyAPIView):
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer

    def get_serializer_context(self):
        return {
            "depth": 1 if self.request.method == "GET" else 0,
        }


"""class ListAddAccommodationView(APIView):

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
"""
