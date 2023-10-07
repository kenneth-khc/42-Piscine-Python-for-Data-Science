def all_thing_is_obj(object: any) -> int:
    """Checks for certain types."""

    obj_type = type(object)
    type_str = str(obj_type)

    if obj_type == list:
        print(f"List : {type_str}")

    elif obj_type == tuple:
        print(f"List : {type_str}")

    elif obj_type == set:
        print(f"Set : {type_str}")

    elif obj_type == dict:
        print(f"Dict : {type_str}")

    elif obj_type == str:
        print(f"{object} is in the kitchen : {type_str}")

    else:
        print("Type not found")

    return 42
