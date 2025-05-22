ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World!"
# Ordered: The elements have an order (index-based).
# Mutable: You can change, add, or remove elements.
# Allows duplicates

# ft_tuple[1] = "World!"
ft_tuple = ("Hello", "UAE!")
# Ordered: Like a list, but...
# Immutable: You cannot change it after creation.
# Allows duplicates.

ft_set.remove("tutu!")
ft_set.add("Abu Dhabi!")
# Unordered: No index. Elements can appear in any order.
# Mutable: You can add/remove items.
# No duplicates: Repeated values are auto-removed.

ft_dict["Hello"] = "42AbuDhabi!"
# Key-value structure: Each value is accessed via a unique key.
# Mutable: You can add, change, or remove keys/values.
# No duplicate keys (but values can repeat).

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
