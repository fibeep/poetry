def get_file_lines(filename):
    #open and read the file, then return a list of strings
    file_lines = open(filename, "r").readlines()
    lines_array = []
    for line in file_lines:
        split_lines = line.rstrip().split(",")
        lines_array.append(split_lines)
    return lines_array


lines_list = get_file_lines("poem.txt")
