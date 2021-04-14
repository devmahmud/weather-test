from django.test import TestCase
from SearchResults.models import TravelPlan


class SearchResultsTests(TestCase):
    """
    Test class for Search Results
    """

    def setUp(self):
        self.origin = 'MAN'
        self.destination = 'OPO'
        self.travelDate = "2021-10-04"

    def test_travelplan_display(self):
        """
        Test travelpan display result
        """

        response = self.client.get(
            f"/resultspage/?origin={self.origin}&destination={self.destination}&travelDate={self.travelDate}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'SearchResults.html')

        self.assertCountEqual(response.context['dbData'], TravelPlan.objects.filter(
            origin=self.origin, destination=self.destination))

        self.assertEqual(response.context['origin'], self.origin)
        self.assertEqual(response.context['destination'], self.destination)

    def test_travelplan_model(self):
        """
        Test TravelPlan model
        """
        obj = TravelPlan.objects.create(
            origin=self.origin, destination=self.destination, price=200, travelOrigins=["orgin1", "origin2"],
            travelDestination=['destination1', 'destination2']
        )
        self.assertIsNotNone(obj.id)
        self.assertEqual(obj.origin, self.origin)
        self.assertEqual(obj.destination, self.destination)
        self.assertEqual(obj.price, 200)
        self.assertEqual(obj.travelOrigins, ["orgin1", "origin2"])
        self.assertEqual(obj.travelDestination, [
                         'destination1', 'destination2'])
