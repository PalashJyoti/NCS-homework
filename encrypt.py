msg = str(input("Enter the message: "))


def encrypt(m):
    emsg=''
    for i in m:
        if i != ' ':
            emsg += chr(ord(i) + 2)
        else:
            emsg += i
    return emsg


print(f'Original message: {msg}')
print(f'Encrypted msg: {encrypt(msg)}')
