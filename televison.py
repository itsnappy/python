class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self._status = False
        self._muted = False
        self._volume = self.MIN_VOLUME
        self._channel = self.MIN_CHANNEL

    def power(self) -> None:
        """
        Turn the TV on or off by changing the value of the status variable.
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

        # If any volume-related method is called when muted, unmute and adjust volume
        if self._muted:
            self._volume = Television.MIN_VOLUME

    def channel_up(self) -> None:
        """
        Increase the TV channel value when the TV is on.
        If the TV is on the maximum channel and this method is called,
        it should set the TV channel to the minimum channel.
        """
        if self._status:
            if self._channel < Television.MAX_CHANNEL:
                self._channel += 1
            else:
                self._channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decrease the TV channel value when the TV is on.
        If the TV is on the minimum channel and this method is called,
        it should set the TV channel to the maximum channel.
        """
        if self._status:
            if self._channel > Television.MIN_CHANNEL:
                self._channel -= 1
            else:
                self._channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increase the TV volume.
        If the TV is on the maximum volume and this method is called,
        the volume should just remain at the maximum.
        """
        if self._status and not self._muted:
            if self._volume < Television.MAX_VOLUME:
                self._volume += 1

    def volume_down(self) -> None:
        """
        Decrease the TV volume.
        If the TV is on the minimum volume and this method is called,
        the volume should just remain at the minimum.
        If muted, unmute and adjust volume.
        """
        if self._status and not self._muted:
            if self._volume > Television.MIN_VOLUME:
                self._volume -= 1

    def __str__(self) -> str:
        """
        Send the values of the TV object in the format:
        Power = [status], Channel = [channel], Volume = [volume]
        """
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"
