# reverse string using recursion
# interview questions
# recursion
def reverse(string):
     if len(string)<=1:
        return string
     return reverse(string[1:]) + string[0]


print(reverse("she is the love of my life"))

