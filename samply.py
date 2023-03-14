#Count number of fruits
fruits_list=["apple", "orange", "strawberry", "orange", "apple"]

def count_fruits(fruits_list):
    fruit_data = {}
    for each_fruit in fruits_list:
        if each_fruit not in fruit_data:
            fruit_data[each_fruit] = 1
        else:
            fruit_data[each_fruit] += 1
    return fruit_data
print(count_fruits(fruits_list))

# move first n elements to last
input_list = [4,6,8,9,5,3]
n = 2

new_list = input_list[n:] + input_list[0:n]
print(new_list)
