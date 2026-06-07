# Rosalind: Mortal Fibonacci Rabbits
# Masala sharti: 86 oy davomida quyonlar ko'payadi, lekin har bir quyon juftligi 
# 18 oy yashab, keyin o'lib ketadi. Jami tirik qolganlarni hisoblash.

n = 86  # Jami oylar soni
m = 18  # Quyonlarning yashash muddati (umri)

# Har bir oylik quyonlar guruhini saqlash uchun ro'yxat (18 ta katak)
yosh_guruhlari = [0] * m
yosh_guruhlari[0] = 1  # 1-oyda faqat 1 ta yangi tug'ilgan juft bor

# 2-oydan boshlab 86-oygacha hisoblash tsikli
for oy in range(1, n):
    # Voyaga yetgan quyonlar (2 oylikdan boshlab 18 oylikkacha bo'lganlar) yangi avlod tug'adi
    yangi_tugilganlar = sum(yosh_guruhlari[1:])
    
    # Quyonlarni 1 yoshga ulgaytiramiz (guruhlarni bitta o'ngga suramiz)
    # 18 oylik bo'lgan eng oxirgi katakdagilar avtomatik ravishda o'ladi (ro'yxatdan chiqadi)
    for i in range(m - 1, 0, -1):
        yosh_guruhlari[i] = yosh_guruhlari[i - 1]
    
    # Yangi tug'ilgan juftliklarni birinchi katakka (0-indeksga) joylaymiz
    yosh_guruhlari[0] = yangi_tugilganlar

# 86-oyda tirik qolgan barcha quyonlar juftligi yig'indisi
jami_quyonlar = sum(yosh_guruhlari)

print("Rosalind saytiga kiritiladigan to'g'ri javob:")
print(jami_quyonlar)
