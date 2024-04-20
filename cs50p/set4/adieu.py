import inflect 


list_names = []
ad = inflect.engine()

while True:
    try:
        name = input("Name: ")
        name = name.strip().title()
        list_names.append(name)
    except EOFError:
        print()
        print("Adieu, adieu, to", ad.join(list_names))
        break
    