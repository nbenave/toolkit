from dataclasses import dataclass

@dataclass
class Vector:
    x: float
    y: float

    def __truediv__(self, other: float) -> 'Vector': # /
        return Vector(self.x / other, self.y / other)

    def __rtruediv__(self, other: float) -> 'Vector': # /
        return Vector(other / self.x, other / self.y)

    def __mul__(self, other): # *
        return Vector(self.x * other, self.y * other)

    def __matmul__(self, other): # @
        return Vector(self.x * other.x, self.y * other.y)

    def __rmatmul__(self, other):  # @
        return Vector(other.x * self.x, other.y * self.y)

    def __add__(self, other): # +
        return Vector(self.x + other.x, self.y + other.y)

    def __mod__(self, other): # %
        return Vector(self.x % other.x, self.y % other.y)

    def __pow__(self, power, modulo=None): # **
        return Vector(self.x ** power, self.y ** power)

    def __floordiv__(self, other): # //
        return Vector(self.x // other.x, self.y // other.y)

def main() -> None:
    point = Vector(1,3)
    print(point / 2) # divide x and y by 2 (0.5,1.5)
    print(2 / point) # divide 2 by x and y (2,0.6666666666666666)
    print(point * 2) # multiply x and y by 2 (2,6)
    print(point @ Vector(3,3)) # multiply x and y by 3 and 3  (3,9)
    print(Vector(3,3) @ point) # multiply x and y by 3 and 3 (same as above)
    print(point + Vector(3,3)) # add x and y by 3 and 3   (4,6)
    print(point % Vector(3,3)) # mod x and y by 3 and 3  (1,0)
    print(point ** 2) # power x and y by 2  (1,9)
    print(point // Vector(3,3)) # floor divide x and y by 3 and 3   (0,1)


if __name__ == '__main__':
    main()
