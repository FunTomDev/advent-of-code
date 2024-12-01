def get_distance(a:int, b:int):

    if a >= b:
        return a-b
    else:
        return b-a

def get_n_sorted(table:list):
    n = len(table)    
    for i in range(1):
        for j in range(n - i - 1):
            if table[j] < table[j+1]:
                table[j], table[j+1] = table[j+1], table[j]
    return table[:-1], table[-1]

with open("input.txt", "r") as file:
    lines = file.read().split("\n")[:-1]
    tab1 = [int(x.split("   ")[0]) for x in lines]
    tab2 = [int(x.split("   ")[1]) for x in lines]
    
    distance_sum = 0

    for i in range(len(tab1)):
        print(i)
        tab1, a = get_n_sorted(tab1)
        tab2, b = get_n_sorted(tab2)
        distance_sum += get_distance(a, b)
    
    print(distance_sum)