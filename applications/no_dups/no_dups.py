def no_dups(s):
    # Implement me.
    words = s.split()
    print(words)

    dups = {}
    sentence = ""
    for word in words:
        if word not in dups.keys():
            dups[word] = word
            sentence += word + " "
    sentence = sentence[:-1]
    return sentence


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
