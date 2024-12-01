def get_n_sorted(table:list):
    n = len(table)    
    for i in range(1):
        for j in range(n - i - 1):
            if table[j] > table[j+1]:
                table[j], table[j+1] = table[j+1], table[j]
    return table[-1]

def get_max(a:int, b:int):
    if a >= b:
        return a
    else:
        return b

def get_repeats(tab2:list[int], tabs_max:int):
    repeats = [0] * (tabs_max + 1)

    for i in tab2:
        repeats[i] += 1
    
    return repeats

with open("input.txt", "r") as file:
    lines = file.read().split("\n")[:-1]
    tab1 = [int(x.split("   ")[0]) for x in lines]
    tab2 = [int(x.split("   ")[1]) for x in lines]
    
    repeats = get_repeats(tab2, get_max(get_n_sorted(tab1), get_n_sorted(tab2)))

    score = 0

    for i in tab1:
        score += repeats[i] * i
    
    print(score)