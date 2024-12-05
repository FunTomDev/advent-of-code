def get_wrong_rule(update_order:list[str], rules:list[str]):

    '''
    Return rule which causes wrong order in update. If not found - return 0
    '''

    good = True
    wrong_rule = ''
    n = len(update_order)

    for rule in rules:
        a, b = rule.split("|")

        if not good:
            break

        for i in range(n//2):

            if any([x not in update_order for x in [a,b]]): #if one of given rules not present in the update
                break

            if update_order[i] == a or update_order[n-i-1] == b: #if correct order
                break

            if update_order[i] == b or update_order[n-i-1] == a: #if wrong order
                good = False
                wrong_rule = rule
                break

    return 0 if good else wrong_rule


def search_indexes(update_order:list[str], rule:str):
    '''
    Get list indexes of pages a | b given in current rule
    '''

    a,b = rule.split("|")
    n = len(update_order)

    i = 0
    j = 0
    
    i_found = False
    j_found = False

    while (not i_found or not j_found):

        if not i_found:
            if update_order[i] != a:
                i += 1
            else:
                i_found = True

        if not j_found:
            if update_order[n-j-1] != b:
                j += 1
            else:
                j_found = True

    return [i,n-1-j]

def fix_order(update_order:list[str], rules:list[str]):

    '''
    Fix page order of given update until it matches given rulelist
    '''

    rule = get_wrong_rule(update_order, rules)

    while rule:

        i, j = search_indexes(update_order, rule)
        update_order[i], update_order[j] = update_order[j], update_order[i]

        rule = get_wrong_rule(update_order, rules)

def get_fixed_middle(update:str, rules:list[str]):

    '''
    Fix given update to match rules and return its middle element
    '''

    update_order = update.split(",")

    if get_wrong_rule(update_order, rules):
        fix_order(update_order, rules)
        return int(update_order[len(update_order)//2])

    return 0

def main():

    suma = 0

    with open("input.txt", "r") as file:
        lines = file.read().strip().split("\n\n")
        rules, updates = [x.split("\n") for x in lines]
        for update in updates:
            suma += get_fixed_middle(update, rules)

    print(suma)

if __name__ == "__main__":
    main()