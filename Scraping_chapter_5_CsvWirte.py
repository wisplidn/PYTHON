import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html, "html.parser")
#The main comparison table is currently the first table on the page
table = bsObj.findAll("table",{"class":"wikitable"})[0]
rows=table.findAll('tr')
print('成功解析网页，尝试打开文件.')

with open('1.csv','wt',encoding='utf-8',newline='') as f:
    print('成功打开文件，尝试写入.')
    write=csv.writer(f)
    for row in rows:
        csvRow=[]
        for cell in row.findAll(['td','th']):
            csvRow.append(cell.get_text())
            print('正在录入单元格',cell)
        write.writerow(csvRow)
        print('成功写入行',csvRow)
