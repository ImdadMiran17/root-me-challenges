chamber = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
flag = ""
for i in chamber:
    flag += chr(i)

print(flag)

# from hex

chamber2 = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'
print(bytes.fromhex(chamber2))
print(bytes.fromhex(chamber2).decode('utf-8'))

# rootme challenge

chamber3 = '4C6520666C6167206465206365206368616C6C656E6765206573743A203261633337363438316165353436636436383964356239313237356433323465'
print(bytes.fromhex(chamber3))
print(bytes.fromhex(chamber3).decode('utf-8'))
