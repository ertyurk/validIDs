from tridcheckerfunc import validTurkishId
from IBAN_check import checkIBAN



#   Correct IDs : 11111111110, 32311164652, IBAN: TR440006400000115210506992
# inCorrect IDs : 01111111111, 12312312333, IBAN: TR440006400000115210506991

print ("Validation")
print("What do you want to Validate?")
print("Type 1 for TurkishIdentyNumber")
print("Type 2 For IBAN")

ch = int(input())

if ch == 1 :

    print("Type Turkish ID;" )
    x = input()
    if validTurkishId(x) == True:
        print("correct!")
    else:
        print("incorrect!")
elif ch == 2 :
    print("Type IBAN")
    y = input()
    if checkIBAN(y) == True:
        print("correct!")
    else:
        print("incorrect!")
