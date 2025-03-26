# how does string concatenation works
# we want to create a stirng that says "My favourite actress is _______________"
# we would create a stirng variable
# actress = "Lee Joo Young"

# ways to do strng concatenation
# print("My favourite actress is " + actress)
# print("My favourite actress is {}".format(actress))
# print(f"My favourite actress is {actress}")


place = input("A Place: ")
adjective = input("An adjective: ")
animal = input("An animal: ")
noun = input("A Noun: ")
verb = input("A Verb: ")

madlib1 = f"I was walking to the {place} when I saw a {adjective} {animal}.\
It was holding a {noun} and started to {verb}!"

print(madlib1)
