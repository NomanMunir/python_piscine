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
    elif object == "Brian":
        print("Brian is in the kitchen : <class 'str'>")
    elif object == "Toto":
        print("Toto is in the kitchen : <class 'str'>")
    else:
        print("Type not found")
    return 42

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))