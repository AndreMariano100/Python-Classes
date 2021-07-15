"""
Basic "dunder" methods:
__abs__, __add__, __and__, __call__, __class__, __cmp__, __coerce__, __complex__, __contains__,
__del__, __delattr__, __delete__, __delitem__, __delslice__, __dict__, __div__, __divmod__, __eq__
__float__, __floordiv__, __ge__, __get__, __getattr__, __getattribute__, __getitem__, __getslice__,
__gt__, __hash__, __hex__, __iadd__, __iand__, __idiv__, __ifloordiv__, __ilshift__, __imod__,
__imul__, __index__, __init__, __instancecheck__, __int__, __invert__, __ior__, __ipow__,
__irshift__, __isub__, __iter__, __itruediv__, __ixor__, __le__, __len__, __long__, __lshift__,
__lt__, __metaclass__, __mod__, __mro__, __mul__, __ne__, __neg__, __new__, __nonzero__, __oct__,
__or__, __pos__, __pow__, __radd__, __rand__, __rcmp__, __rdiv__, __rdivmod__, __repr__, __reversed__,
__rfloordiv__, __rlshift__, __rmod__, __rmul__, __ror__, __rpow__, __rrshift__, __rshift__, __rsub__,
__rtruediv__, __rxor__, __set__, __setattr__, __setitem__, __setslice__, __slots__, __str__, __sub__
__subclasscheck__, __truediv__, __unicode__, __weakref__, __xor__
"""
import math


class Vector2D:
    """A two-dimensional vector with Cartesian coordinates."""

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        """Human-readable string representation of the vector. Shown when calling print() method."""
        return f'{self.x}i + {self.y}j'

    def __repr__(self):
        """Unambiguous string representation of the vector. Debugging Purposes."""
        return f'Vector2D({self.x}, {self.y})'

    def __add__(self, other):
        """Vector addition."""
        # print(f'Self: {self}')
        # print(f'Other: {other}')
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Vector subtraction."""
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """Multiplication of a vector by a scalar."""

        if isinstance(scalar, int) or isinstance(scalar, float):
            return Vector2D(self.x*scalar, self.y*scalar)
        raise NotImplementedError('Can only multiply Vector2D by a scalar')

    def __rmul__(self, scalar):
        """Reflected multiplication so scalar * vector also works."""
        return self.__mul__(scalar)

    def __neg__(self):
        """Negation of the vector (invert through origin.)"""
        return Vector2D(-self.x, -self.y)

    def __truediv__(self, scalar):
        """True division of the vector by a scalar."""
        return Vector2D(self.x / scalar, self.y / scalar)

    def __abs__(self):
        """Absolute value (magnitude) of the vector."""
        return (self.x**2 + self.y**2)**0.5

    def __lt__(self, other):
        """ Compares the length of two vectors """
        return abs(self) < abs(other)

    def __gt__(self, other):
        """ Compares the length of two vectors """
        return abs(self) > abs(other)

    def __eq__(self, other):
        """ Compares the length of two vectors """
        return abs(self) == abs(other)

    def __le__(self, other):
        """ Compares the length of two vectors """
        return abs(self) <= abs(other)

    def __ge__(self, other):
        """ Compares the length of two vectors """
        return abs(self) >= abs(other)

    def distance_to(self, other):
        """The distance between vectors self and other."""
        return abs(self - other)

    def dot(self, other):
        """The scalar (dot) product of self and other. Both must be vectors."""
        if not isinstance(other, Vector2D):
            raise TypeError('Can only take dot product of two Vector2D objects')
        return self.x * other.x + self.y * other.y
    # Alias the __matmul__ method to dot so we can use a @ b as well as a.dot(b).
    __matmul__ = dot

    def angle(self, other):
        """ The angle in between vectors """
        return math.degrees(math.acos((self.dot(other) / (abs(self) * abs(other)))))


if __name__ == '__main__':
    v1 = Vector2D(0, 1)
    v2 = Vector2D(1, 0)
    print(v1.angle(v2))
