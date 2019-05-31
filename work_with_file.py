with open('referat.txt') as f:
    content = f.read()
    print(len(content))
    print(len(content.split()))
    modify_text = content.replace('.', '!')
    with open('referat2.txt', 'w') as f2:
        f2.write(modify_text)