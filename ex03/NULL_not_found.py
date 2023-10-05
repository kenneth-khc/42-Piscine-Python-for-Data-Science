def NULL_not_found(object: any) -> int:
    """Checks for NULLS."""

    obj_type = type(object)
    type_str = str(obj_type)

    if object:
        if object != object:
            print(f"Cheese: nan {type_str}")
            return 0

        else:
            print("Type not Found")
            return 1

    else:
        if object is None:
            print(f"Nothing: None {type_str}")

        elif object is False:
            print(f"Fake: False {type_str}")

        elif object == 0:
            print(f"Zero: 0 {type_str}")

        elif object == "":
            print(f"Empty: {type_str}")

        return 0
