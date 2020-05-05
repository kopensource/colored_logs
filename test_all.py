import unittest

from colored_logs.models.color import Color

class ColorTestCase(unittest.TestCase):
    def test_init_hex(self):
        self.assertIsNotNone(Color.fromHex('ffffff'))
        self.assertRaises(Exception, Color.fromHex, 'fffffg')

    def test_init_rgb(self):
        self.assertIsNotNone(Color(0, 0, 0))
        self.assertRaises(Exception, Color.__init__, -5, 0, 0)

class IntegrationTestCase(unittest.TestCase):
    def test_demo(self):
        try:
            import demo
        except Exception as e:
            self.fail('Failed main test with error: ' + repr(e))

if __name__ == '__main__':
    unittest.main()