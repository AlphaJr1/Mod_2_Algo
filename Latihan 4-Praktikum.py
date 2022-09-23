#Adrian Alfajri - 064002200009
import math
n = str(input("Masukkan nama kota pertama = "))
t1 = float(input("Masukkan lattitude kota pertama = "))
g1 = float(input("Masukkan longitude kota pertama = "))

m = str(input("Masukkan nama kota kedua = "))
t2 = float(input("Masukkan lattitude kota kedua = "))
g2 = float(input("Masukkan longitude kota kedua = "))

dlat = t2 - t1
dlon = g2 - g1

a = math.sin(math.radians(dlat/2)) ** 2 + math.cos(math.radians(t1)) * math.cos(math.radians(t2)) * math.sin(math.radians(dlon/2)) ** 2

# Versi Arc sinus
c = 2 * math.sin(math.sqrt(a))

# Versi Arc tangen 2
r = 6371.01

print('')
print("jarak antara", n , "dan", m , "sejauh" , c*r , "kilometer")

