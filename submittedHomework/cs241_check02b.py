file = input("Enter file: ")
num_lines = 0
num_words = 0
with open(file,"r") as file:
    for line in file:
        words = line.split()
        num_lines += 1
        num_words += len(words)
        #num_words += 1
    print("The file contains {} lines and {} words.".format (num_lines, num_words))
    file.close()
