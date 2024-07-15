def kmpAlgorithm(word, pattern):
    n, m = len(word), len(pattern)
    mainIndex, patternIndex = 1, 0
    lps = [0] * m 
    while mainIndex < m:
        while mainIndex < m and pattern[mainIndex] == pattern[patternIndex]:
            lps[mainIndex] = patternIndex + 1 
            mainIndex += 1 
            patternIndex += 1 
        patternIndex = 0 
        mainIndex += 1 
 
    wordIndex, patternIndex = 0, 0 
    while wordIndex < n:
        if word[wordIndex] == pattern[patternIndex]:
            wordIndex += 1 
            patternIndex += 1 
            if patternIndex == m:
                return wordIndex - m 
        else:
            while patternIndex > 0 and word[wordIndex] == pattern[patternIndex]:
                patternIndex = lps[patternIndex]
            wordIndex += 1 
    return -1
 
 
 
 
 
 
 
word = "abcdpqrsabcdefabcder"
pattern = "abcdefabcd"
index = kmpAlgorithm(word, pattern)
if index == -1:
    print(pattern, "not found")
else:
    print(pattern, "found at index:", index)
