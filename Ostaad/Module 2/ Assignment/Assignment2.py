def set_operations(set1=None, set2=None):
   
    if set1 is None:
        set1 = set()
    if set2 is None:
        set2 = set()

    union_result = set1 | set2
    intersection_result = set1 & set2
    difference_result = set1 - set2

    print("Set 1:", set1)
    print("Set 2:", set2)

    print("\nUnion:", union_result)
    print("Intersection:", intersection_result)
    print("Difference (Set1 - Set2):", difference_result)


set_operations(set1={1, 2, 3, 4}, set2={3, 4, 5, 6})