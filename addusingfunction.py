list = ['Sanjeev',10, 20, 30, 40, 50, "Suraj", True, 50]

def add(list):
    result = 0
    for i in list:
        if type(i) == int:
            result += i
        else:
            print(f"'{i}' is not an integer and will be ignored.")
    return result
print("The sum is:", add(list))
