#Basic Calculator
print("Wellcome to my calculator")
repeat= 'Y'

while repeat=='Y':
    num1 = float(input('Enter the 1st number: '))
    operator = input('''Enter which operation to do
         + -> addition,
         - -> subtraction,
         * -> multiplication,
         / -> division,
         // -> floor division,
         % -> modulus and
         ** -> power operator
         : ''')
    
    num2 = float(input('Enter the 2nd number: '))
    if operator == '+':
         answer = num1 + num2
         print(num1,' + ', num2, ' = ', answer)
    elif operator == '-':
         answer = num1 - num2
         print(num1,' - ', num2, ' = ', answer)
    elif operator == '*':
         answer = num1 * num2
         print(num1,' * ', num2, ' = ', answer)
    elif operator == '/':
         answer = num1 / num2
         print(num1,' / ', num2, ' = ', answer)
    elif operator == '//':
         answer = num1 // num2
         print(num1,' // ', num2, ' = ', answer)
    elif operator == '%':
         answer = num1 % num2
         print(num1,' % ', num2, ' = ', answer)
    elif operator == '**':
         answer = num1 ** num2
         print(num1,' ** ', num2, ' = ', answer)

    Next_calculation= input("Press 'Y' for another calculation and 'N' for Exit")

     
    if Next_calculation.upper()== 'Y':
       repeat = 'Y'

    elif Next_calculation.upper()== 'N':
       print("Thank you for using my Calculator")
       break
    else:
       print("you enter wrong key, Anyway bye Visit Again later")
        
