from bs4 import BeautifulSoup
import requests
import random

url = "https://type.fit/api/quotes"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
with open ('file.txt','w') as file:
    file.write(str(soup))

list = []
with open('file.txt') as f:
    line = f.readlines()
    list.append(line)

ls = []
quotelist = list[0]
for i in range(1,len(quotelist),1):
    if len(quotelist[i]) > 5:
        ls.append(quotelist[i])
    else:
        continue


def msg(rand_num):
    text = ls[rand_num][12:-2]
    author = ls[rand_num+1][4:]
    return f"{text}\n{author}"