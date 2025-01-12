while 1:
    try:
            
        N = input()
        print(bytearray.fromhex(N).decode())
    except EOFError:
        break
