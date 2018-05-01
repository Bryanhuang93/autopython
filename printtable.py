# printtable.py - Practice Project for Chapter 6

tableData = [
    ['apples','oranges','cherries','banana'],
    ['Alice','Bob','Carol','David'],
    ['dogs','cats','moose','goose']
]

colwidth = len(tableData)
rowwidth = len(tableData[0])

maxlen = []
for col in tableData:
    maxlen.append(max(map(len,col)))

for i in range(rowwidth):
    temp = ''
    for j in range(colwidth):
        temp = temp + ' '+tableData[j][i].rjust(maxlen[j])
    print(temp)
