import task as t

# m1: Armstrong check
print(t.isArmstrong(153))        # True

# m2: Count vowels in a string
print(t.countVowels("Hello World"))  # 3

# m3: Simulate simple login
print(t.loginSystem("User","pass"))  # Login Successful!

# m4: Simulate logout
print(t.logoutSystem())              # You have logged out successfully.

# m5: Check if a word is uppercase
print(t.isUpper("HELLO"))            # True

# m6: Check if a word is lowercase
print(t.isLower("hello"))            # True

# m7: Reverse a list
print(t.reverseList([1,2,3,4,5]))    # [5,4,3,2,1]

# m8: Merge two lists
print(t.mergeLists([1,2,3],[4,5,6])) # [1,2,3,4,5,6]

# m9: Count occurrences of an item in a list
print(t.countItem([1,2,2,3,2,4],2))  # 3

# m10: Simple password verification
print(t.verifyPassword("1234"))      # True