def NULL_not_found(object: any) -> int:
    """Prints the label, value and type of
        null-like objects. Returns 0 or 1."""

    if object is None:
        print("Nothing:", object, object.__class__)
        return 0
    elif object.__class__ is float and object != object:
        print("Cheese:", object, object.__class__)
        return 0
    elif object == 0 and object.__class__ is int:
        print("Zero:", object, object.__class__)
        return 0
    elif object == '' and object.__class__ is str:
        print("Empty:", object.__class__)
        return 0
    elif object is False:
        print("Fake:", object, object.__class__)
        return 0
    else:
        print("Type not found")
        return 1
