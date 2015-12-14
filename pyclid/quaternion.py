import vector

class Quat:
    def __init__(self):
        self.q0 = 0
        self.q1 = 0
        self.q2 = 0
        self.q3 = 0

    def __eq__(self, other):
        assert isinstance(other, Quat), 'Cannot call eq on a non-Quaternion'
        if self.q0 == other.q0 and self.q1 == other.q1 and self.q2 == other.q2 and self.q3 == other.q3:
            return True
        return False

    def __add__(self, other):
        assert isinstance(other, Quat), 'Cannot call addition on a non-Quaternion'
        self.q0 = self.q0 + other.q0
        self.q1 = self.q1 + other.q1
        self.q2 = self.q2 + other.q2
        self.q3 = self.q3 + other.q3

        return self

    def __str__(self):
        return '(' + str(self.q0) + ', ' + str(self.q1) + ', ' + str(self.q2) + ', ' + str(self.q3) + ')'


    def __mul__(self, other):
        assert isinstance(other, (Quat, int, float, long)), 'Cannot call multiplication on non-Quaternion or non-number'

        if isinstance(other, Quat):


            pass

        else:
            self.q0 *= other
            self.q1 *= other
            self.q2 *= other
            self.q3 *= other
        return self

    def __rmul__(self, other):
        return self.__mul__(other)
