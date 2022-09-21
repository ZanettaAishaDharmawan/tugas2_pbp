from django.test import TestCase
from django.test import Client

# Create your tests here.
# test html
class Testing(TestCase):
    def test_url_check_html(self):
        client = Client()
        response = client.get(('/mywatchlist/html/'))
        self.assertEquals(response.status_code,200)
    
    def test_url_check_xml(self):
        client = Client()
        response = client.get(('/mywatchlist/xml/'))
        self.assertEquals(response.status_code,200)
    
    def test_url_check_json(self):
        client = Client()
        response = client.get(('/mywatchlist/json/'))
        self.assertEquals(response.status_code,200)