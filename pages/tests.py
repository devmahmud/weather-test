from django.test import TestCase


class PagesViewTests(TestCase):
    """
    Test class for pages views
    """

    def test_open_main_page(self):
        """
        Test open_main_page view
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Travelly')
        self.assertTemplateUsed(response, 'TravellyHomePage.html')
