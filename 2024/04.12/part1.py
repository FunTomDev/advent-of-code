def find_xmas(lines:int):
    n = len(lines)
    m = len(lines[0])

    word_length = 4

    word_count = 0

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "X":
                
                #check left

                if m >= word_length and j >= word_length - 1:
                    word = ''.join([lines[i][j-x] for x in range(4)])
                    if word == "XMAS":
                        word_count += 1

                #check right

                if m >= word_length and m-j >= word_length:
                    word = ''.join([lines[i][j+x] for x in range(4)])
                    if word == "XMAS":
                        word_count += 1

                #check top

                if n >= word_length and i >= word_length - 1:
                    word = ''.join([lines[i-x][j] for x in range(4)])
                    if word == "XMAS":
                        word_count += 1

                #check bottom

                if n >= word_length and n-i >= word_length:
                    word = ''.join([lines[i+x][j] for x in range(4)])
                    if word == "XMAS":
                        word_count += 1

                #check NE

                if m >= word_length and n >= word_length and i >= word_length - 1 and m-j >= word_length:
                    word = ''.join([lines[i-x][j+x] for x in range(4)])
                    if word == "XMAS":
                        word_count += 1

                #check SE

                if m >= word_length and n >= word_length and n-i >= word_length and m-j >= word_length:
                    word = ''.join([lines[i+x][j+x] for x in range(4)])
                    if word == "XMAS":
                        word_count += 1

                #check SW

                if m >= word_length and n >= word_length and n-i >= word_length and j >= word_length-1:
                    word = ''.join([lines[i+x][j-x] for x in range(4)])
                    if word == "XMAS":
                        word_count += 1

                #check NW

                if m >= word_length and n >= word_length and i >= word_length-1 and j >= word_length-1:
                    word = ''.join([lines[i-x][j-x] for x in range(4)])
                    if word == "XMAS":
                        word_count += 1

    return word_count

def main():

    with open("input.txt", "r") as file:
        lines = file.read().strip().split('\n')
        print(find_xmas(lines))

if __name__ == "__main__":
    main()