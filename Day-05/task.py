# m1: Check if a number is Armstrong
def isArmstrong(n):
    num_str = str(n)
    power = len(num_str)
    total = sum(int(digit) ** power for digit in num_str)
    return total == n

# m2: Count vowels in a string
def countVowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

# m3: Simulate simple login
def loginSystem(username, password):
    if username == "User" and password == "pass":
        return "Login Successful!"
    return "Login Failed!"

# m4: Simulate logout
def logoutSystem():
    return "You have logged out successfully."

# m5: Check if a word is uppercase
def isUpper(word):
    return word.isupper()

# m6: Check if a word is lowercase
def isLower(word):
    return word.islower()

# m7: Reverse a list
def reverseList(lst):
    return lst[::-1]

# m8: Merge two lists
def mergeLists(lst1, lst2):
    return lst1 + lst2

# m9: Count occurrences of an item in a list
def countItem(lst, item):
    return lst.count(item)

# m10: Simple password verification
def verifyPassword(password):
    correct = "1234"
    return password == correct