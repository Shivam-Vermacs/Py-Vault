def madlib():
    place = input("A Place: ")
    adjective1 = input("An Adjective: ")
    adjective2 = input("Another Adjective: ")
    noun1 = input("A Noun: ")
    verb1 = input("A Verb Ending in -ing: ")
    sound = input("A Sound: ")
    verb2 = input("Another Verb: ")
    noun2 = input("Another Noun: ")

    madlib = f"Deep in the {place}, a {adjective1} monster lurked. Its {adjective2} eyes \
glowed as it clutched a {noun1}. It started {verb1} loudly, making a terrifying {sound}. \
I tried to {verb2}, but it threw the {noun2} at me! That was the last thing I remember before darkness consumed me."

    print(madlib)
