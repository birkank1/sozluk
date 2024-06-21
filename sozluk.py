meme_dict = {
            "MVP":"En değerli oyunucu"
            "GG":"İyi oyundu"
}
kelime=input("kelime girin")
if kelime in meme_dict.keys():
            for kelime in range (5):
    print(meme_dict[kelime])
else:
    print("kelime listede yok")
