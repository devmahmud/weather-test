from django.test import TestCase
from SearchResults.models import TravelPlan


class SearchResultsTests(TestCase):
    """
    Test class for Search Results
    """

    def test_travelplan_display(self):
        """
        Test travelpan display result
        """
        response = self.client.get(
            "/resultspage/?origin=DHAKA&destination=USA&travelDate=2020-10-04")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'SearchResults.html')
        self.assertIsInstance(response.context['dbData'], TravelPlan)
        self.assertEqual(response.context['origin'], 'DHAKA')
        self.assertEqual(response.context['destination'], 'USA')

    def test_travelplan_model(self):
        """
        Test TravelPlan model
        """
        obj = TravelPlan.objects.create(
            origin="CANADA", destination="AUSTRALIA", price=200, travelOrigins=["orgin1", "origin2"],
            travelDestination=['destination1', 'destination2']
        )
        self.assertEqual(obj.id, 1)
        self.assertEqual(obj.origin, 'CANADA')
        self.assertEqual(obj.destination, 'AUSTRALIA')
        self.assertEqual(obj.price, 200)
        self.assertEqual(obj.travelOrigins, ["orgin1", "origin2"])
        self.assertEqual(obj.travelDestination, [
                         'destination1', 'destination2'])
