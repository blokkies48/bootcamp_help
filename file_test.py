from random import randint
import re
def random_num(r1,r2):
    random_num_lst = []
    for i in range(r1,r2+1):
        random_num_lst.append(randint(1,99))
    return random_num_lst

def randint_to_string(random_num_list):
    return " ".join(str(num) for num in random_num_list)

list_r = random_num(1,10)
list_r.sort()
list_r_str = randint_to_string(list_r)

list_r2 = random_num(1,10)
list_r2.sort(reverse=True)
list_r2_str = randint_to_string(list_r2)

f = open("numbers1.txt", "w+")
f.write("this is file_one \n""It has random nubers for min to max\n" + list_r_str)
f.close()

f = open("numbers2.txt", "w+")
f.write("this is file_two \n"+"It has random nubers for max to min\n" + list_r2_str)
f.close()

filenames = ["numbers1.txt", "numbers2.txt"]

f3_num = []

with open("all_numbers.txt", "w") as outfile:
    outfile.write("File_three contains content form both file one and file two")
    for names in filenames:
        with open(names) as infile:
            numbers = re.findall(r"(\d+)", infile.read())
            f3_num += numbers
        outfile.write("\n")

    f3_num.sort()

    f3_num_str = randint_to_string(f3_num)

    outfile.write(f3_num_str)