def main():
    text = input("Enter text here: ")
    convert_text = convert(text)
    print(convert_text)

def convert(text):
    text1 = text.replace(":)", '🙂')
    text2 = text1.replace(":(", '🙁')
    return text2

main()

