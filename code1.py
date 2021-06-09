while 1:
    b=0
    c=0
    temp = []
    for i in str(input("ast: ")):
        if c < 1:
            temp.append(i)
            c+=1
        for x in temp:
            x=(ord(x)+ord(i))<<256
        i=(ord(i)+x)>>32
        b+=i
    b=str(b).encode().hex()[8:]
    print(b, "a")
    hex_value = hex(int(b))[2:]
    print(hex_value, "HEX b")
    hex_value = hex(int(str(b).encode().hex()))[2:]
    print(hex_value, "HEX b2")
