nachalnaya_tsifra = int(input("Введите произвольную цифру (от 0 до 9): "))

schotchik = 0

for i in range(nachalnaya_tsifra * 100000, (nachalnaya_tsifra + 1) * 100000):

    bilet = str(i)
    pervaya_polovina = bilet[:3]
    vtoraya_polovina = bilet[3:]

    summa_pervoy_poloviny = sum(int(digit) for digit in pervaya_polovina)
    summa_vtoroy_poloviny = sum(int(digit) for digit in vtoraya_polovina)

    if summa_pervoy_poloviny == summa_vtoroy_poloviny:
        schotchik += 1

print("Количество счастливых билетов:", schotchik)