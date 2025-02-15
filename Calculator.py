import speech_recognition as s
import math
# Extreact number from text --------------------------------------:
def extreact_num_from_text(text):
    l=[]
    for w in text.split(' '):
        for e in w.split(','):
            try:
                if "+" in e:
                    l.append(complex(e))
                elif "." in e:
                    l.append(float(e))
                else:
                    l.append(int(e))
            except:
                pass
    return l

# Function section -------------------:
# Two Arguments function----------
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def power(a,b):
    return math.pow(a,b)
def log(a,b):
    try:
        return math.log(b,a)
    except ValueError:
        return "Plece provide a positive value."
def division(a,b):
    try:
        if a%b==0:
            return a//b
        else:
            return a/b
    except ZeroDivisionError:
        return "Division by zero is not allowed."
def modulus(a,b):
    try:
        return a%b
    except ZeroDivisionError:
        return ("Modulus by zero is not allowed.")
def lcm(a,b):
    try:
        if a<0 or b<0 or type(a)!=int or type(b)!=int:
            raise ValueError
        L=a if a>b else b
        while L<=a*b:
            if L%a==0 and L%b==0:
                return L
            L+=1
    except ValueError:
        return "LCM is typically defined for positive integers."
    except ZeroDivisionError:
        return "LCM is not defined for zero."
def hcf(a,b):
    try:
        if a<0 or b<0 or type(a)!=int or type(b)!=int:
            raise ValueError
        H=a if a<b else b
        while H>=0:
            if a%H==0 and b%H==0:
                return H
            H-=1
    except ValueError:
       return "HCF is typically defined for positive integers."
    except ZeroDivisionError:
        return "HCF is not defined for zero."

# One Argument function-------------------------:
def square_root(num):
    try:
       return math.sqrt(num)
    except ValueError:
        return "Plece provide a positive value."
def cube_root(num):
    if num < 0:
        return -math.pow(-num, 1/3)
    else:
        return math.pow(num, 1/3)
def factorial(num):
    try:
        if num<0 or type(num)!=int:
            raise ValueError
        else:
            return math.factorial(num)
    except ValueError:
        return "Input must be an Positive integer."
def square(num):
    try:
        if num <=0:
            raise ValueError
        return num**2
    except ValueError:
        return "Input must be an greater than ZERO."

def cube(num):
    try:
        if num <=0:
            raise ValueError
        return num**3
    except ValueError:
        return "Input must be an greater than ZERO."
        
def factors(num):
    try:
        if num<=0 or type(num)!=int:
            raise ValueError
        return [ i for i in range(1,num+1) if num%i==0]
    except ValueError:
        return "Input must be an Positive integer."

def binary(num):
    if num == 0:
        return "0"
    sign = "-" if num < 0 else ""
    num = abs(num)
    integer_part = int(num)
    fractional_part = num - integer_part

    binary_integer = bin(integer_part)[2:]

    binary_fraction = []
    while fractional_part and len(binary_fraction) < 10:
        fractional_part *= 2
        bit = int(fractional_part)
        binary_fraction.append(str(bit))
        fractional_part -= bit
    if binary_fraction:
        return f"{sign}{binary_integer}." + "".join(binary_fraction)
    else:
        return f"{sign}{binary_integer}"

def octal(n):
    is_negative = n < 0
    n = abs(n)
    integer_part = int(n)
    fractional_part = n - integer_part

    octal_integer = oct(integer_part)[2:] 

    octal_fraction = ""
    while fractional_part > 0 and len(octal_fraction) < 10: 
        fractional_part *= 8
        digit = int(fractional_part)
        octal_fraction += str(digit)
        fractional_part -= digit

    if octal_fraction:
        octal_result = f"{octal_integer}.{octal_fraction}"
    else:
        octal_result = octal_integer
    return f"-{octal_result}" if is_negative else octal_result

def hexa(n):
    try:
        if isinstance(n, float):  # Handling float numbers
            return float.hex(n).replace('0x', '')
        elif isinstance(n, int):  # Handling integers
            return hex(n).replace('0x', '').upper()
        else:
            raise ValueError 
    except ValueError:
        return "Input must be an integer or float."

def is_even(num):
    try:
        if type(num)!=int:
            raise ValueError
        return True if num%2==0 else False
    except ValueError:
        return "Input must be an integer."

def next_even(num):
    try:
        if type(num)!=int:
            raise TypeError
        num+=1
        while not is_even(num):
            num+=1
        return num
    except TypeError:
        return "Input must be an integer."
def evens(num):
    try:
        if num<=0 or type(num)!=int:
            raise ValueError
        elif num==1:
            return 2
        else:
            return [i for i in range(2,num*2+1,2)]
    except ValueError:
        return "Input must be an Positive integer."

def odds(num):
    try:
        if num <= 0 or type(num)!=int:
            raise ValueError
        elif num==1:
            return 1
        else:
            return [i for i in range(1,num*2,2)]
    except ValueError:
        return "Input must be an Positive integer."
def next_odd(num):
    try:
        if type(num)!=int:
            raise TypeError
        num+=1
        while not is_odd(num):
            num+=1
        return num
    except TypeError:
        return "Input must be an integer."
def is_odd(num):
    try:
        if type(num)!=int:
            raise ValueError
        return True if num%2!=0 else False
    except ValueError:
        return "Input must be an integer."

def is_prime(n):
    try:
        if type(n)!=int:
            raise ValueError
        return True if len([i for i in range(2,n) if n%i ==0])==0 else False
    except ValueError:
        return "Input must be an integer."
def next_prime(num):
    try:
        if type(num)!=int:
            raise TypeError
        num+=1
        while not is_prime(num):
            num+=1
        return num
    except TypeError:
        return "Input must be an integer."
def primes(num):
    try:
        if num<=0 or type(num)!=int:
            raise ValueError
        elif num==1:
            return 2;
        p,n=[],2
        while num:
            p.append(n)
            n=next_prime(n)
            num-=1
        return p
    except ValueError:
        return "Input must be an Positive integer."

def fibonaccis(num):
    try:
        if num<=0 or type(num)!=int:
            raise ValueError
        elif num==1:
            return 0
        l1,a,b=[],-1,1
        while num:
            l1.append(a+b)
            a,b=b,a+b
            num-=1
        return l1
    except ValueError:
        return "Input must be an Positive integer."

def next_fibonacci(num):
    try:
        if type(num)!=int:
            raise TypeError
        if num<0:
            return 0
        a,b=0,1
        while a<=num:
            a,b=b,a+b
        return a
    except TypeError:
        return "Input must be an integer."

def is_perfect_square(n):
    s = int(math.sqrt(n))
    return s*s == n
def is_fibonacci(n):
    try:
        if type(n)!=int:
            raise ValueError
        return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)
    except ValueError:
        return "Input must be an integer."

def table(num):
    try:
        if type(num)!=int:
            raise ValueError
        return [num*i for i in range(1,11)]
    except ValueError:
        return "Input must be an Positive integer."

def is_armstrong(num):
    try:
        if num<=0 or type(num)!=int:
            raise ValueError
        power = len(str(num))
        return num == sum(int(digit) ** power for digit in str(num))
    except ValueError:
        return "Input must be an positive integer."
def armstrongs(n):
    try:
        if n<=0 or type(n)!=int:
            raise ValueError
        if n==1:
            return 1
        num,l1=1,[]
        while n:
            if is_armstrong(num):
                l1.append(num)
                n-=1
            num += 1
        return l1
    except ValueError:
        return "Input must be an Positive integer."
def next_armstrong(num):
    try:
        if num<=0:
            return 1
        num+=1
        while not is_armstrong(num):
            num+=1
        return num
    except ValueError:
        return "Input must be an integer."

# Zero Argument function-----------------------:
def end():
    print("\n-----:Thank you for using Smart Calculator:-----")
    input("=>Press enter key to exit: ")
    exit()
def sorry():
    print("Ans: This instruction is beyond my ability.")

# Dictionary-----------------------:
operactions0={'CLOSE':end,'END':end,'TERMINATE':end,'EXIT':end,'QUIT':end,'FINISH':end}
operactions1={'FACTORIAL':factorial,'FACTOR':factors,'FACTORS':factors,'SQUARE':square,'CUBE':cube,
    'BINARY':binary,'DECIMALTOBINARY':binary,'DECIMAL_TO_BINARY':binary,'BINARYS':binary,'BIN':binary,
    'OCTAL':octal,'DECIMALTOOCTAL':octal,'DECIMAL_TO_OCTAL':octal,'OCTALS':octal,'OCT':octal,'HEX':hexa,
    'HEXA':hexa,'HEXADECIMAL':hexa,'DECIMALTOHEXADECIMAL':hexa,'DECIMAL_TO_HEXADECIMAL':hexa,'ISFIBONACCIS':is_fibonacci,'IS_FIBONACCIS':is_fibonacci,
    'HEXADECIMALS':hexa,'HEXA_DECIMAL':hexa,'EVEN':evens,'EVENS':evens,'ODD':odds,'ODDS':odds,'PRIME':primes,'PRIMES':primes,'ISFIBONACCI':is_fibonacci,'IS_FIBONACCI':is_fibonacci,
    'IS_PRIME':is_prime,'ISPRIME':is_prime,'ISEVEN':is_even,'IS_EVEN':is_even,'ISODD':is_odd,'IS_ODD':is_odd,'ISARMSTRONG':is_armstrong,'IS_ARMSTRONG':is_armstrong,
    'FIBONACCI':fibonaccis,'FIBONACCIS':fibonaccis,'FIBONACCI_SERIES':fibonaccis,'FIBONACCISERIES':fibonaccis,'FIBO':fibonaccis,
    'ARMSTRONG':armstrongs,'ARMSTRONGS':armstrongs,'TABLE':table,'TABLES':table,'SQUAREROOT':square_root,
    'SQUARE_ROOT':square_root,'CUBEROOT':cube_root,'CUBE_ROOT':cube_root,'NEXTEVEN':next_even,'NEXT_EVEN':next_even,
    'NEXTODD':next_odd,'NEXT_ODD':next_odd,'NEXTPRIME':next_prime,'NEXT_PRIME':next_prime,'NEXTFIBONACCISERIES':next_fibonacci,
    "NEXT_FIBONACCI_SERIES":next_fibonacci,"NEXTFIBO":next_fibonacci,'NEXTFIBONACCI':next_fibonacci,'NEXTFIBONACCIS':next_fibonacci,'NEXT_FIBONACCI':next_fibonacci,'NEXT_FIBONACCIS':next_fibonacci,'NEXTARMSTRONG':next_armstrong,'NEXT_ARMSTRONG':next_armstrong}
operactions2={'PLUS':addition,'ADD':addition,'ADDITION':addition,'SUM':addition,
    'MINUS':subtraction,'SUBTRACT':subtraction,'SUBTRACTION':subtraction,'DIFFERENCE':subtraction,'SUB':subtraction,
    'PRODUCT':multiplication,'MULTIPLY':multiplication,'MULTIPLICATION':multiplication,'MULTIPLE':multiplication,'MULTIPLIDE':multiplication,
    'DIVIDE':division,'DIVISION':division,'MODULE':modulus,'MODULUS':modulus,'LCM':lcm,'HCF':hcf,'POWER':power,'POW':power,'EXPONENT':power,'LOG':log}

# Main body--------------------------:
def main():
    print("\n-------:WELCOME TO THE SMART CALCULATOR:-------")
    while True:
        text=input("\nEnter some text:\n")
        for word in text.split(' '):
            if word.upper() in operactions2.keys():
                try:
                    l=extreact_num_from_text(text)
                    if len(l)==2:
                        r=operactions2[word.upper()](l[0],l[1])  #lambda expression
                        print("Ans:",r)
                    else:
                        s1="{} is typically defined for Two numbers."
                        print(s1.format(word.upper()))
                except:
                    print("Something is wrong, please retry.")
                finally:
                    break
            elif word.upper() in operactions1.keys():
                try:
                    l=extreact_num_from_text(text)
                    if len(l)==1:
                        r=operactions1[word.upper()](l[0])  #lambda expression
                        print("Ans:",r)
                    else:
                        s1="{} is typically defined for One number."
                        print(s1.format(word.upper()))
                except:
                    print("Something is wrong, please retry.")
                finally:
                    break
            elif word.upper() in operactions0.keys():
                operactions0[word.upper()]()
                break
        else:
            sorry()

if __name__=='__main__':
    main()