# x=int(input("what is the number?"))

# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
def main():
    x=int(input("what is the number?"))
    if is_even(x):
        print("even")
    else:
        print("Odd")

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
    
    
    #the expart option
# def is_even(n):
#     return True if n % 2 == 0 else False       
        
        #More tricky
def is_even(n):
    return n % 2 == 0
        
        
        
        
        
        
main()
#fix the problem