import random

def gen_phrase(nouns, verbs, n):
    phrases = []
    for i in range(n):

        phrase_type = random.choice(["С-Г-С", "Г-С-С", "С-С-Г"])

        if phrase_type == "С-Г-С":
            phrase = f"{random.choice(nouns)} {random.choice(verbs)} {random.choice(nouns)}"
        elif phrase_type == "Г-С-С":
            phrase = f"{random.choice(verbs)} {random.choice(nouns)} {random.choice(nouns)}"
        elif phrase_type == "С-С-Г":
            phrase = f"{random.choice(nouns)} {random.choice(nouns)} {random.choice(verbs)}"

        phrases.append(phrase)

    return phrases


nouns = []
verbs = []

while True:
    print("Введите существительные (по одному на строку). Введите 'СТОП', чтобы закончить: ")
    word = input()
    if word == "СТОП":
        break
    nouns.append(word)
print("\nВвод существительных окончен\n")


while True:
    print("Введите глаголы (по одному на строку). Введите 'СТОП', чтобы закончить: ")
    word = input()
    if word == "СТОП":
        break
    verbs.append(word)
print("\nВвод глаголов окончен\n")


print("Сколько фраз нужно сгенерировать? ")
n = int(input())
if len(nouns) > 0 and len(verbs) > 0:
    phrases = gen_phrase(nouns, verbs, n)
else:
    print("Один из списков пуст")
print("\nСгенерированные фразы: \n")
for phrase in phrases:
    print(phrase)