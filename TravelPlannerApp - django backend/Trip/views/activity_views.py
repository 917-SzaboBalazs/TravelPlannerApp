from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from Trip.models.activity import Activity
from Trip.models.trip import Trip
from Trip.serializers.activity_serializers import ActivitySerializer


class ListCreateActivityView(ListCreateAPIView):
    serializer_class = ActivitySerializer

    def get_queryset(self):
        queryset = Activity.objects.all()
        name_starts_with = self.request.query_params.get('name_starts_with')
        length = self.request.query_params.get('length')

        if name_starts_with is not None:
            queryset = queryset.filter(name__istartswith=name_starts_with)

        queryset = queryset.order_by("-id")

        if length is not None:
            queryset = queryset[:int(length)]

        return queryset


class RetrieveUpdateDestroyActivityView(RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


"""
class ListAddActivityView(APIView):

    def get(self, request, *args, **kwargs):
        trip_id = self.kwargs.get('pk')

        try:
            queryset = Trip.objects.get(id=trip_id).activities.values()
            serializer = ActivitySerializer(queryset, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Trip.DoesNotExist as dne:
            return Response(data={"detail": str(dne)}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        trip_id = self.kwargs.get('pk')

        try:
            activity = Activity.objects.get(id=request.data['activity_id'])

            Trip.objects.get(id=trip_id).activities.add(activity.id)
            serializer = ActivitySerializer(activity)

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except (Trip.DoesNotExist, Activity.DoesNotExist) as dne:
            return Response(data={"detail": str(dne)}, status=status.HTTP_404_NOT_FOUND)


class RemoveActivityFromTripView(APIView):

    def delete(self, request, *args, **kwargs):
        trip_id = self.kwargs.get('pk')
        activity_id = self.kwargs.get('act_id')

        try:
            Trip.objects.get(id=trip_id).activities.remove(Activity.objects.get(id=activity_id))

            return Response(status=status.HTTP_204_NO_CONTENT)

        except Trip.DoesNotExist as dne:
            return Response(data={"detail": str(dne)}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, *args, **kwargs):
        trip_id = self.kwargs.get('pk')
        activity_id = self.kwargs.get('act_id')

        try:
            instance = Trip.objects.get(id=trip_id).activities.get(id=activity_id)
            serializer = ActivitySerializer(instance=instance)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        except (Trip.DoesNotExist, Activity.DoesNotExist) as dne:
            return Response(data={"detail": str(dne)}, status=status.HTTP_404_NOT_FOUND)
"""
