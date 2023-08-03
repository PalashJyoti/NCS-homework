emsg = str(input("Enter the encrypted message: "))


def decrypt(m):
    dmsg = ''
    for i in m:
        if i != ' ':
            dmsg += chr(ord(i) - 2)
        else:
            dmsg += i
    return dmsg


print(f'Encrypted message: {emsg}')
print(f'Decrypted msg: {decrypt(emsg)}')
