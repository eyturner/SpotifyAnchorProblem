# Takes the string and places each char into a dictionary with its count. O(n)
def stringToDict(string):
    dict = {}
    for char in string:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

# Sorts the dictionary by value in ascending order. O(n*log(n))
def sortDictByVals(dict):
    return {k: val for k, val in sorted(dict.items(), key=lambda item: item[1])}
    
# Finds the unique set. O(n)
def findMaxSet(dict, strLength, minLength):
    dict = sortDictByVals(dict)
    finalSet = []
    for key in dict:
        if(strLength - dict[key] >= minLength):
            strLength -= dict[key]
            finalSet.append(key)
        else:
            return finalSet

# Main program. Runs in O(n*log(n))
def main():
    string = 'If you want to jumpstart the process of talking to us about this role, here’s a little challenge: write a program that outputs the largest unique set of characters that can be removed from this paragraph without letting its length drop below 50. For example: [‘H’, ‘i’, ‘!’, ‘ ’]'
    minLength = 50

    charDict = stringToDict(string)
    result = findMaxSet(charDict, len(string), minLength)
    print(result)


if __name__ == "__main__":
    main()
