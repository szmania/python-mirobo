
__author__ = 'szmania'

from mirobo import Device, DeviceException

from unittest.mock import patch
from unittest import TestCase


class Mock_Value(object):
    def __init__(self):
        self.__devtype = 'devtype'
        self.__serial = 'serial'
        self.__ts = 'ts'


    @property
    def devtype(self):
        return self.__devtype

    @devtype.setter
    def devtype(self, value):
        self.__devtype = value

    @property
    def serial(self):
        return self.__serial

    @serial.setter
    def serial(self, value):
        self.__serial = value

    @property
    def ts(self):
        return self.__ts

    @ts.setter
    def ts(self, value):
        self.__ts = value

class Mock_Header(object):
    def __init__(self):
        self.__value = None

    @property
    def value(self):
        mockObj = Mock_Value()
        return mockObj

    @value.setter
    def value(self, value):
        self.__value = value

class Mock_Socket(object):

    def __init__(self):
        self.__header = None

    @property
    def header(self):
        mockObj = Mock_Header()
        return mockObj

    @header.setter
    def header(self, value):
        self.__header = value



class Test_Device(TestCase):

    def setUp(self):
        kwargs = {'ip': '192.168.0.2',
                'token': '5664326b306873574f67467874337464',
                'start_id': 0,
                'debug': 0
                }
        self.cls = Device(**kwargs)


    @patch('mirobo.device.Device.discover')
    def test_happy_path__do_discover(self, mock_device_discover):
        """
        Test happy path flow.

        Args:
            mock_device_discover (MagicMock): MagicMock device discover.
        """
        kwargs = {'ip': '192.168.0.2',
                'token': '5664326b306873574f67467874337464',
                'start_id': 0,
                'debug': 0
                }

        self.cls = Device(**kwargs)

        mock_device_discover.return_value = Mock_Socket()
        self.assertTrue(self.cls.do_discover() is not None)

    @patch('mirobo.device.Device.discover')
    def test_debug__do_discover(self, mock_device_discover):
        """
        Test when debug attribute is None.

        Args:
            mock_device_discover (MagicMock): MagicMock device discover.
        """
        kwargs = {'ip': '192.168.0.2',
                  'token': '5664326b306873574f67467874337464',
                  'start_id': 0,
                  'debug': 1
                  }

        self.cls = Device(**kwargs)

        mock_device_discover.return_value = Mock_Socket()
        self.assertTrue(self.cls.do_discover() is not None)

    @patch('mirobo.device.Device.discover')
    def test_none_discover__do_discover(self, mock_device_discover):
        """
        Test when Device.discover returns None.
        
        Args:
            mock_device_discover (MagicMock): MagicMock device discover.
        """
        kwargs = {'ip': '192.168.0.2',
                  'token': '5664326b306873574f67467874337464',
                  'start_id': 0,
                  'debug': 1
                  }

        self.cls = Device(**kwargs)

        mock_device_discover.return_value = None
        with self.assertRaises(DeviceException) as context:
            self.cls.do_discover()

        self.assertTrue('Unable to discover the device' in str(context.exception))



if __name__ == '__main__':
    unittest.main()
