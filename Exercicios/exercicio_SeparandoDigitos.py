num = int(input("Digite um numero "))
n = str(num)

print("Analizando o numero {} ".format(num))
print("Unidade {}".format(n[3]))
print("Dezena {}0".format(n[2]))
print("Centena {}00".format(n[1]))
print("Milhar {}000".format(n[0]))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print("Analizando o numero {} ".format(num))
print("Unidade {}".format(u))
print("Dezena {}0".format(d))
print("Centena {}00".format(c))
print("Milhar {}000".format(m))