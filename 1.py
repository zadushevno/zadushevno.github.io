import re
f = open('proceedings.txt', 'r', encoding="utf-8")
regex1 = '\[[0-9]*\]\s[A-Z].*'
text = f.read()
list_of_ref = []
list_of_ref = (re.findall(regex1, text)) #все ссылки с цифрами и авторами
f.close()
regex2 = ']\s[\w*\s]*[\.|,]' #ищется криво, но с душой
list_of_authors = []
for elem in list_of_ref:
    if re.findall(regex2, elem) != []:
        list_of_authors.append(re.findall(regex2, elem))
for st in list_of_authors:
    new_st = ''.join(st)
    print(new_st[1:])
