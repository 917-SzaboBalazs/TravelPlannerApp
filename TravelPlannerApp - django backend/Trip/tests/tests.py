from rest_framework.test import APITestCase

from Trip.models.trip import Trip
from Trip.models.activity import Activity


class TestAverageDurationOfTrips(APITestCase):
    url = "/reports/avg_duration_of_trips_in_days/"

    def setUp(self):
        Trip.objects.create(name="trip1", start_date="2023-03-23", end_date="2023-03-25")
        Trip.objects.create(name="trip2", start_date="2023-03-23", end_date="2023-03-30")
        Trip.objects.create(name="trip3", start_date="2023-04-25", end_date="2023-04-30")
        Trip.objects.create(name="trip4", start_date="2023-04-25", end_date="2023-05-02")
        Trip.objects.create(name="trip5", start_date="2023-04-25", end_date="2023-05-25")

    def test_get_result_all_data_are_not_null(self):
        response = self.client.get(self.url)
        result = response.json()

        self.assertEqual(result["number_of_trips"], 5)
        self.assertAlmostEqual(result["average_duration"], 10.2)

    def test_get_result_with_null_fields(self):
        Trip.objects.create(name="trip6")
        Trip.objects.create(name="trip7", start_date="2023-04-25")
        Trip.objects.create(name="trip8", end_date="2023-05-25")

        response = self.client.get(self.url)
        result = response.json()

        self.assertEqual(result["number_of_trips"], 5)
        self.assertAlmostEqual(result["average_duration"], 10.2)

    def test_empty_set(self):
        Trip.objects.all().delete()

        response = self.client.get(self.url)
        result = response.json()

        self.assertEqual(result["message"], "Number of trips with start_data and end_data specified must be greater "
                                            "than 0")


class TestTotalPriceOfActivitiesOfSpecificTrip(APITestCase):
    url = "/reports/trips_total_price_of_activities/"

    def setUp(self):
        my_activity1 = Activity.objects.create(name="activity1", price=10)
        my_activity2 = Activity.objects.create(name="activity2", price=15)
        my_activity3 = Activity.objects.create(name="activity3", price=20)
        my_activity4 = Activity.objects.create(name="activity4", price=55)

        my_trip1 = Trip.objects.create(name="trip1")
        my_trip1.activities.add(my_activity1)
        my_trip1.activities.add(my_activity2)
        my_trip1.activities.add(my_activity3)

        my_trip2 = Trip.objects.create(name="trip2")
        my_trip2.activities.add(my_activity3)
        my_trip2.activities.add(my_activity4)

    def test_get_total_price_no_null_prices(self):
        response = self.client.get(self.url)
        result = response.json()

        trip1 = result[1]
        trip2 = result[0]

        self.assertEqual(trip1["name"], "trip1")
        self.assertAlmostEqual(trip1["total_price"], 45.)

        self.assertEqual(trip2["name"], "trip2")
        self.assertAlmostEqual(trip2["total_price"], 75.)

    def test_get_total_price_null_priceS(self):
        my_empty_price_activity = Activity.objects.create(name="empty_activity")

        my_trip1 = Trip.objects.get(name="trip1")
        my_trip1.activities.add(my_empty_price_activity)

        response = self.client.get(self.url)
        result = response.json()

        trip1 = result[1]
        trip2 = result[0]

        self.assertEqual(trip1["name"], "trip1")
        self.assertAlmostEqual(trip1["total_price"], 45.)

        self.assertEqual(trip2["name"], "trip2")
        self.assertAlmostEqual(trip2["total_price"], 75.)
