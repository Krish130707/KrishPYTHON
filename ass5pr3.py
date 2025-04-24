class NextPermutation:
    def __init__(self, word):
        self.word = word

    def find_next_permutation(self):
        #Convert the word to a list of characters 
        word = list(self.word)
        n = len(word)
        #Find first character from the right that is smaller than its next character
        i = n - 2
        while i >= 0 and word[i] >= word[i + 1]:
            i -= 1

        #If no pivot is found, the word is in descending order
        if i == -1:
            return "no answer"

        #Find the smallest character to the right of the pivot that is larger than the pivot
        j = n - 1
        while word[j] <= word[i]:
            j -= 1

        #Swap the pivot and the character found before
        word[i], word[j] = word[j], word[i]

        #Reverse the substring to the right of the pivot
        word = word[:i + 1] + word[i + 1:][::-1]
        #Join the list back into a string and return the result
        return ''.join(word)


#Reading inputs
t = int(input("Enter the number of test cases: "))
for _ in range(t):
    w = input("Enter the word: ")
    #Create an object of the NextPermutation class
    permutation_finder = NextPermutation(w)
    #Find and print the next permutation
    print(permutation_finder.find_next_permutation())

