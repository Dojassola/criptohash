while 1:
    a=""
    b=0
    c=0
    temp = []
    for i in str(input("ast: ")):
        if c < 1:
            temp.append(i)
            c+=1
        for x in temp:
            x=ord(x)<<32
        i=(ord(i)+x)<<32
        a+=str(i)
        b+=i
    print(a)
    print(str(b).encode().hex(), "B")
    b=str(b).encode().hex()
    hex_value = hex(int(b))[2:]
    print(hex_value, "HEX b")
    hex_value = hex(int(str(b).encode().hex()))[2:]
    print(hex_value, "HEX b2")
