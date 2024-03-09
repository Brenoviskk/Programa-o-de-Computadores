segunda = int(input("João trabalhou na segunda?"))
quarta = int(input("João trabalhou na quarta?"))
sexta = int(input("João trabalhou na sexta?"))

# Comparação TV 55k
tv55 = bool(segunda) and bool(quarta) and bool(sexta)
print(f"João pode comprar uma tv 55? {tv55}")

# Comparação TV tubo
tvtubo= bool(segunda) 
print(f"João pode comprar uma tv de tubo? {tvtubo}")

# Comparação TV 32
tv32 = bool(segunda) and bool(quarta)
print(f"João pode comprar uma tv de 32? {tv32}")
