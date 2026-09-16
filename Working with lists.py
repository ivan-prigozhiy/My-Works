A=[50, True, 'Google', 1.23]
print(A)
A.extend(['CHATGPT', 34])
print(A)

smb = A.pop(2)
print(smb)

A.insert(1, 'Meta')
print(A)

A.remove('CHATGPT')
print(A)

B = 'Hello World'
print(B)

A.append(B)
print(A)

print(A)