import unittest
from app import app

class FlaskTest(unittest.TestCase):
    def test_hello(self):
        tester = app.test_client(self)
        response = tester.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Hello, DevOps! this is in class")
    
    def test_hi(self):
        tester = app.test_client(self)
        response = tester.get('/hi')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Hi!")

if __name__ == '__main__':
    unittest.main()
