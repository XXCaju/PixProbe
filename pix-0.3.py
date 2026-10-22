pix = input("Pix: ")

i = 0

while i < len(pix):
    campo = pix[i:i+2]
    tamanho = int(pix[i+2:i+4])
    valor = pix[i+4:i+4+tamanho]

    print(f"{campo} ({tamanho}): {valor}")

    i += 4 + tamanho

def crc16(data):
    crc = 0xFFFF

    for byte in data.encode():
        crc ^= byte << 8

        for _ in range(8):
            if crc & 0x8000:
                crc = ((crc << 1) ^ 0x1021) & 0xFFFF
            else:
                crc = (crc << 1) & 0xFFFF

    return f"{crc:04X}"

pix_sem_crc = pix[:-4]
crc_informado = pix[-4:]

print("CRC Calculado :", crc16(pix_sem_crc))
print("CRC Informado :", crc_informado)
