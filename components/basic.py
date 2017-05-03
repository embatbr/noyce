"""Description of diodes and transistors.
"""


import math


class UnsetPinError(Exception):

    def __init__(self, msg_prefix):
        self.message = '{} must be set.'.format(msg_prefix)


class Pin(object):

    def __init__(self):
        self.__voltage = None

    def __str__(self):
        ret = '{} Volts'.format(self.__voltage)

    def set(self, voltage):
        assert isinstance(voltage, int) or isinstance(voltage, float)

        self.__voltage = voltage

    def unset(self):
        self.__voltage = None

    def read(self):
        return self.__voltage


class Diode(object):

    def __init__(self, saturation_current, ideality_factor=1):
        assert 1 <= ideality_factor <= 2, 'Idealty factor must be between 1 and 2.'

        self.saturation_current = saturation_current
        self.max_fwd_ddp = 0.7
        self.ideality_factor = ideality_factor
        self.thermal_ddp = 0.02585

        self.anode = Pin()
        self.cathode = Pin()

    def __str__(self):
        ret = 'Is = {}\nmax V = {}\nn = {}\nVt = {}'.format(
            self.saturation_current,
            self.max_fwd_ddp,
            self.ideality_factor,
            self.thermal_ddp
        )

        return ret

    def calculate_current(self):
        anode_voltage = self.anode.read()
        cathode_voltage = self.cathode.read()

        if (anode_voltage is None) or (cathode_voltage is None):
            raise UnsetPinError('Anode and cathode')

        fwd_ddp = anode_voltage - cathode_voltage

        if fwd_ddp > self.max_fwd_ddp:
            fwd_ddp = self.max_fwd_ddp

        exponent = fwd_ddp / (self.ideality_factor * self.thermal_ddp)

        return self.saturation_current * math.expm1(exponent)


if __name__ == '__main__':
    diode = Diode(25 / 1000000000)
    print(diode)
    print()

    try:
        diode.calculate_current()
    except UnsetPinError as err:
        print(err.message)

    diode.anode.set(0.2)
    diode.cathode.set(-0.2)
    print('\nanode: {}'.format(diode.anode.read()))
    print('cathode: {}'.format(diode.cathode.read()))
    print('current:', diode.calculate_current())

    diode.anode.set(1)
    diode.cathode.set(0)
    print('\nanode: {}'.format(diode.anode.read()))
    print('cathode: {}'.format(diode.cathode.read()))
    print('current:', diode.calculate_current())

    diode.anode.set(1)
    diode.cathode.set(1.1)
    print('\nanode: {}'.format(diode.anode.read()))
    print('cathode: {}'.format(diode.cathode.read()))
    print('current:', diode.calculate_current())

    print('\n===============\n')
    diode = Diode(25 / 1000000000, 1.3)
    print(diode)
    print()

    try:
        diode.calculate_current()
    except UnsetPinError as err:
        print(err.message)

    diode.anode.set(0.2)
    diode.cathode.set(-0.2)
    print('\nanode: {}'.format(diode.anode.read()))
    print('cathode: {}'.format(diode.cathode.read()))
    print('current:', diode.calculate_current())

    diode.anode.set(1)
    diode.cathode.set(0)
    print('\nanode: {}'.format(diode.anode.read()))
    print('cathode: {}'.format(diode.cathode.read()))
    print('current:', diode.calculate_current())

    diode.anode.set(1)
    diode.cathode.set(1.1)
    print('\nanode: {}'.format(diode.anode.read()))
    print('cathode: {}'.format(diode.cathode.read()))
    print('current:', diode.calculate_current())
