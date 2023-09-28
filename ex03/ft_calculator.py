class calculator:

    def __init__(self, vector):
        """Initialize an instance of a calculator."""

        self.vector = vector

    def __add__(self, object) -> None:
        """Applies addition on each element in the vector with object"""

        for i in range(len(self.vector)):
            self.vector[i] += object

        print(self.vector)

    def __mul__(self, object) -> None:
        """Applies multiplication on each element in the vector with object"""

        for i in range(len(self.vector)):
            self.vector[i] *= object

        print(self.vector)

    def __sub__(self, object) -> None:
        """Applies subtraction on each element in the vector with object"""

        for i in range(len(self.vector)):
            self.vector[i] -= object
    
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Applies non-floor division on each element in the vector with object"""

        try:
            for i in range(len(self.vector)):
                self.vector[i] /= object

        except ZeroDivisionError as e:
            print(f"Error: {e}.")

        print(self.vector)

