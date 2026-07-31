bytes(4)
SmileyBytes = bytes('😊', 'utf-8')
SmileyBytes
print(SmileyBytes.decode('utf-8'))

SmileyBytes = bytearray('😊', 'utf-8')