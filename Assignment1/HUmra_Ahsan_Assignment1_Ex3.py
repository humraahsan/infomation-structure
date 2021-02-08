# Humra Ahsan
# Assignment1, Ex3

# Method1
def countVowels(s):
    vowels = "a", "e", "i", "o", "u"
    lowercase = s.lower()
    count_a = 0
    count_e = 0
    count_i = 0
    count_o = 0
    count_u = 0
    for i in range(len(s)):
        if s[i] == "a":
            count_a = count_a + 1
        if s[i] == "e":
            count_e = count_e + 1
        if s[i] == "i":
            count_i = count_i + 1
        if s[i] == "o":
            count_o = count_o + 1
        if s[i] == "u":
            count_u = count_u + 1
    print("a", count_a,'\n' "e", count_e,'\n' "i", count_i,'\n' "o", count_o,'\n' "u", count_u,'\n')


if __name__ == '__main__':
    s = "This is a book about Python programming"
    countVowels(s)

#Method2
# function definition
def countVowels(s):
    # create two lists
    vowels = ["a", "e", "i", "o", "u"]
    count = [0, 0, 0, 0, 0]
    # for every character in string, loop through vowels
    for i in range(len(vowels)):
        # loop through every character in string
        for j in range(len(s)):
            if s.lower()[j] == vowels[i]:
                count[i] = count[i] + 1
        print(vowels[i], count[i])

if __name__ == '__main__':
    s = "This is a book about Python programming."
    countVowels(s)


