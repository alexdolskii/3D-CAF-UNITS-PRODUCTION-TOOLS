from statistics import mean
import math

def prGreen(prt):
    print(f"\033[92m{prt}\033[00m")


def prGreenwithout(prt):
    print(f"\033[92m{prt}\033[00m", end=' ')


def prRed(prt):
    print(f"\033[91m{prt}\033[00m")


def plates_wells(a):
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


a = input('hematocytometer four numbers: ')
b = a.split()
b = [int(i) for i in b]
prGreenwithout('Mean =')
print(mean(b))

dil = int(input('Please, enter dulution fold: '))
vol = int(input('Please, enter total volume of counted cells in ml: '))
total = mean(b)*dil*vol*(10000)
print('_________________________________________________________________________________________________________________')
print()
prGreen('According to the formula mean x dillution x volume x 10^4:')

total1 = total
i = 0
while total1 > 10:
    total1 = total1 // 10
    i += 1
prGreenwithout('Total amount of cells')
print(total/(10**6), '*10^6')
prGreenwithout('Concentration is: ')
print((total/vol)/(10**6), '*10^6')
print('_________________________________________________________________________________________________________________')
print()
plates = dict()
print('''Enter number of plates and wells in format 'plates wells'. After the end of the input enter 'done' ''')
plates_wells(a)

agree = 'n'
while agree != 'y':
    k6 = int(input('Enter total cell amount in 6 well plate (example: 500000):'))
    k24 = int(input('Enter total cell amount in 24 well plate (example: 150000):'))
    k48 = int(input('Enter total cell amount in 48 well plate: (example: 75000):'))
    print()
    print(f"6-well plate: {k6} cells/well, total volume 2 ml with concentration {k6/2}/ml")
    print(f"24-well plate: {k24} cells/well, total volume 500 mkl with concentration {k24*2}/ml")
    print(f"48-well plate: {k48} cells/well, total volume 250 mkl with concentration {k48*4}/ml")
    agree = input('Are you sure (y/n)? ')
    print()


aimvol = {}
aimcell = {}
for i in plates.keys():
    if i == 6:
        aimvol[6] = (math.ceil((plates[i]*2)*1.15))
        aimcell[6] = (math.ceil((plates[i]*2)*1.15))*(k6/2)
    elif i == 24:
        aimvol[24] = (math.ceil((plates[i]*0.5)*1.15))
        aimcell[24] = (math.ceil((plates[i]*0.5)*1.15))*(k24*2)
    elif i == 48:
        aimvol[48] = (math.ceil((plates[i]*0.25)*1.15))
        aimcell[48] = (math.ceil((plates[i]*0.25)*1.15))*(k48*4)
weneed = 0
for i in aimcell.keys():
    weneed = weneed + aimcell[i]

if weneed >= total:
    print('We have: ', total)
    print('We need: ', weneed)
    prRed('Cells is not enough')
else:
    print('_________________________________________________________________________________________________________________')

    print()
    prGreenwithout('We have')
    print(vol, end='')
    prGreenwithout(' ml of cells with the concentration ')
    print((total/vol)/(10**6), '*10^6.',  end='')
    prGreenwithout(' Total: ')
    print(total/(10**6), '*10^6')
    print()
    for i in plates.keys():
        if i == 6:
            prGreen('In case of 6 well plate')
            print('Concentration is: ', k6/2, 'cells/ml')
            print(round((aimvol[6]/((total/vol)/(k6/2))), 3), 'ml cells and', round((aimvol[6] -
                  aimvol[6]/((total/vol)/(k6/2))), 3), 'new DMEM.', aimvol[6], 'ml total. By 2 ml/well')
            print()
        elif i == 24:
            prGreen('In case of 24 well plate')
            print('Concentration is: ', int(k24*2), 'cells/ml')
            print(round((aimvol[24]/((total/vol)/(k24*2))), 3), 'ml cells and', round((aimvol[24] -
                aimvol[24]/((total/vol)/(k24*2))), 3), 'new DMEM.', aimvol[24], 'ml total. By 500 mkl/well')
            print()
        elif i == 48:
            prGreen('In case of 48 well plate')
            print('Concentration is: ', int(k48*4), 'cells/ml')
            print(round((aimvol[48]/((total/vol)/(k48*4))), 3), 'ml cells and', round((aimvol[48] -
                aimvol[48]/((total/vol)/(k48*4))), 3), 'new DMEM.', aimvol[48], 'ml total. By 250 mkl/well')
            print()
print('_________________________________________________________________________________________________________________')

