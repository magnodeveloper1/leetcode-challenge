#https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true

def minion_game(s):
    vowels = set('AEIOU')
    kevin_score = 0
    stuart_score = 0
    n = len(s)
    for i, ch in enumerate(s):
        # substrings que começam em i: são (n - i) no total
        if ch in vowels:
            kevin_score += n - i
        else:
            stuart_score += n - i

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

# Exemplo de uso
if __name__ == '__main__':
    s = input().strip()
    minion_game(s)
