my_tuple = (10, "Ayshi", 3.14, True)

num, text, decimal, boolean = my_tuple

print("Unpacked Tuple Values:")

print("Number:", num)
print("Text:", text)
print("Decimal:", decimal)
print("Boolean:", boolean)

another_tuple = (20, "Hello", 2.71, True)

print("\nNow comparing two tuples:\n")

print("Are both tuples equal?", my_tuple == another_tuple)

print("Are they different?", my_tuple != another_tuple)

print("Is first tuple greater?", my_tuple > another_tuple)

print("Is first tuple smaller?", my_tuple < another_tuple)

print("Is first tuple greater or equal?", my_tuple >= another_tuple)

print("Is first tuple smaller or equal?", my_tuple <= another_tuple)


"""
Simple idea about List vs Tuple:

List:
1. We can change it anytime (add, remove, update values)
2. Uses square brackets []

Tuple:
1. Once created, we cannot change it
2. Uses round brackets ()

So basically,
List= flexible and changeable
Tuple= fixed 
"""