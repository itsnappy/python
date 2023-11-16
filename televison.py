class Television:
    # Class variables
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initialize a Television object with default values.

        Instance Variables:
            _status (bool): Represents the power status of the TV.
            _muted (bool): Represents the mute status of the TV.
            _volume (int): Represents the volume level of the TV.
            _channel (int): Represents the channel of the TV.

        The default values are False for status and muted, MIN_VOLUME for volume,
        and MIN_CHANNEL for channel.
        """
        self._status: bool = False
        self._muted: bool = False
        self._volume: int = self.MIN_VOLUME
        self._channel: int = self.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggle the power status of the TV.
        If the TV is off, turn it on; if it's on, turn it off.
        """
        self._status = not self._status

    def mute(self) -> None:
        """
        Toggle the mute status of the TV.
        If the TV is muted, unmute it; if it's unmuted, mute it.
        If any volume-related method is called when the TV is muted,
        it will automatically unmute the TV and adjust the volume accordingly.
        """
        self._muted = not self._muted
        if self._muted:
            self._muted = False

    def channel_up(self) -> None:
        """
        Increase the TV channel.
        If the TV is on the maximum channel, loop back to the minimum channel.
        """
        if self._status:
            self._channel = (self._channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        """
        Decrease the TV channel.
        If the TV is on the minimum channel, loop back to the maximum channel.
        """
        if self._status:
            self._channel = (self._channel - 1) % (self.MAX_CHANNEL + 1)

    def volume_up(self) -> None:
        """
        Increase the TV volume.
        If the TV is on the maximum volume, the volume remains at the maximum.
        """
        if self._status and not self._muted:
            self._volume = min(self._volume + 1, self.MAX_VOLUME)

    def volume_down(self) -> None:
        """
        Decrease the TV volume.
        If the TV is on the minimum volume, the volume remains at the minimum.
        """
        if self._status and not self._muted:
            self._volume = max(self._volume - 1, self.MIN_VOLUME)

    def __str__(self) -> str:
    """
    Return a formatted string representation of the TV object.

    Format:
        If the TV is muted:
            Power = [status], Muted, Channel = [channel], Volume = [volume]
        If the TV is not muted:
            Power = [status], Channel = [channel], Volume = [volume]

    The items placed in brackets hold the current values of the TV variables.
    """
    if self._muted:
        return f"Power = [{self._status}], Muted, Channel = [{self._channel}], Volume = [{self._volume}]"
    else:
        return f"Power = [{self._status}], Channel = [{self._channel}], Volume = [{self._volume}]"
