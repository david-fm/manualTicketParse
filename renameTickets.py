import os

PATH = os.path.join(os.path.dirname(__file__), "Tickets")

# Take each jpg and change its name by it's counter 

for i, filename in enumerate(os.listdir(PATH)):
    file = os.path.join(PATH, filename)
    newName = os.path.join(PATH, str(i)+".jpg")
    os.rename(file, newName)