list = []

with (open("./Input/Names/invited_names.txt", 'r')) as file:
    for line in file:
        list.append(line.strip())

with (open("./Input/Letters/starting_letter.txt", 'r')) as file:
    letter = file.read()
    for name in list:
        with (open(f"./Output/ReadyToSend/letter_for_{name}.txt", 'w')) as file:
            file.write(letter.replace("[name]", name))
