class calculator:

    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Find the dot product of two vectors."""

        vectors_multiplied = [float(x * y) for x, y in zip(V1, V2)]
        result = sum(vectors_multiplied)
        print(f"Dot product is: {int(result)}")

    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors."""

        added_vec = [float(x + y) for x, y in zip(V1, V2)]
        print(f"Add Vector is : {added_vec}")

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract two vectors."""

        subtracted_vec = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Sous Vector is : {subtracted_vec}")
