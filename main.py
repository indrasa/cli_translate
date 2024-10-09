from translate import Translator
terjemah = Translator(to_lang="id")

def terjemahkan(kata: str):
    return terjemah.translate(kata)

while True:
    kata_asing = input("Masukkan terjemahan: ")
    print(terjemahkan(kata=kata_asing))