"""Description of diodes and transistors.
"""


import math


class Diode(object):

    def __init__(self, saturation_current, ideality_factor=1):
        self.saturation_current = saturation_current
        self.max_fwd_ddp = 0.7
        self.ideality_factor = ideality_factor
        self.thermal_ddp = 0.02585

    def __str__(self):
        ret = 'Is = {}\nmax V = {}\nn = {}\nVt = {}'.format(
            self.saturation_current,
            self.max_fwd_ddp,
            self.ideality_factor,
            self.thermal_ddp
        )

        return ret

    def calculate_current(self, fwd_ddp):
        if fwd_ddp > self.max_fwd_ddp:
            fwd_ddp = self.max_fwd_ddp

        exponent = fwd_ddp / (self.ideality_factor * self.thermal_ddp)

        return self.saturation_current * math.expm1(exponent)


if __name__ == '__main__':
    diode = Diode(25 / 1000000000)
    print(diode)

    print('\nfwd_ddp: 0.4')
    print('current:', diode.calculate_current(0.4))

    print('\nfwd_ddp: 1')
    print('current:', diode.calculate_current(1))

    print('\nfwd_ddp: -0.1')
    print('current:', diode.calculate_current(-0.1))

    print()
    diode = Diode(25 / 1000000000, 1.3)
    print(diode)

    print('\nfwd_ddp: 0.4')
    print('current:', diode.calculate_current(0.4))

    print('\nfwd_ddp: 1')
    print('current:', diode.calculate_current(1))

    print('\nfwd_ddp: -0.1')
    print('current:', diode.calculate_current(-0.1))
