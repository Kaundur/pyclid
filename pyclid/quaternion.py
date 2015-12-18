import math

import pyclid.vector
import pyclid.matrix


class Quat:
    def __init__(self, q0=0, q1=0, q2=0, q3=0):
        self.q0 = q0
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3

    def __eq__(self, other):
        assert isinstance(other, Quat), 'Cannot call eq on a non-Quaternion'
        if self.q0 == other.q0 and self.q1 == other.q1 and self.q2 == other.q2 and self.q3 == other.q3:
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        assert isinstance(other, Quat), 'Cannot call addition on a non-Quaternion'
        self.q0 = self.q0 + other.q0
        self.q1 = self.q1 + other.q1
        self.q2 = self.q2 + other.q2
        self.q3 = self.q3 + other.q3

        return self

    def __sub__(self, other):
        assert isinstance(other, Quat), 'Cannot call subtraction on a non-Quaternion'
        self.q0 = self.q0 - other.q0
        self.q1 = self.q1 - other.q1
        self.q2 = self.q2 - other.q2
        self.q3 = self.q3 - other.q3

        return self

    def __str__(self):
        return '(' + str(self.q0) + ', ' + str(self.q1) + ', ' + str(self.q2) + ', ' + str(self.q3) + ')'

    def __mul__(self, other):
        assert isinstance(other, (Quat, int, float)), 'Cannot call multiplication on non-Quaternion or non-number'

        if isinstance(other, Quat):
            # In matrix form
            # Self
            # p0, -p1, -p2, -p3
            # p1, p0, -p3, p2
            # p2, p3, p0, -p1
            # p3, -p2, p1, p0

            # multiply by
            # Other
            # q0, q1, q2, q3

            mat = pyclid.matrix.Mat4([self.q0, -self.q1, -self.q2, -self.q3,
                               self.q1,  self.q0, -self.q3,  self.q2,
                               self.q2,  self.q3,  self.q0, -self.q1,
                               self.q3, -self.q2,  self.q1,  self.q0])
            vec = pyclid.vector.Vec4(other.q0, other.q1, other.q2, other.q3)

            quat = mat*vec
            return Quat(quat.x, quat.y, quat.z, quat.w)
        else:
            self.q0 *= other
            self.q1 *= other
            self.q2 *= other
            self.q3 *= other
        return self

    def __rmul__(self, other):
        return self.__mul__(other)

    def __abs__(self):
        return math.sqrt(self.q0**2 + self.q1**2 + self.q2**2 + self.q3**2)

    def magnitude(self):
        return self.__abs__()

    def norm(self):
        return self.__abs__()

    def unit(self):
        mag = self.norm()
        if mag:
            self.q0 /= mag
            self.q1 /= mag
            self.q2 /= mag
            self.q3 /= mag
        return self

    # Consider rename - normalize is similar to norm, but returns a unit quaternion
    def normalize(self):
        return self.unit()
