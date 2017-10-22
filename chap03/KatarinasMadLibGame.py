# Katarina's Mad Lib Game

print("MAD LIB GAME")
print("Enter answers to the following prompts\n")

person = input("Name of a famous person: ")
animal = input("Name of an animal: ")
place = input("A place: ")
attraction = input("Name of a tourist attraction: ")
group = input("Name of a group: ")
job = input("Name of a job: ")
disease = input("Name of disease: ")


story = "\nA famous person PERSON and a ANIMAL, went on\n" +\
        "a trip to PLACE." +\
        "There they saw the ATTRACTION. \n" +\
        "Their money were stolen by GROUP \n" +\
        "They had to get a job as JOB\n" +\
        "Since they were both suffering from DISEASE, they had to cut their\n" +\
        "trip short."

story = story.replace("PERSON", person)
story = story.replace("ANIMAL", animal)
story = story.replace("PLACE", place)
story = story.replace("ATTRACTION", attraction)
story = story.replace("GROUP", group)
story = story.replace("JOB", job)
story = story.replace("DISEASE", disease)


print(story)


