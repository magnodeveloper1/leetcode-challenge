#https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true

if __name__ == '__main__':
    s = input()
    chars = 'abcdefghijklmnopqrstuvwxyz'
    result = list()
    i = 0

    for ch in chars:
        count = s.count(ch)
        if count > 0:
            result.append((ch, count))
            i += 1

    for j in range(i):
        already_sorted = True
        for k in range(i - j - 1):
            if result[k][1] < result[k + 1][1]:
                result[k], result[k + 1] = result[k + 1], result[k]
                already_sorted = False
        if already_sorted:
            break
        
    print(result[0][0], result[0][1])
    print(result[1][0], result[1][1])
    print(result[2][0], result[2][1])