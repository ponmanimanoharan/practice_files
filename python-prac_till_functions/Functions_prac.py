base_num = 123
def doubling(num):
    return(num*2)


print(doubling(base_num))
print("--------------")
al = "Green Fox"
def greet(al):
    return("Greetings, dear " + al)

print(greet(al))
print("--------------")
typo = "chinchill"

def append_a_func(t):
    return t + 'a'

print(append_a_func(typo))

print("--------------")

def sum(n):
    num = 0
    for i in range(1,n+1):
        num +=i
    return(num)
print(sum(9))

print("--------------")

def factorio(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return(fact)

print(factorio(2))

def print_param(*args):
    return(args)
print(print_param(1,"ponmani",23,4.56))

print("--------------")


def list_fun(n,l_n):
    if n in l_n:
        return l_n
    else:
        return []

print(list_fun(1, [1, 11, 34, 52, 61]))
print(list_fun(9, [1, 11, 34, 52, 61]))
print("--------------")

def uni(arr):
    arr = list(set(arr))
    return arr

print(uni([1, 11, 34, 11, 52, 61, 1, 34]))
print("--------------")

def anagram(word,re_word):
    if len(re_word) == len(word) and word == re_word[::-1]:
        return("true")
    else:
        return("False")

print(anagram("dog","god"))
print(anagram("green", "fox"))
print(anagram("fox", "fxo"))

print("--------------")


def palindrome_test(palindrome_string):
    if palindrome_string == "":
        return ""
    elif palindrome_string != "":
        palindrome_string += palindrome_string[::-1]
        return palindrome_string

print(palindrome_test("hello"))
print(palindrome_test("greenfox"))
print(palindrome_test("123"))
print(palindrome_test(""))

print("---------------")

def search_palindrome(palindrome_string):
    i = 0
    pali = []
    for x in range(0, len(palindrome_string)):
        text = palindrome_string[x:len(palindrome_string)]
        for i in range(0, len(text)):
            p_text = text[i::]
            j = 0
            for j in range(0, len(p_text)-1):
                print(p_text[0:-j])
                if palindrome_test(p_text[0:-j]):
                    if p_text[0:-j] != "":
                        pali.append(p_text[0:-j])
            return pali
print(search_palindrome("dog goat dad duck doodle never"))
print(search_palindrome("apple"))

print("---------------")

def bubble(taken_list):
    taken_list.sort()
    return taken_list

def advanced_bubble(b, is_descending):
    if b == is_descending:
        b = b.sort(reversed = True)
    return(b)


print(bubble([43, 12, 24, 9, 5]))
print(advanced_bubble([43, 12, 24, 9, 5], True))



# --------------------------------------------------
print("-----------------xxx------------------")






