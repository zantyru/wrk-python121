class WaterDrop:
    def __init__(self, volume=1.0):
        self.volume = float(volume)

    def __str__(self):
        class_name = self.__class__.__name__
        return f"{class_name}({self.volume})"

    def _check_type(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"Ожидается экземпляр класса {self.__class__.__name__}, "
                f"но получен тип {type(other)}."
            )

    def __add__(self, other):
        self._check_type(other)
        result = WaterDrop(self.volume + other.volume)
        return result

    def __sub__(self, other):
        self._check_type(other)
        result = WaterDrop(self.volume - other.volume)
        return result

    def __mul__(self, other):
        self._check_type(other)
        result = WaterDrop(self.volume * other.volume)
        return result

    def __truediv__(self, other):
        self._check_type(other)
        result = WaterDrop(self.volume / other.volume)
        return result

    def __eq__(self, other):
        self._check_type(other)
        return self.volume == other.volume

    def __ne__(self, other):
        self._check_type(other)
        return self.volume != other.volume

    def __lt__(self, other):
        self._check_type(other)
        return self.volume < other.volume

    def __le__(self, other):
        self._check_type(other)
        return self.volume <= other.volume

    def __gt__(self, other):
        self._check_type(other)
        return self.volume > other.volume

    def __ge__(self, other):
        self._check_type(other)
        return self.volume >= other.volume

if __name__ == '__main__':
    wd1 = WaterDrop(10)
    wd2 = WaterDrop()

    wd3 = wd1 + wd2  # wd1.__add__(wd2)  # WaterDrop.__add__(wd1, wd2)
    wd4 = wd2 + wd1

    print(wd3, id(wd3))
    print(wd4, id(wd4))

    print("----------------")

    print(wd2, id(wd2))
    wd2 += wd2  # wd2 = wd2 + wd2
    print(wd2, id(wd2))
    wd2 += wd2  # wd2 = wd2 + wd2
    print(wd2, id(wd2))