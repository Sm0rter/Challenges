# Variables
list1 = []


# Functions
def c_p(a, common, iterations):
    false = False
    comparer = a[0][iterations]
    print(comparer)
    for i in range(1, len(a)):
        subject = a[i]
        letter = subject[iterations]
        if len(subject) == iterations or len(comparer) == iterations:
            false = True
        if comparer != letter:
            return common
    if false == True:
        return (common + a[0][iterations])
    return(c_p(a, common + a[0][iterations], iterations + 1))



# Main Loop
while True:
    words = int(input("How many words do you want to check? "))
    for i in range(words):
        string = input("Insert word here: ")
        list1.append(string)
        iterations = 0
        common = ""
    common_p = c_p(list1, common, iterations)
    print(common_p)