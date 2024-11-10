

#تعریف توابع اصلی
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multipy(x,y):
    return x*y

def divide(x,y):
    
    if y==0:
        return "Division by zero is undefined"
    return x/y

#حلقه اصلی ماشین حساب
while True:
    #گرفتن ورودی از کاربر
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice=input("Enter choice (1,2,3,4,5):")

    if choice=='5':
            print("Exiting the calculator. GoodBye!")
            break
    num1=float(input("Enter first number:"))
    num2=float(input("Enter second number:"))

    
#اجرای عملیات بر اساس انتخاب کاربر
    if choice=='1':
        print("Result:", add(num1,num2))
        
    elif choice=='2':
        print("Result:",subtract(num1,num2))
        
    elif choice=='3':
        print("Result:",multipy(num1,num2))
            
    elif choice=='4':
        print("Result:",divide(num1,num2))
        
    else:
        print("Invalid input")