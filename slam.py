def get_file_lines(filename):
    #open and read the file, then return a list of strings
    file_lines = open(filename, "r").readlines()
    lines_array = []
    for line in file_lines:
        split_lines = line.rstrip().split(",")
        lines_array.append(split_lines)
    return lines_array


lines_list = get_file_lines("poem.txt")

# Prints the poem backwards as well as their initial starting position
def lines_printed_backwards(lines_list):
    for i in range(len(lines_list)):
        print(len(lines_list) - (i), lines_list[-(i + 1)])


lines_printed_backwards(lines_list)
