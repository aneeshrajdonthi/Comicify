def subtitleSplit(file_path):
    res = []
    with open(file_path, 'r',encoding='utf-8-sig') as file:
        lines = file.read()

    alllines = (lines.split('\n\n'))

    for i in alllines:
        temp = []
        if(i==''):
            continue
        curr = i.split('\n')
        dialogueno = curr[0]
        time = curr[1]
        dialogue = ''.join(curr[2:]).strip('- ').split('- ')
        # print('{'+dialogueno+'}{'+time+'}{'+dialogue+'}')
        temp.append(dialogueno)
        temp.append(time)
        temp.append(dialogue)
        res.append(temp)
    return res

