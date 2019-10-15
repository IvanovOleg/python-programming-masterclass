# with open("C:\\Users\\dlj\\Documents\\python-programming-masterclass\\Fileio\\binary", 'bw') as binary_write_file:
#     for i in range(17):
#         binary_write_file.write(bytes([i]))

# with open("C:\\Users\\dlj\\Documents\\python-programming-masterclass\\Fileio\\binary", 'bw') as binary_write_file:
#     binary_write_file.write(bytes(range(17)))

# with open("C:\\Users\\dlj\\Documents\\python-programming-masterclass\\Fileio\\binary", 'br') as binary_read_file:
#     for b in binary_read_file:
#         print(b)

a = 65534   # FF FE
b = 65535   # FF FF
c = 65536   # 00 01 00 00
x = 2998302 # 00 2D C0 1E

with open("C:\\Users\\dlj\\Documents\\python-programming-masterclass\\Fileio\\binary", 'bw') as binary_write_file:
    binary_write_file.write(a.to_bytes(2, 'big'))
    binary_write_file.write(b.to_bytes(2, 'big'))
    binary_write_file.write(c.to_bytes(4, 'big'))
    binary_write_file.write(x.to_bytes(4, 'big')) # most significant byte will be stored first
    binary_write_file.write(x.to_bytes(4, 'little')) # least significant byte will be stored first

with open("C:\\Users\\dlj\\Documents\\python-programming-masterclass\\Fileio\\binary", 'br') as binary_read_file:
    e = int.from_bytes(binary_read_file.read(2), 'big')
    print(e)
    f = int.from_bytes(binary_read_file.read(2), 'big')
    print(f)
    g = int.from_bytes(binary_read_file.read(4), 'big')
    print(g)
    h = int.from_bytes(binary_read_file.read(4), 'big')
    print(h)
    i = int.from_bytes(binary_read_file.read(4), 'big') # 515910912 because of 'big' instead of 'little'
    print(i)
