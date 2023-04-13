# get two integer parameters
# return sum
# 한국전쟁
def plus(x, y):
    return x+y

def minus(x, y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    try:
        result = x/y
        return result
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다")
    




# main function
def main():
    check = 1
    print("Welcome to calcuator")
    while check >= 1:        
        print("0: exit, 1: plus 2: minus 3: multiplication 4: division")
        try:
            check = int(input())
            if check == 1:
                print("First Number")
                x = float(input())
                print("Second Number")
                y = float(input())
                print("answer : ", plus(x,y))
            elif check == 2:
                print("First Number")
                x = float(input())
                print("Second Number")
                y = float(input())
                print("answer : ", minus(x,y))
            elif check == 3:
                print("First Number")
                x = float(input())
                print("Second Number")
                y = float(input())
                print("answer : ", multiplication(x,y))
            elif check == 4:
                print("First Number")
                x = float(input())
                print("Second Number")
                y = float(input())
                print("answer : ", division(x,y))
            elif check > 4 or check < 0:
                print("Unsupported")
            else:
                print("Thank you")
        except ValueError:
            print("제대로 된 숫자를 입력하세요")
            
                

if __name__ == "__main__":
    main()
