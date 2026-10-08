pix = input("Pix: ")

i = 0

while i < len(pix):
    campo = pix[i:i+2]
    tamanho = int(pix[i+2:i+4])
    valor = pix[i+4:i+4+tamanho]

    print(f"{campo} ({tamanho}): {valor}")

    i += 4 + tamanho