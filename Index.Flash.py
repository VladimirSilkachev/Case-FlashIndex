"""Case-study #3 Анализ текста
Разработчики:
Силкачев В.В. 37% Попов К.Б., Винников А.А. 35%

"""
from textblob import TextBlob
import local as lc

text = input(lc.enter)

sentens = text.split('. ')

count_sentens = len(sentens)
list_of_words = []
count_words = 0
for j in sentens:
    list_of_words = j.split(' ')
    count_words += len(list_of_words)
ASL = count_words / count_sentens

count_syllables = 0
list_1 = list('аиоеуэяыюёЁУЕЫАОЭЮИЯeyuioaEYUIOA')
for i in list_1:
    count_syllables += text.count(i)
ASW = count_syllables / count_words

FRE = 206.835 - (1.3 * ASL) - (60.1 * ASW)


print(lc.sent, count_sentens)
print(lc.words, count_words)
print(lc.syll, count_syllables)
print(lc.average_length_words, '{:.3f}'.format(ASL))
print(lc.aver_len_syllable, '{:.2f}'.format(ASW))
print(lc.flesh_index, FRE)
if FRE <= 25:
    print(lc.hard)
elif FRE <= 50:
    print(lc.average)
elif FRE <= 80:
    print(lc.easy)
else:
    print(lc.very_easy)

TextForBlob = TextBlob(text)
if TextForBlob.detect_language() == 'en':
    Ton = (TextForBlob.sentiment.polarity) * 100
    Sbj = TextForBlob.sentiment.subjectivity
    print(lc.obj, (1 - Sbj) * 100, '%')
    if Ton < 0:
        print(lc.negative)
    elif 0 < Ton < 50:
        print(lc.neutral)
    else:
        print(lc.positive)
