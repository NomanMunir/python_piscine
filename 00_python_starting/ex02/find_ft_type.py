def all_thing_is_obj(object: any) -> int:
    """Prints the type of the object in a specific format and returns 42."""

    if object.__class__ is list:
        print("List : <class 'list'>")
    elif object.__class__ is tuple:
        print("Tuple : <class 'tuple'>")
    elif object.__class__ is set:
        print("Set : <class 'set'>")
    elif object.__class__ is dict:
        print("Dict : <class 'dict'>")
    elif object.__class__ is str:
        print(f"{object} is in the kitchen : <class 'str'>")
    else:
        print("Type not found")
    return 42
