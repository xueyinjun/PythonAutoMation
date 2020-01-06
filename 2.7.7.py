#encoding = utf-8
while True:
    print('Who are you?')
    name = input('>')
    if name != 'Joe':
        continue
    print('Hello,Joe.What is the password?(It is a this.)')
    password = input('>')
    if password == 'swordfish':
        break

print('Access granted.') 