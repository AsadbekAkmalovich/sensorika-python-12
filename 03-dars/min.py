# FIZZBUZZ
son = int(input("Sonni kiriting: "))
fizzbuzz = ""

if son % 3 == 0 and son % 5 == 0:
    fizzbuzz = "FIZZBUZZ" 
elif son % 3 == 0:
    fizzbuzz = "FIZZ"
elif son % 5 == 0:
    fizzbuzz = "BUZZ"

print(fizzbuzz)
