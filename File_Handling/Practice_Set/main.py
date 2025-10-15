import random

# problem 1
# with open("poem.txt", "r") as file:
#     content = file.read()
#     if("twinkle" in content):
#         print("Yes, 'twinkle' is present in the file.")
#     else:
#         print("No, 'twinkle' is not present in the file.")        

# problem 2 write in a file separate separate
def Generate_Table(n):
    with open(f"tables/table_of_{n}.txt", "w") as file:
        for i in range(1, 11):
            file.write(f"{n} x {i} = {n*i}\n")
    # print(f"Table of {n} has been written to table_of_{n}.txt")
    
for i in range(31,40):
    Generate_Table(i)
    
# problem 2 append in a single file
def Generate_table(n):
    with open(f"table.txt", "a") as file:
        for i in range(1,11):
            file.write(f"{n}*{i}={n*i}\n")
            if(i==10):
                file.write(f"{'-'*40}\n")
    # print(f"Table of {n} has been written to table.txt")
    
for i in range(11,20):
    Generate_table(i)