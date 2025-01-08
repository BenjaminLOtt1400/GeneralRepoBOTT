entered_age = int(input())

while (entered_age < 18 or entered_age > 65):
    if entered_age < 18:
        print('20% discount')
    else:
         print('15% discount')
    entered_age = int(input())

print('No discount')