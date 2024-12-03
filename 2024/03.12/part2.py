def mul(nums:list[int]):

    return nums[0] * nums[1]

def find_mul(text:str):

    suma = 0
    possible_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ","]

    n = len(text)
    if n<8:
        return 0

    enabled = True

    for i in range(0,n-4):
        if text[i:i+4] == "do()":
            enabled = True
        if text[i:i+7] == "don't()":
            enabled = False
        if text[i:i+4] == "mul(" and enabled:
            j = i + 4

            match = True
            comma = False
            while text[j] != ")":

                if text[j] == ",":
                    comma = True
                if text[j] not in possible_chars:
                    match = False
                    break
                j += 1

            if match and comma:
                suma += mul([int(x) for x in text[i+4:j].split(",")])
    return suma

def main():
    with open("input.txt", "r") as file:
        text = file.read()
        print(find_mul(text))

if __name__ == "__main__":
    main()