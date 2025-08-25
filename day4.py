#https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true

if __name__ == '__main__':
    s = input().strip()
    freq = {}

    # Contando manualmente
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    # Ordenando (-contagem, letra)
    top3 = sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:3]

    for char, count in top3:
        print(char, count)