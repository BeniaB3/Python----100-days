# age: int
# name: str
# height: float
# is_human: bool

def police_chcek(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_chcek(19):
    print("You may pass.")
else:
    print("Pay a fine.")
