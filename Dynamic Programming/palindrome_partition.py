'''
String: Given a string s, partition s such that every substring of the partition is a palindrome in Python #1374

The initial idea will be to make partitions to generate substring and check if 
the substring generated out of the partition will be a palindrome. Partitioning 
means we would end up generating every substring and checking for palindrome at every step.
 Since this is a repetitive task being done again and again, at this point we should think of recursion. 
 The recursion continues until the entire string is exhausted. 
 After partitioning, every palindromic substring is inserted in a data structure 
 When the base case has reached the list of palindromes generated during that recursion call is 
 inserted in a vector of vectors/list of list.

'''


class Solution:
    def partition(self, s):
        res = []
        path = []


        def partitionHelper(index: int):
            if index == len(s):
                res.append(path[:])
                return
            for i in range(index, len(s)):
                if isPalindrome(s, index, i):
                    path.append(s[index:i + 1])
                    partitionHelper(i + 1)
                    path.pop()


        def isPalindrome(s: str, start: int, end: int) -> bool:
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True


        partitionHelper(0)
        return res




if __name__ == "__main__":
    s = "aabb"
    obj = Solution()
    ans = obj.partition(s)
    print("The Palindromic partitions are :-")
    print(" [ ", end="")
    for i in ans:
        print("[ ", end="")
        for j in i:
            print(j, end=" ")
        print("] ", end="")
    print("]")