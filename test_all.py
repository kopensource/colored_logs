import unittest

from colored_logs.models.color import Color

class ColorTestCase(unittest.TestCase):
    def test_init_hex(self):
        self.assertIsNotNone(Color.fromHex('ffffff'))
        self.assertRaises(Exception, Color.fromHex, 'fffffg')

    def test_init_rgb(self):
        self.assertIsNotNone(Color(0, 0, 0))
        self.assertRaises(Exception, Color.__init__, -5, 0, 0)


# import time
# from colored_logs.logger import Logger

# class LogTestCase(unittest.TestCase):
#     def test_logs(self):
#         try:
#             log = Logger(ID='Test-id-1')

#             log.info('This is an info log')
#             log.success('This is a success log')
#             log.warning('This is a warning log')
#             log.error('This is an error log')
#             log.fail('This is a fail log')
#             log.critical('This is a critical log')
#             log.subtle('This is a subtle log')

#             log.start_process('This will take a while')
#             time.sleep(1)
#             log.stop_process()
#         except Exception as e:
#             self.fail('Failed main test with error: ' + repr(e))

if __name__ == '__main__':
    unittest.main()