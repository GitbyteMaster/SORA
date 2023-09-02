import scratchattach as scratch3

session = scratch3.login("G_bite_Masters", "mypassboy333")

pid = "875134025"

char = "QWERTYUIOPASDFGHJKLZXCVBNM~!@#$%^&*()_+{}|:\"<>?qwertyuiopasdfghjklzxcvbnm`1234567890-=[]\;\',./ "
def encode(txt):
    n = -1
    nn = -1
    enc = ""
    while not n == len(txt)-1:
        n += 1
        nn = -1
        while not txt[n] == char[nn]:
            nn += 1
        nn += 1
        if len(str(nn)) == 1:
            enc = f"{enc}0"
        enc = f"{enc}{nn}"
    return enc
def decode(txt):
    n = 0
    dec = ""
    while not n == len(txt)-2:
        add = int(f"{txt[n]}{txt[n+1]}")
        dec = f"{dec}{char[add-1]}"
        n += 2
        
    return dec
conn = session.connect_cloud(pid)
while True:
    request = scratch3.get_var(pid, "DATA:requesttype")
    if int(request) != 0:
        if int(request) == 1:
            itm = scratch3.get_var(pid, "DATA:request/response")
            conn.set_var("DATA:request/response", encode(open(f"C:/Users/Boyz/Desktop/SORA/{decode(itm)}").read()))
            conn.set_var("DATA:requesttype", "0")
