#https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

def merge_the_tools(s, k):
    # Percorre s em blocos de tamanho k
    for i in range(0, len(s), k):
        substring = s[i:i + k]
        seen = set()
        result = []
        for ch in substring:
            if ch not in seen:
                seen.add(ch)
                result.append(ch)
        print(''.join(result))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
