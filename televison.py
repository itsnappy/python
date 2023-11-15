class Television:
    # Class variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        # Instance variables
        self._status = False
        self._muted = False
        self._volume = self.MIN_VOLUME
        self._channel = self.MIN_CHANNEL

    def power(self):
        # Toggle the power status
        self._status = not self._status

    def mute(self):
        # Toggle mute status and unmute if muted
        self._muted = not self._muted
        if self._muted:
            self._muted = False

    def channel_up(self):
        # Increase channel or loop back to MIN_CHANNEL if at MAX_CHANNEL
        if self._status:
            self._channel = (self._channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self):
        # Decrease channel or loop back to MAX_CHANNEL if at MIN_CHANNEL
        if self._status:
            self._channel = (self._channel - 1) % (self.MAX_CHANNEL + 1)

    def volume_up(self):
        # Increase volume within limits
        if self._status and not self._muted:
            self._volume = min(self._volume + 1, self.MAX_VOLUME)

    def volume_down(self):
        # Decrease volume within limits
        if self._status and not self._muted:
            self._volume = max(self._volume - 1, self.MIN_VOLUME)

    def __str__(self):
        # Return formatted string representation of TV object
        return f"Power = [{self._status}], Channel = [{self._channel}], Volume = [{self._volume}]"
