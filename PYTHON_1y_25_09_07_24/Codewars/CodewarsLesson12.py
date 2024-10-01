# Name:MakeUpperCase
# Write a function which converts the input string to uppercase.
def make_upper_case(s):
    return s.upper()
text = "Hello, World!"
print(make_upper_case(text))

# Name:Reversing words into string
# You need to write a function that reverses the words in a given string.
# Words are always separated by a single space.
# As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.
def reverse(st):
    st = st.split()
    st.reverse()
    return ' '.join(st)

# Name: Reversed Words
# Complete the solution so that it reverses all of the words within the string passed in.
# Words are separated by exactly one space and there are no leading or trailing spaces.
def reverseWords(s):
    return " ".join(s.split(" ")[::-1])
