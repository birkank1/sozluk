meme_dict = {
            "MVP":"En değerli oyunucu",
            "GG":"İyi oyundu",
}
for i in range (5):
                kelime=input("kelime girin")
                if kelime in meme_dict.keys():           
                    print(meme_dict[kelime])
                else:
                    print("kelime listede yok")
