# Rosalind: Rabbits and Recurrence Relations
# Masala sharti: 30 oy davomida har bir voyaga yetgan juftlik 3 tadan bolalaganda 
# jami quyonlar juftligi sonini hisoblash.

n = 30  # Oylar soni
k = 3   # Har bir avlodda tug'iladigan quyonlar juftligi soni

# Boshlang'ich holat: 1-oyda va 2-oyda 1 juftdan quyon bo'ladi
quyonlar = [0] * (n + 1)
quyonlar[1] = 1
quyonlar[2] = 1

# 3-oydan boshlab 30-oygacha dinamik dasturlash (tsikl) orqali hisoblash
for i in range(3, n + 1):
    # i-oydagi quyonlar = o'tgan oydagi quyonlar + (undan oldingi oydagi voyaga yetganlar * k)
    quyonlar[i] = quyonlar[i - 1] + (quyonlar[i - 2] * k)

# Yakuniy javobni ekranga chiqarish
print("30-oydagi jami quyonlar juftligi soni:", quyonlar[n])
