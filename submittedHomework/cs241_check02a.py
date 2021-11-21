def prompt_number():
    positive_num = int(input("Enter a positive number: "))
    while positive_num <= 0:
        print("Invalid entry. The number must be positive.")
        positive_num = int(input("Enter a positive number: "))
    else:
        print()
        return positive_num

def compute_sum(a,b,c):
    add_three = a + b + c
    return add_three

def main():
    a = prompt_number()
    b = prompt_number()
    c = prompt_number()
    total = compute_sum(a,b,c)
    print("The sum is: {}".format (total))
    
if __name__ == "__main__":
    main()
