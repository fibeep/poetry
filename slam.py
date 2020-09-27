from random import randint
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

#Prints lines randomly, not sure how to make it NOT double count
def lines_printed_random(lines_list):
    for i in lines_list:
        print(lines_list[randint(0, 26)])


lines_printed_random(lines_list)

#This custom function will determine whether the text 
#document has an even or odd number of lines, and then
#print the even or odd lines ONLY accordingly

def lines_printed_custom(lines_list):
    if (len(lines_list) % 2) == 0: #Determines if text doc is even
        for i in range(len(lines_list)):
            if i % 2 == 0: #determines which lines are even
                print(lines_list[i + 1]) #prints the index + 1, because line 2 is index 1 (which is not even)
    else: # same as above but for odds
        for i in range(len(lines_list)):
            if i % 2 !== 0: 
                print(lines_list[i])


lines_printed_custom(lines_list)
