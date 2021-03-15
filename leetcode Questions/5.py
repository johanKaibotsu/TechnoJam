class Solution:
   def uniqueMorseRepresentations(self, words):
      morse_codes=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
      s=set()
      for word in words:
         temp=''
         for c in word:
            temp+=morse_codes[ord(c)-97]
         s.add(temp)
      return len(s)
ob = Solution()
n=int(input("No. of Words = "))
words=[str(j) for j in input().split()]
print(ob.uniqueMorseRepresentations(words))