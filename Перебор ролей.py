f1 = open('st.txt','r')
exname = f1.read()
f1.close()
from openpyxl import load_workbook
wb = load_workbook(exname, data_only=True)
sheet = wb.get_sheet_by_name('Роли')
it=0
role=[0,0,0,0,0,0,0,0,0,0,0,0]
for cellobj in sheet['A17' : 'A28']:
    for cell in cellobj:
        role[it]=cell.value
        it+=1
it=0
name=[0,0,0,0,0]
for cellobj in sheet['B16' : 'F16']:
    for cell in cellobj:
        name[it]=cell.value
        it+=1
it=0
a=[0,0,0,0,0,0,0,0,0,0,0,0]
for cellobj in sheet['B17' : 'B28']:
    for cell in cellobj:
        a[it]=cell.value
        it+=1
it=0
b=[0,0,0,0,0,0,0,0,0,0,0,0]
for cellobj in sheet['C17' : 'C28']:
    for cell in cellobj:
        b[it]=cell.value
        it+=1
it=0
c=[0,0,0,0,0,0,0,0,0,0,0,0]
for cellobj in sheet['D17' : 'D28']:
    for cell in cellobj:
        c[it]=cell.value
        it+=1
it=0
d=[0,0,0,0,0,0,0,0,0,0,0,0]
for cellobj in sheet['E17' : 'E28']:
    for cell in cellobj:
        d[it]=cell.value
        it+=1
it=0
e=[0,0,0,0,0,0,0,0,0,0,0,0]
for cellobj in sheet['F17' : 'F28']:
    for cell in cellobj:
        e[it]=cell.value
        it+=1
l12=len(a)
gs=0
gc=[0,0,0,0,0]
s=0
for i in range(l12):
    s=a[i]
    for j in range(l12):
        if j==i:
            continue
        s+=b[j]
        for k in range(l12):
            if k==j:
                continue
            if k==i:
                continue
            s+=c[k]
            for l in range(l12):
                if l==k:
                    continue
                if l==j:
                    continue
                if l==i:
                    continue
                s+=d[l]
                for m in range(l12):
                    if m==l:
                        continue
                    if m==k:
                        continue
                    if m==j:
                        continue
                    if m==i:
                        continue
                    s+=e[m]
                    if s>gs:
                        gs=s
                        gc=[i,j,k,l,m]
                    s-=e[m]
                s-=d[l]
            s-=c[k]
        s-=b[j]
    s-=a[i]    
dlg = 0
for itb in range(len(name)):
    dl = len(name[itb])
    if dl>dlg:
        dlg = dl
f2 = open('rfin.txt', 'w')
for ita in range(len(name)):
    f2.write(name[ita].ljust(dlg, " ") + ' = ' + role[gc[ita]])
    f2.write('\n')
f2.close()
    
