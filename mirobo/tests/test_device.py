
__author__ = 'szmania'

import unittest
from mirobo import device

class Test_DeviceInfo(unittest.TestCase):
    data = ['model': '']

    def setUp(self):
        self.cls = device()

    def test_netif(self):
        self.assert



if __name__ == '__main__':
    unittest.main()
