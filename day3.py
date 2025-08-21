def merge_the_tools(string, k):

    n = len(string) // k
    
    for i in range(n):
        substr = string[i*k: (i+1)*k]
        index = 0
        total = len(substr)
        
        while True:
            
            if index == total:
                break
            
            found = substr.count(substr[index])
            
            if found > 1:
                substr = substr[:index+1] + substr[index+1:].replace(substr[index],'')
                total -= found-1
            
            index += 1
    
        print(substr)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)