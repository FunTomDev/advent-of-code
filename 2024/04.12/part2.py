def find_xmas(lines:int):
    n = len(lines)
    m = len(lines[0])

    word_length = 4

    word_count = 0

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "A":
                if n >= 3 and m >= 3 and j > 0 and j < m-1 and i > 0 and i < n-1:
                    wordlist = ''.join([lines[i - 1 if x == 0 else i + 1][j - 1 if y == 0 else j + 1] for x in range(2) for y in range(2)])
                    if wordlist in ["MSMS", "SSMM", "SMSM", "MMSS"]:
                        word_count += 1

    return word_count

def main():

    with open("input.txt", "r") as file:
        lines = file.read().strip().split('\n')
        print(find_xmas(lines))

if __name__ == "__main__":
    main()