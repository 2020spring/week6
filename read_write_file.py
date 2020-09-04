filename = 'data/inputData.txt'

# READING
with open(filename) as input_data:

    counter = 1
    print("1. reading line by line:")
    for line in input_data:
        print("line: ", counter, line)
        counter += 1

    # print("2. reading the whole content and assigning to a variable")
    # contents = input_data.read()
    # print(contents)

    # print("3. read line by line using readlines(), returns as list of lines")
    # if you choose this way you can loop lines outside of WITH statement
    # lines = input_data.readlines()  - reading line by line

# print(contents)
print("Reading a inputData.txt file completed")

# WRITING TO THE FILE
with open(filename, 'a') as file_object: # use 'w' to override, 'a' to append
    file_object.write("I love programming.\n")
    file_object.write("I love python.\n")