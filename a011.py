while True:
    try:
        sentence = str(input())
    except EOFError:
        break
    newstring = ""

    for i in range(0, len(sentence)):
        if sentence[i].isspace() or sentence[i].isalpha():
            newstring += sentence[i]
        else:
            newstring += " "

    word_count = newstring.split()
    print(len(word_count))