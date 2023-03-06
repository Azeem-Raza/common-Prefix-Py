def longest_common_prefix(strs):#takes the list of strings
#checks if the strs is empty then it returns ""
    if not strs:
        return ""
#.sort method will sort the list of string which will group similar strings
    strs.sort()
    prefix = ""
#strs[0] is first word in string
#and strs[-1] is last one where i indecates the chars
    for i in range(len(strs[0])):
        if strs[0][i] == strs[-1][i]:
            prefix += strs[0][i]#if char matches then it will go to the next char
        else:
            break
    return prefix

strs = ["hello", "heaven", "heavy", "heat"]
print(longest_common_prefix(strs))  # Output: "he"


