# for _ in range(3):
#     print("#")
    
def main():
    print_column(3)
    print_row(4)
    print_squire(6)
    
def print_column(height):
    # print("#\n" * height,end="")
    for _ in range(height):
        print("#")
        
def print_row(width):
    print("?" * width)


# def print_squire(size):
#     for _ in range(size):
#         for j in range(size):
#             print("#",end="")
#         print()
        







main()