"""
contains only the clock object
"""

class Clock():
    """
    represents a time without a date
    """
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.fix_time()

    def __repr__(self):
        # return str(self.hour) + ':' + "{:2d}".format(self.minute)
        return str(self.hour).zfill(2) + ':' + str(self.minute).zfill(2)

    def __eq__(self, other):
        return bool(self.hour == other.hour
                    and self.minute == other.minute)

    def __add__(self, minutes):
        self.minute += minutes
        self.fix_time()
        return self

    def __sub__(self, minutes):
        self.minute -= minutes
        self.fix_time()
        return self

    def fix_time(self):
        """
        checks if self is a valid time and fixes it in place if not
        """
        while self.minute >= 60:
            self.minute -= 60
            self.hour += 1
        while self.hour >= 24:
            self.hour -= 24

        while self.minute < 0:
            self.minute += 60
            self.hour -= 1
        while self.hour < 0:
            self.hour += 24
