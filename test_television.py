import unittest
from television import Television

class TestTelevision(unittest.TestCase):

    def setUp(self):
        self.tv_instance = Television()

    def test_init(self):
        self.assertEqual(self.tv_instance._status, False)
        self.assertEqual(self.tv_instance._muted, False)
        self.assertEqual(self.tv_instance._volume, Television.MIN_VOLUME)
        self.assertEqual(self.tv_instance._channel, Television.MIN_CHANNEL)

    def test_power(self):
        self.tv_instance.power()
        self.assertEqual(self.tv_instance._status, True)

    def test_mute(self):
        self.tv_instance.mute()
        self.assertEqual(self.tv_instance._muted, True)

    def test_channel_up(self):
        self.tv_instance.channel_up()
        self.assertEqual(self.tv_instance._channel, Television.MIN_CHANNEL + 1)

    def test_channel_down(self):
        self.tv_instance.channel_down()
        self.assertEqual(self.tv_instance._channel, Television.MAX_CHANNEL)

    def test_volume_up(self):
        self.tv_instance.volume_up()
        self.assertEqual(self.tv_instance._volume, Television.MIN_VOLUME + 1)

    def test_volume_down(self):
        self.tv_instance.volume_down()
        self.assertEqual(self.tv_instance._volume, Television.MIN_VOLUME)

    def test_str(self):
        self.assertEqual(str(self.tv_instance), "Power = [False], Channel = [0], Volume = [0]")

if __name__ == '__main__':
    unittest.main()
