def check_spelling(etalon_words, sentence):
    errors = []
    words = sentence

    for word in words:
        is_error = True
        for etalon_word in etalon_words:
            if len(word) == len(etalon_word):
                diff_count = sum(1 for a, b in zip(word, etalon_word) if a != b)
                if diff_count <= 2:
                    is_error = False
                    break

        if is_error:
            errors.append(word)

    return errors


etalon_words = input().split()
sentence = input().split()

errors = check_spelling(etalon_words, sentence)
print(f"Слова с ошибками: {errors}")