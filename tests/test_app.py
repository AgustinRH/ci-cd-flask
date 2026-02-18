import unittest
from src.app import app

class FlaskTest(unittest.TestCase):

    # Test 1: Comprobar que la web carga correctamente
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)

    # Test 2: Comprobar que el contenido es correcto
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertIn(b'Hello World', response.data)

    # Test 3: Comprobar que una página que no existe da error 404
    def test_404(self):
        tester = app.test_client(self)
        response = tester.get('/no-existe')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()