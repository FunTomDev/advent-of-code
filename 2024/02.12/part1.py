def get_abs(a:int):
    return a if a >= 0 else -a

def get_difference(a:int, b:int):
    return a - b

def safe_level(a:int, b:int, last_difference:int):

    difference = get_difference(a, b)

    if get_abs(difference) in range(1,4) and difference * last_difference >= 0:
        return True, difference
    return False, 0

def safe_report(report:list[int]):
    last_difference = 0
    for i in range(len(report) - 1):
        is_safe, last_difference = safe_level(report[i], report[i+1], last_difference)
        if not is_safe:
            return False
    return True

def main():

    safe_reports_count = 0

    with open("input.txt", "r") as file:
        reports = [[int(y) for y in x.split(' ')] for x in file.read().strip().split('\n')]
    

    for report in reports:
        if safe_report(report):
            safe_reports_count += 1

    print(safe_reports_count)

if __name__ == '__main__':
    main()