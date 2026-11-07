
# solution of leetcode string problem-58 (length of last word)

'''
 we need to find the length of last word given in a string.
 string can be '     hello world' or 'hello   world     ', etc.
 best approach is to use '.strip()' function of clear out empty spaces,
 and '.split()' to split the array into subtrings and store it as a list.
 here i had a better solution by stripping the string then directly returning the 
 length of s.split()[-1] ( -1 is for last index, that means last word of the returned
 list from '.split()' function and we directly return it's length) 
'''

def lengthOfLastWord(s):
        s = s.strip()   # clearing empty white spaces
        return len(s.split()[-1])       # directly returning length of last word of the list that  
                                        # is returned by '.split()' function.
                                        
# this solution gives 0ms runtime speed and 12.28mb of memory usage.                                        