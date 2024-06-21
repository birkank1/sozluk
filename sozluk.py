meme_dict = {
            "MVP":"En değerli oyunucu"
}
kelime=input("kelime girin")
if kelime in meme_dict.keys():
    print(meme_dict[kelime])
else:
    print("kelime listede yok")
