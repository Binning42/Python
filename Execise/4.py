h = float(input("Height="))
w = float(input("Weight="))
bmi = w / pow(h, 2)
if bmi > 32:
    print('terrible heavy')
elif bmi < 18.5:
    print('underweight')
elif bmi <= 25:
    print('normal')
elif bmi <=28:
    print('heavy')
elif bmi <=32:
    print('too heavy')