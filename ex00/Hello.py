ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# Use case: When you need a collection of items that can change (e.g., shopping list, to-do list).
ft_list[1] = "World!"
# Ordered: The elements have an order (index-based).
# Mutable: You can change, add, or remove elements.
# Allows duplicates

# ft_tuple[1] = "World!"
# Use case: When you want a fixed collection that won’t change (e.g., coordinates, RGB colors).
ft_tuple = ("Hello", "UAE!")
# Ordered: Like a list, but...
# Immutable: You cannot change it after creation.
# Allows duplicates.


# Use case: When you need a collection of unique items (e.g., tags, unique identifiers).
ft_set.remove("tutu!")
ft_set.add("Abu Dhabi!")
# Unordered: No index. Elements can appear in any order.
# Mutable: You can add/remove items.
# No duplicates: Repeated values are auto-removed.


# Use case: When you need a key-value pair structure (e.g., phone book, configuration settings).
ft_dict["Hello"] = "42AbuDhabi!"
# Key-value structure: Each value is accessed via a unique key.
# Mutable: You can add, change, or remove keys/values.
# No duplicate keys (but values can repeat).

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
