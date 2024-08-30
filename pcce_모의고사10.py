def solution(text, anagram, sw):
    list_text = ['0']*len(text)
    if sw == True :
        for i in range (len(anagram)):
            list_text[anagram[i]]= text[i]
    else :
        for i in range (len(anagram)):
            list_text[i]= text[anagram[i]]
    answer = ''.join(list_text)
    return answer