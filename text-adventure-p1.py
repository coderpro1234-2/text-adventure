import os
def clearscreen():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")
room = "Hallway 2"
items = []
rwitems = ["Closet 1", "Closet 2", "Closet 3"]
grabitems = {"Closet 1": "Garage Door Key", "Closet 2": "Gate Key", "Closet 3": "Laundry Key"}
locked = {"Closet 2": "Laundry Key", "Closet 3": "Garage Door Key", "Exit": "Gate Key"}
lockuse = {"Laundry": "Closet 2", "Garage 3": "Closet 3", "Garden 2": "Exit"}
drawscreen = """
                                    ------
                                   | Exit |
                                   |      |
 ------ ------               ------ -Gate- ⬅ Needs Gate Key
|Living|Living|             | Gard | Gard |
|Room 1|Room 2|             | en 1 | en 2 |
 ------ ------ ------ ------ ------ ------
|Living|Living| Kit- | Kit- | Gard | Gard |
|Room 3|Room 4|chen 1|chen 2| en 3 | en 4 |
 ------ ------ ------ ------ ------ ------
              |Hallw-|
              | ay 1 |
 ------ ------ ------ ------ ------ ------
| Bed- | Bed- |Hallw-|Hallw-|Hallw-| Laun |
|Room 1|Room 2| ay 2 | ay 3 | ay 4 | -dry |
 ------ ------ ------ ------ ------ -Door- ⬅ Needs Laundry Door Key
| Clos |      |Hallw-|             | Clos |
| et 1 |      | ay 5 |             | et 2 |⬅ Gate Key!
 ------        ------ ------        ------
   ↑          | Gara | Gara |
   Garage     | ge 1 | ge 2 |
   Door Key    ------ ------
              | Gara | Gara |
              | ge 3 | ge 4 |
    Needs    → -Door- ------
  Garage Key  | Clos |
              | et 3 |⬅ Laundry Door Key
               ------
"""
def allmoves(room):
  moves = {"Living Room 1": ["down", "right"], "Living Room 2": ["down", "left"], "Living Room 3": ["up", "right"], "Living Room 4": ["up", "left", "right"], "Kitchen 1": ["down", "left", "right"], "Kitchen 2": ["left", "right"], "Garden 1": ["down", "right"], "Garden 2": ["up", "down", "left"], "Garden 3": ["up", "left", "right"], "Garden 4": ["up", "left"], "Hallway 1": ["up", "down"], "Hallway 2": ["up", "down", "left", "right"], "Hallway 3": ["left", "right"], "Hallway 4": ["left", "right"], "Hallway 5": ["up", "down"], "Laundry": ["down", "left"], "Closet 2": ["up"], "Bedroom": ["down", "right"], "Bedroom 2": ["left", "right"], "Closet 1": ["up"], "Garage 1": ["up", "down", "right"], "Garage 2": ["down", "left"], "Garage 3": ["up", "down", "right"], "Garage 4": ["up", "left"], "Closet 3": ["up"]}
  tmp = ' '.join([str(elem)+"," for elem in moves[room]])
  return(tmp.strip(", "))
def moveplayer(room, dir):
  movesava = ["up", "down", "left", "right"]
  if dir == "use":
    try:
      if lockuse[room] != "":
        if items.count(locked[lockuse[room]]) > 0:
          items.remove(locked[lockuse[room]])
          locked.pop(lockuse[room])
          lockuse.pop(room)
        else:
          print("You do not have that item yet.")
          return(room)
    except:
      print("you cannot run `use` here.")
    return(room)
  if dir == "grab":
    if rwitems.count(room) != 0:
      rwitems.remove(room)
      items.append(grabitems[room])
    else:
      print("you cannot run `grab` here, there is nothing to grab.")
    return(room)
  moves = {"Living Room 1": ["down", "right"], "Living Room 2": ["down", "left"], "Living Room 3": ["up", "right"], "Living Room 4": ["up", "left", "right"], "Kitchen 1": ["down", "left", "right"], "Kitchen 2": ["left", "right"], "Garden 1": ["down", "right"], "Garden 2": ["up", "down", "left"], "Garden 3": ["up", "left", "right"], "Garden 4": ["up", "left"], "Hallway 1": ["up", "down"], "Hallway 2": ["up", "down", "left", "right"], "Hallway 3": ["left", "right"], "Hallway 4": ["left", "right"], "Hallway 5": ["up", "down"], "Laundry": ["down", "left"], "Closet 2": ["up"], "Bedroom": ["down", "right"], "Bedroom 2": ["left", "right"], "Closet 1": ["up"], "Garage 1": ["up", "down", "right"], "Garage 2": ["down", "left"], "Garage 3": ["up", "down", "right"], "Garage 4": ["up", "left"], "Closet 3": ["up"]}
  moveb = {"Living Room 1": ["Living Room 3", "Living Room 2"], "Living Room 2": ["Living Room 4", "Living Room 1"], "Living Room 3": ["Living Room 1", "Living Room 4"], "Living Room 4": ["Living Room 2", "Living Room 3", "Kitchen 1"], "Kitchen 1": ["Hallway 1", "Living Room 4", "Kitchen 2"], "Kitchen 2": ["Kitchen 1", "Garden 3"], "Garden 1": ["Garden 3", "Garden 2"], "Garden 2": ["Exit", "Garden 4", "Garden 1"], "Garden 3": ["Garden 1", "Kitchen 2", "Garden 4"], "Garden 4": ["Garden 2", "Garden 3"], "Hallway 1": ["Kitchen 1", "Hallway 2"], "Hallway 2": ["Hallway 1", "Hallway 5", "Bedroom 2", "Hallway 3"], "Hallway 3": ["Hallway 2", "Hallway 4"], "Hallway 4": ["Hallway 3", "Laundry"], "Hallway 5": ["Hallway 2", "Garage 1"], "Laundry": ["Closet 2", "Hallway 4"], "Closet 2": ["Laundry"], "Bedroom": ["Closet 1", "Bedroom 2"], "Bedroom 2": ["Bedroom", "Hallway 2"], "Closet 1": ["Bedroom"], "Garage 1": ["Hallway 5", "Garage 3", "Garage 2"], "Garage 2": ["Garage 4", "Garage 1"], "Garage 3": ["Garage 1", "Closet 3", "Garage 4"], "Garage 4": ["Garage 2", "Garage 3"], "Closet 3": ["Garage 3"]}
  tmp1 = moves[room]
  tmp11 = moveb[room]
  try:
    tmp12 = tmp11[tmp1.index(dir)]
  except:
    if movesava.count(dir) > 0:
      print("You cannot move in this direction.")
    else:
      print("You cannot run command `"+dir+"`.")
    return(room)
  try:
    if locked[tmp12] != "":
      print("This room is locked.")
      return(room)
  except:
    return(tmp12)
clearscreen()
while True:
  if room == "Exit":
    print("Well Done! You Escaped.")
    exit()
  print("You are currently at "+room+".")
  if items == []:
    print("You currently have nothing in your inventory.")
  else:
    print("Your current inventory is: "+(' '.join([str(elem)+"," for elem in items]).strip(", "))+".")
  print(drawscreen)
  if rwitems.count(room) != 0:
    print("This room has "+grabitems[rwitems[rwitems.index(room)]]+" in it, type 'grab' to grab the item.")
  try:
    if lockuse[room] != "":
      print("To gain access to "+lockuse[room]+", you need the "+locked[lockuse[room]]+". type 'use' to use the item.")
  except:
    speling = "bad :("
  print("The current moves direction you can move are: "+allmoves(room))
  inp = input("What is your move? ").lower()
  clearscreen()
  room = moveplayer(room, inp)