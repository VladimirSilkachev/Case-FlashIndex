"""Case-study #3 Анализ текста
Разработчики:
Силкачев В.В., Попов К.Б., Винников А.А.

"""

text = input("Введите текст:")

sentens = text.split('. ')
count_sentens = len(sentens)
list_of_words = []
count_words = 0
for j in sentens:
    list_of_words = j.split(' ')
    count_words += len(list_of_words)
ASL = count_words / count_sentens

count_syllables = 0
list_1 = list('аиоеуэяыюёЁУЕЫАОЭЮИЯ')
for i in list_1:
    count_syllables += text.count(i)
ASW = count_syllables / count_words
FRE = 206.835 - (1.3 * ASL) - (60.1 * ASW)









print ('Предложений:',count_sentens)
print ('Слов:',count_words)
print ('Слогов:',count_syllables)
print ('Средняя длина предложения в словах:', '{:.3f}'.format(ASL))
print ('Средняя длина слова в слогах:','{:.2f}'.format(ASW))
print ('Индекс удобочитаемости Флеша:',FRE)
if FRE <= 25:
    print('Текст трудно читается (для выпускников ВУЗов).')
elif FRE <=50:
    print('Текст немного трудно читать (для студентов).')
elif FRE <= 80:
    print('Простой текст (для школьников).')
else:
    print('Текст очень легко читается (для младших школьников).')
