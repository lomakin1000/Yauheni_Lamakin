# Дан текст и некоторый набор стоп слов. Надо извлечь из текста слова, удалив знаки препинания и стоп-слова в одну строку

stopwords = {'и', 'из', 'под', 'а', 'о', 'у', 'их',}

text = 'Дан текст и некоторый набор стоп слов. Надо извлечь из текста слова, удалив знаки препинания и стоп-слова.'

symbols = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
for symbol in symbols:
    if symbol in text:
        text = text.replace(symbol, "")
words = [word for word in text.split(
) if word not in stopwords and word.isalnum() == True]
print(" ".join(words))













