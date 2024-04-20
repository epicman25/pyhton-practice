def convert(sentence:str):
    sentence = sentence.replace(':)','🙂')
    sentence = sentence.replace(':(','🙁')
    return sentence


if __name__ == '__main__':
    print(convert(input()))
