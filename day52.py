n = int(input())
visible_box = []

while n > 0:
    a = input()

    tamanho = len(visible_box)
    enter = False

    for i in range(0,tamanho) :

        if visible_box[i][0] < a:
            visible_box[i] = (a, 'p')
            enter = True
            break
        elif visible_box[i][0] > a and visible_box[i][1] == '':
            visible_box[i] = (visible_box[i][0], 'p')
            enter = True
            break

    if not enter or tamanho == 0:
        visible_box.append((a, ''))

    n -= 1

print(len(visible_box))