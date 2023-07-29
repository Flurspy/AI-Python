def remove_duplicates(li, l2):
        for element in li:
            if element not in l2:
                l2.append(element)
        print(l2)
list1 = [12, 23, 15, 67, 12, 0, 15, 13]
list2 = []
print(remove_duplicates(list1, list2))