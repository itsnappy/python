import pytest
from television import Television

@pytest.fixture
def tv_instance():
    return Television()

def test_init(tv_instance):
    assert tv_instance._status == False
    assert tv_instance._muted == False
    assert tv_instance._volume == Television.MIN_VOLUME
    assert tv_instance._channel == Television.MIN_CHANNEL

def test_power(tv_instance):
    tv_instance.power()
    assert tv_instance._status == True

def test_mute(tv_instance):
    tv_instance.mute()
    assert tv_instance._muted == True

def test_channel_up(tv_instance):
    tv_instance.channel_up()
    assert tv_instance._channel == Television.MIN_CHANNEL + 1

def test_channel_down(tv_instance):
    tv_instance.channel_down()
    assert tv_instance._channel == Television.MAX_CHANNEL

def test_volume_up(tv_instance):
    tv_instance.volume_up()
    assert tv_instance._volume == Television.MIN_VOLUME + 1

def test_volume_down(tv_instance):
    tv_instance.volume_down()
    assert tv_instance._volume == Television.MIN_VOLUME

def test_str(tv_instance):
    assert str(tv_instance) == "Power = [False], Channel = [0], Volume = [0]"
