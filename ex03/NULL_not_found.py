def NULL_not_found(object: any) -> int:
    obj_type = type(object)
    if object:
        if object != object:
            print("Cheese: nan " + str(obj_type))
        else:
            print("Type not Found")
        return 1
    else:
        if object is None:
            print("Nothing: None " + str(obj_type))
        elif object is False:
            print("Fake: False " + str(obj_type))
        elif object == 0:
            print("Zero: 0 " + str(obj_type))
        elif object == "":
            print("Empty: " + str(obj_type))
        return 0
