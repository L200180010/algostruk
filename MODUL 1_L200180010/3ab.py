def jumlahHurufVokal(input):
    total = 0
    voc = ["a", "i", "u", "e", "o"]
    for i in input:
        if i in voc:
            total+=1
    return [len(input), total]

def jumlahHurufKonsonan(input):
    total = 0
    voc = ["a", "i", "u", "e", "o"]
    for i in input:
        if i in voc:
            total+=1
    return [len(input), len(input)-total]

v = jumlahHurufVokal("Ismi Dzikrina")
k = jumlahHurufKonsonan("Ismi Dzikirna")

print(v)
print(k)
