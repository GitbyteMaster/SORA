import scratchattach as scratch3
import random

capschar = "QWERTYUIOPASDFGHJKLZXCVBNM"
rawchar = "qwertyuiopasdfghjklzxcvbnm[]\{}|-=_+;\':\",./<>?~`1234567890!@#$%^&*() \t"
currentchar = rawchar

def encode(text):
  encode = ""
  for x in text:
    char = x
    if char in capschar:
      char = currentchar[capschar.index(char)]
    loc = currentchar.index(char)
    if not len(str(loc)) == 2:
      encode = f"{encode}0"
    encode = f"{encode}{str(loc)}"
  return encode

def decode(text):
  n = -2
  decode = ""
  while not len(decode) == len(text)/2:
    n += 2
    curr = f"{text[n]}{text[n+1]}"
    decode = f"{decode}{currentchar[int(curr)]}"
  return decode

account = ""
def login(username, password):
  global account
  account = scratch3.login(username, password)

def shuffle():
  limit = len(rawchar)
  newkey = ""
  newchars = []
  suggest = 0
  while not len(newchars) == limit:
    suggest = random.randint(0, limit-1)
    char = ""
    if not len(str(suggest)) == 2:
      char = "0"
    char = f"{char}{str(suggest)}"
    if not char in newchars:
      newchars.append(char)
  for x in newchars:
    newkey = f"{newkey}{x}"
  return newkey

def updatechar():
  shuffled = shuffle()
  conn = account.connect_cloud(929963862)
  conn.set_var("key", int(shuffled))
  currentchar = decode(scratch3.get_var("929963862", "key"))
