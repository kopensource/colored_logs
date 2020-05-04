from colored_logs.models.color import Color

import unittest

class ColorTestCase(unittest.TestCase):
    def test_init_hex(self):
        self.assertIsNotNone(Color.fromHex('ffffff'))
        self.assertRaises(Exception, Color.fromHex, 'fffffg')

    def test_init_rgb(self):
        self.assertIsNotNone(Color(0, 0, 0))
        self.assertRaises(Exception, Color.__init__, -5, 0, 0)

if __name__ == '__main__':
    unittest.main()