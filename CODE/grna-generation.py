import openpyxl

# Чтение исходного файла
new = str()
guides = {}
input_file = r'C:\Users\dolsk\Desktop\WORK\gRNA for ZIM3\SDC1 and ACTN4.txt'
output_file = input_file.replace('gRNA_for_ZIM3', 'READY_MADE_gRNA_for_ZIM3').replace('.txt', '.xlsx')

with open(input_file) as f:
    list_guides = f.read().rstrip().split()
for i in range(1, len(list_guides), 2):
    guides[list_guides[i - 1]] = list_guides[i]

# Создание нового файла Excel
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "gRNA Data"

# Запись данных в Excel
for key, value in guides.items():
    oligo1 = 'cacc' + value
    new = ''
    for i in value.upper():
        if i == 'T':
            new += 'A'
        elif i == 'A':
            new += 'T'
        elif i == 'C':
            new += 'G'
        elif i == 'G':
            new += 'C'
    oligo2 = 'aaac' + new[::-1]
    
    # Запись Key и Oligo1
    ws.append([key+'_oligo1', oligo1])
    # Запись Key и Oligo2 на следующей строке
    ws.append([key+'_oligo2', oligo2])

# Сохранение файла Excel
wb.save(output_file)

print(f'Data saved to {output_file}')
