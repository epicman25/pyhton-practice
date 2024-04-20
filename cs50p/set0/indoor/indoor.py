def to_lowercase(sentence : str):
    return sentence.lower()

def main(sentence):
    return to_lowercase(sentence)


if __name__ == '__main__':
    print(main(input()))
