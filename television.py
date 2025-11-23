class Television:
    """
    A class representing details for a television object
    """
    MIN_VOLUME = 0
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    MAX_VOLUME = 2

    def __init__(self) -> None:
        """
        Method to set default values of TV object
        :muted: if TV is muted
        :volume: TV's minimum volume
        :channel: TV's minimum channel
        :status: if TV is powered on
        """
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__status = False
    def power(self):
        """
        Method to power the TV on/off
        """
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False
    def mute(self):
        """
        Method to mute/unmute the TV
        """
        if self.__status:
            if self.__muted == False:
                self.__muted = True
            else:
                self.__muted = False
                
    def channel_up(self):
        """
        Method to move the TV channel up
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL
    def channel_down(self):
        """
        Method to move the TV channel down
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL
    
    def volume_up(self):
        """
        Method to turn the TV volume up
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
    
    def volume_down(self):
        """
        Method to turn the TV volume down
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        :return string explaining the status, channel, and volume of TV object
        """
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"