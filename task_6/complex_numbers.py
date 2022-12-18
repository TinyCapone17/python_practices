
class ComplexNumber:
    def __init__(self, re, im):
        self._re = re
        self._im = im

    @property
    def re(self):
        return self._re

    @property
    def im(self):
        return self._im

    def __repr__(self):
        return f"{self.re} + {self.im}i"

    def __str__(self):
        return repr(self)

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self + ComplexNumber(other, 0)
        return ComplexNumber(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return self - ComplexNumber(other, 0)
        return ComplexNumber(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self * ComplexNumber(other, 0)
        re = self.re * other.re - self.im * other.im
        im = self.re * other.im + self.im * other.re
        return ComplexNumber(re, im)

    def conjugate(self):
        return ComplexNumber(self.re, -self.im)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return self / ComplexNumber(other, 0)
        # Implement division using the conjugate to avoid division by zero
        other_conj = other.conjugate()
        numerator = self * other_conj
        denominator = other * other_conj
        return ComplexNumber(numerator.re / denominator.re, numerator.im / denominator.re)

    def __abs__(self):
        # Calculate the absolute value (magnitude) of the complex number
        return (self.re ** 2 + self.im ** 2) ** 0.5

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self == ComplexNumber(other, 0)
        return self.re == other.re and self.im == other.im


def test_complex_class():
    c1 = ComplexNumber(1, 2)
    c2 = ComplexNumber(3, 4)
    c3 = ComplexNumber(1, 2)

    assert str(c1) == "1 + 2i"
    assert repr(c1) == "1 + 2i"

    assert c1 + c2 == ComplexNumber(4, 6)
    assert c1 + 2 == ComplexNumber(3, 2)
    assert c1 - c2 == ComplexNumber(-2, -2)
    assert c1 - 2 == ComplexNumber(-1, 2)
    assert c1 * c2 == ComplexNumber(-5, 10)
    assert c1 * 2 == ComplexNumber(2, 4)
    assert c1.conjugate() == ComplexNumber(1, -2)
    assert c1 / c2 == ComplexNumber(0.44, 0.08)
    assert c1 / 2 == ComplexNumber(0.5, 1)
    assert abs(c1) == 5 ** 0.5
    assert c1 == c3
