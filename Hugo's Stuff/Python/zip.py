#By Hugo Lewczak

list1 = ["banana", "apple", "cherry"]
list2 = [3, 1, 2]
list3 = ["yellow", "red", "dark red"]

#Ascending

# Sort all lists based on list1
sorted_lists = sorted(zip(list1, list2, list3))

# Unzip the sorted tuples
sorted_list1, sorted_list2, sorted_list3 = map(list, zip(*sorted_lists))

print(sorted_list1)  # ['apple', 'banana', 'cherry']
print(sorted_list2)  # [1, 3, 2]
print(sorted_list3)  # ['red', 'yellow', 'dark red']

#Descending

# Sort all lists based on list1
sorted_lists = sorted(zip(list1, list2, list3), reverse=True)

# Unzip the sorted tuples
sorted_list1, sorted_list2, sorted_list3 = map(list, zip(*sorted_lists))

print(sorted_list1)  # ['apple', 'banana', 'cherry']
print(sorted_list2)  # [1, 3, 2]
print(sorted_list3)  # ['red', 'yellow', 'dark red']
