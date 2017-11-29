import unittest
import app


class TestApp(unittest.TestCase):


    def test_app(self):
        result = app.hello()
        self.assertEqual(result, "hello world")

if __name__ == '__main__':
    unittest.main()
