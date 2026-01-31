# Q1
sentence = "Hello World"
counter = 0
for c in sentence:
    if(c in 'aeiouAEIOU'):
        counter += 1
print("Number of vowels:", counter)


# Q2
user_input = []
for i in range(5):
    value = input("Enter value {}: ".format(i+1))
    user_input.append(value)
user_input.sort()
print(user_input)
user_input.sort(reverse=True)
print(user_input)


# Q3
sentence = "iti shhdn ititi jdjditi ncnc iti"
words = sentence.split()
count = 0
for word in words:
    if word == "iti":
        count += 1
print(count)

#jdjditi is handled
sentence = "iti shhdn ititi jdjditi ncnc iti"
count = sentence.count("iti")
print(count)

#ititi is handled
sentence = "iti shhdn ititi jdjditi ncnc iti"
count = 0
for i in range(len(sentence)-2):
    if sentence[i:i+3] == "iti":
        count += 1
print(count)


# Q4
# O(n^2)
word = "Hello"
char_list = list(word)
for c in char_list:
    if c in 'aeiouAEIOU':
        char_list.remove(c)
word = ''.join(char_list)
print(word)

# O(n^2)
word = "Hello"
for c in word:
    if c in 'aeiouAEIOU':
        word = word.replace(c, '')
print(word)

# O(n)
word = "Hello"
mylist = []
for c in word:
    if c in 'aeiouAEIOU':
        continue
    mylist.append(c)
word = ''.join(mylist)
print(word)


# Q5
word = "Hii"
for i in range(len(word)):
    if word[i] == 'i':
        print(i)

# Q6
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i * j, end=" ")
    print()


# Q7
# O(n)
user_input = input("Enter a number: ")
if user_input.isdigit():
    n = int(user_input)
    for i in range(1, n + 1):
        print(' ' * (n-i) +'*' * i)