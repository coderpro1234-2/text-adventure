import os
def clearscreen():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")
room = "Hallway 4"
items = []
rwitems = ["Study 1", "Bedroom", "Greenhouse", "Garage Closet"]
grabitems = {"Study 1": "Bedroom Door Key", "Bedroom": "Garden Key", "Greenhouse": "Garage Door Key", "Garage Closet": "Front Door Key"}
locked = {"Bedroom": "Bedroom Door Key", "Garden 6": "Garden Key", "Garage 4": "Garage Door Key", "Exit": "Front Door Key"}
lockuse = {"Hallway 2": "Bedroom", "Living Room 1": "Garden 6", "Hallway 1": "Garage 4", "Front Hall": "Exit"}
drawscreen = """
                             ------
                            |Garage|⬅ Front Door Key
                            |Closet|
                      ------ ------
                     | Gara | Gara |
                     | ge 1 | ge 2 |
                      ------ ------
                     | Gara | Gara | Needs Garage Door Key
                     | ge 3 | ge 4 |↙
                      ------ -Door-        ------
   Needs Bedroom Door Key   |Hallw-|      | Stud |⬅ Bedroom Door Key
                   ↘        | ay 1 |      | -y 1 |
               ------ ------ ------ ------ ------
              | Bedr |Hallw-|Hallw-|Hallw-| Stud |
 Garden Key → | -oom | ay 2 | ay 3 | ay 4 | -y 2 |
 ------        ------ ------ ------ ------ ------
|Green | <- Garage Door Key        |Hallw-|
| house|                           | ay 5 |
 ------ ------ ------               ------
| Gard | Gard | Gard |             |Hallw-|      Needs Front Door Key
| en 1 | en 2 | en 3 |             | ay 6 |      ⬇
 ------ ------ ------ ------ ------ ------ ------ ------
| Gard | Gard | Gard |Living|Living|Living| Fron | Exit |
| en 4 | en 5 | en 6 |Room 1|Room 2|Room 3|t Hall|      |
 ------ ------ ------ ------ ------ ------ ------ ------
                    ↗|Dining|Dining|
    Needs Garden Key |Room 1|Room 2|
                      ------ ------ ------ ------ ------
                     |Dining|Dining| Kit- |Lounge|Lounge|
                     |Room 3|Room 4| chen |Room 1|Room 2|
                      ------ ------ ------ ------ ------
"""
def allmoves(room):
  moves = {"Garage 1": ["down", "right"], "Garage 2": ["up", "down", "left"], "Garage 3": ["up", "right"], "Garage 4": ["up", "down", "left"], "Hallway 1": ["up", "down"], "Hallway 2": ["left", "right"], "Hallway 3": ["up", "left", "right"], "Hallway 4": ["down", "left", "right"], "Hallway 5": ["up", "down"], "Hallway 6": ["up", "down"], "Study 1": ["down"], "Study 2": ["up", "left"], "Bedroom": ["right"], "Living Room 1": ["down", "left", "right"], "Living Room 2": ["down", "left", "right"], "Living Room 3": ["up", "left", "right"], "Front Hall": ["left", "right"], "Dining Room 1": ["up", "down", "right"], "Dining Room 2": ["up", "down", "left"], "Dining Room 3": ["up", "right"], "Dining Room 4": ["up", "left", "right"], "Kitchen": ["left", "right"], "Lounge Room 1": ["left", "right"], "Lounge Room 2": ["left"], "Greenhouse": ["down"], "Garden 1": ["up", "down", "right"], "Garden 2": ["down", "left", "right"], "Garden 3": ["down", "left"], "Garden 4": ["up", "right"], "Garden 5": ["up", "left", "right"], "Garden 6": ["up", "left", "right"], "Garage Closet": ["down"]}
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
  moves = {"Garage 1": ["down", "right"], "Garage 2": ["up", "down", "left"], "Garage 3": ["up", "right"], "Garage 4": ["up", "down", "left"], "Hallway 1": ["up", "down"], "Hallway 2": ["left", "right"], "Hallway 3": ["up", "left", "right"], "Hallway 4": ["down", "left", "right"], "Hallway 5": ["up", "down"], "Hallway 6": ["up", "down"], "Study 1": ["down"], "Study 2": ["up", "left"], "Bedroom": ["right"], "Living Room 1": ["down", "left", "right"], "Living Room 2": ["down", "left", "right"], "Living Room 3": ["up", "left", "right"], "Front Hall": ["left", "right"], "Dining Room 1": ["up", "down", "right"], "Dining Room 2": ["up", "down", "left"], "Dining Room 3": ["up", "right"], "Dining Room 4": ["up", "left", "right"], "Kitchen": ["left", "right"], "Lounge Room 1": ["left", "right"], "Lounge Room 2": ["left"], "Greenhouse": ["down"], "Garden 1": ["up", "down", "right"], "Garden 2": ["down", "left", "right"], "Garden 3": ["down", "left"], "Garden 4": ["up", "right"], "Garden 5": ["up", "left", "right"], "Garden 6": ["up", "left", "right"], "Garage Closet": ["down"]}
  moveb = {"Garage 1": ["Garage 3", "Garage 2"], "Garage 2": ["Garage Closet", "Garage 4", "Garage 1"], "Garage 3": ["Garage 1", "Garage 4"], "Garage 4": ["Garage 2", "Hallway 1", "Garage 3"], "Hallway 1": ["Garage 4", "Hallway 3"], "Hallway 2": ["Bedroom", "Hallway 3"], "Hallway 3": ["Hallway 1", "Hallway 2", "Hallway 4"], "Hallway 4": ["Hallway 5", "Hallway 3", "Study 2"], "Hallway 5": ["Hallway 4", "Hallway 6"], "Hallway 6": ["Hallway 5", "Living Room 3"], "Study 1": ["Study 2"], "Study 2": ["Study 1", "Hallway 4"], "Bedroom": ["Hallway 2"], "Living Room 1": ["Dining Room 1", "Garden 6", "Living Room 2"], "Living Room 2": ["Dining Room 2", "Living Room 1", "Living Room 3"], "Living Room 3": ["Hallway 6", "Living Room 2", "Front Hall"], "Front Hall": ["Living Room 3", "Exit"], "Dining Room 1": ["Living Room 1", "Dining Room 3", "Dining Room 2"], "Dining Room 2": ["Living Room 2", "Dining Room 4", "Dining Room 1"], "Dining Room 3": ["Dining Room 1", "Dining Room 4"], "Dining Room 4": ["Dining Room 2", "Dining Room 3", "Kitchen"], "Kitchen": ["Dining Room 4", "Lounge Room 1"], "Lounge Room 1": ["Kitchen", "Lounge Room 2"], "Lounge Room 2": ["Lounge Room 1"], "Greenhouse": ["Garden 1"], "Garden 1": ["Greenhouse", "Garden 4", "Garden 2"], "Garden 2": ["Garden 5", "Garden 1", "Garden 3"], "Garden 3": ["Garden 6", "Garden 2"], "Garden 4": ["Garden 1", "Garden 5"], "Garden 5": ["Garden 2", "Garden 4", "Garden 6"], "Garden 6": ["Garden 3", "Garden 5", "Living Room 1"], "Garage Closet": ["Garage 2"]}
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