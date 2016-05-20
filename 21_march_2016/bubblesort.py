def selection_sort(list):
    sorted_list =[]
    for i in range(0,len(list)):
        min_element = min(list)
        index_of_min_element = list.index(min_element)
        sorted_list.append(min_element)
        del list[index_of_min_element]
    return sorted_list

##This was s]a selection sort program

z = []

loop = int(input())   #this is no of term thre loop continue

for i in range(0,loop):
    n_sepated_input = input()                  #It is n separated integer
    num = n_separated_input.split()
    x = [int(n) for n in num]
    z = selection_sort(x)       #Calling the function selection sort
    print(z)
