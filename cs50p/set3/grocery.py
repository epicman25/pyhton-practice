grocery = {}
while True:
    try:
        item = input()
        if item in grocery:
            grocery[item]+=1
        else:
            grocery[item] = 1
    except EOFError:
        sorted_grocery = {key:value for key,value in sorted(grocery.items())}
        for key in sorted_grocery:
            print(sorted_grocery[key],key.upper())
        break
        