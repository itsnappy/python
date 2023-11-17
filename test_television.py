import pytest
from television import Television

# Instantiate a Television object for testing
tv = Television()

def test_power():
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_channel_up():
    tv.power()
    tv.channel_up()
    tv.channel_up()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 2, Volume = 1"

def test_channel_down():
    tv.power()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    tv.volume_down()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"

def test_power_off():
    tv.power()
    tv.volume_up()
    tv.channel_down()
    assert str(tv) == "Power = False, Channel = 1, Volume = 0"

def test_complex_scenario():
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()
    tv.channel_down()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 2"

def test_another_television():
    tv_2 = Television()
    tv_2.power()
    tv_2.channel_up()
    tv_2.volume_up()
    assert str(tv_2) == "Power = True, Channel = 1, Volume = 1"

def test_mute_effect():
    tv.power()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 1"
    tv.mute()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 3, Volume = 2"
    tv.power()
    tv.mute()
    assert str(tv) == "Power = False, Channel = 3, Volume = 2"
