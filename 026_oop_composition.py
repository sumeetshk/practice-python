class Train:
    def get_fuels(self):
        return 'diesel'

    def get_speed(self):
        return "200Km/hr"

    def get_type(self):
        return "A train"


class Bus:
    def get_fuels(self):
        return 'electricity'

    def get_speed(self):
        return "80Km/hr"

    def get_type(self):
        return "A bus"


class Transport:
    def __init__(self, transport):
        self.transport = transport

    def travel(self):
        fuels = self.transport.get_fuels()
        return self.transport.get_type() + " uses " + fuels

    def distance_covered(self, hrs):
        km = int(self.transport.get_speed().strip("Km/hr"))
        return (
            self.transport.get_type() + " covers " + str(hrs * km)
            + "Km in " + str(hrs) + " hours."
        )


train = Transport(Train())
bus = Transport(Bus())

print(train.travel())
print(bus.travel())
print(train.distance_covered(3))
print(bus.distance_covered(3))


class Train:
    def get_fuels(self):
        return 'diesel'

    def get_speed(self):
        return "200Km/hr"

    def get_type(self):
        return "A train"


class Bus:
    def get_fuels(self):
        return 'electricity'

    def get_speed(self):
        return "80Km/hr"

    def get_type(self):
        return "A bus"


class Transport:
    # Add the constructor with a transport argument
    def __init__(self, transport):
        self.transport = transport

    def travel(self):
        # Get fuels from transport object
        fuels = self.transport.get_fuels() # complete the code
        return
        # complete code below so outcome is:
        # A bus uses diesel / or A train uses electricity
        return # complete code

    def distance_covered(self, hrs):
        # Get speed from the transport object
        # use a string method to delete 'Km/hr' part from speed
        # and return an integer
        km = # complete the code
        return (
            # complete code so outcome is:
            # A train covers <km> in <hrs> hours.
            # or A bus covers <km> in <hrs> hours.

        )


train = Transport(Train())
bus = Transport(Bus())

print(train.travel())
print(bus.travel())
print(train.distance_covered(3))
print(bus.distance_covered(3))
