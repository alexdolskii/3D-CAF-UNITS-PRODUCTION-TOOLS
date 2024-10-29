import math
def prGreen(prt):
    print(f"\033[92m{prt}\033[00m")


def prGreenwithout(prt):
    print(f"\033[92m{prt}\033[00m", end=' ')


def prRed(prt):
    print(f"\033[91m{prt}\033[00m")

def plates_wells():
    answer = 'n'
    while answer != 'y':
        a = input()
        while a != 'done':
            a = a.split()
            if len(a) == 2:
                if int(a[0]) == 6 or int(a[0]) == 24 or int(a[0]) == 48:
                    plates[int(a[0])] = int(a[1])
                else:
                    prRed('Incorrect type of plates')
            else:
                prRed('Incorrect format plates wells')
            a = input()
        for key, value in plates.items():
            print('We have ', value, 'wells', 'in', key, 'well-plate format')
        answer = input('Are you sure (y/n)? ')


plates = dict()
print('''Enter number of plates and wells in format 'plates wells'. After the end of the input enter 'done' ''')
plates_wells()

print()

aimvol = {}

for i in plates.keys():
    if i == 6:
        aimvol[6] = (math.ceil((plates[i]*2)*1.10))
        
    elif i == 24:
        aimvol[24] = (math.ceil((plates[i]*0.5)*1.10))
        
    elif i == 48:
        aimvol[48] = (math.ceil((plates[i]*0.3)*1.10))
        
weneedvol = 0
for i in aimvol.keys():
    weneedvol = weneedvol + aimvol[i]

ascorbic = int(input('Please, ender amount of ascorbic acid powder in mg: '))
conc = int(input('Please, the concentration of solution you need in mkg/ml: '))
prGreenwithout('If you add 1 ml PBS, the concentration is: ')
print(ascorbic*1000, 'mkg/ml')
prGreenwithout('Add L-ascorbic acid')
print((weneedvol*1000/((ascorbic*1000)/conc)), 'mkl', end=' ')
prGreenwithout('and')
print(((weneedvol*1000)-((weneedvol*1000/((ascorbic*1000)/conc))))/1000, end=' ')
prGreen('ml of DMEM')


