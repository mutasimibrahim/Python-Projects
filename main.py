from unicodedata import name


print("\nHello welcome to Mutasim's madLibs game. Have fun!\n")

Name = input("Name: ")
number = input("Age: ")
sport = input("Sport: ")

madlib = f"My name is {Name}. I am {number} years old. In my free time I like to play {sport}."
print(madlib)