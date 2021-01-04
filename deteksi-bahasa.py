from langdetect import detect, detect_langs, DetectorFactory
import pyperclip

pyperclip.paste()

DetectorFactory.seed = 0

global repeat
repeat = 0
while repeat == 0:
    bahasa = input("masukan kalimat : ")
    kode_bahasa = {"af": "afrika", "ar": "arab", "bg": "bulgaria", "bn": "bengali", "ca": "catalan", "cs": "ceko",
                   "cy": "weish", "da": "denmark", "de": "jerman", "el": "yunani", "en": "english", "es": "spanyol", "et": "estonia",
                   "fa": "persia", "fi": "finlandia", "fr": "perancis", "gu": "gujarat", "he": "ibrani", "hi": "hindi", "hr": "kroasia",
                   "hu": "hungaria", "id": "indoneisa", "it": "italia", "ja": "japan", "kn": "kanada", "ko": "korea", "lt": "lithuania",
                   "lv": "latvia", "mk": "makedonia", "ml": "malayalam", "mr": "marathi", "ne": "nepal", "nl": "belanda",
                   "no": "norwegia", "pa": "punjabi", "pl": "polandia", "pt": "portugis", "ro": "rumania", "ru": "rusia", "sk": "slowakia", "sl": "slovenia",
                   "so": "somalia", "sq": "albania", "sv": "swedia", "sw": "swahli", "ta": "tamli", "te": "telugu", "th": "thailand",
                   "tl": "tigrinya", "tr": "turki", "uk": "ukrania", "ur": "urdu", "vi": "vietnam", "zh-cn": "tionghoa", "zh-tw": "zande"
                   }

    deteksi = detect(bahasa)
    deteksi2 = detect_langs(bahasa)

    print("menggunakan bahasa : ", kode_bahasa.get(str(deteksi)))
    print("kemungkinan bahasa : ", deteksi2)

    prompt = input('\napakah mau lanjut? (Y/N) ')
    print('\n')
    if prompt.lower() == 'y':
        repeat = 0
    elif prompt.lower() == 'n':
        repeat = 1
    else:
        print('karakter salah . keluar !!')
        repeat = 1
