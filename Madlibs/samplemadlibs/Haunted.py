def madlib():
    place = input("A Place: ")
    adjective1 = input("An Adjective: ")
    verb1 = input("A Verb: ")
    noun1 = input("A Noun: ")
    verb2 = input("Another Verb: ")
    adjective2 = input("Another Adjective: ")
    noun2 = input("Another Noun: ")
    verb3 = input("Another Verb Ending in -ing: ")

    madlib4 = f"Everyone warned me not to enter the {adjective1} house at the edge of {place}, \
but I couldnt resist. As soon as I {verb1} inside, the door slammed shut, and a {noun1} fell from the ceiling. \
I tried to {verb2}, but the {adjective2} whispers of a {noun2} filled the air. \
Now Im stuck here, {verb3} for someone to find me."

    print(madlib4)
