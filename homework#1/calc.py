num1 = int(input())
num2 = int(input())
operator = input()

def calc():
 if operator == '+' :
     print(num1 + num2)

 elif operator == '-' :
     print(num1 - num2)

 elif operator == '*' :
     print(num1 * num2)

 elif operator == '/':
     print(num1 - num2)

 else:
     print('올바른 연산자를 입력하세요.')