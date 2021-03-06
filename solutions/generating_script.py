import argparse
import bigramm_model

parser = argparse.ArgumentParser(description='Preprocessing script')
parser.add_argument('-s', action="store", dest="load_way")  # принимает путь до папки с частотами для загрузки
parser.add_argument('-n', action="store", dest="name")  # с таким именем будут загружены частоты
parser.add_argument('-l', action="store", dest="length")  # длина генерируемого текста
parser.add_argument('-p', action="store", dest="pref")  # принимает префикс генерируемого текста (опционально)
parser.add_argument('-k', action="store", dest="seed")  # принимает сид радномайзера
args = parser.parse_args()

save_way = args.load_way
name = args.name
length = args.length
pref = args.pref
seed = args.seed

model = bigramm_model.model_v1()
model.load_freq(name, save_way)
model.ch_seed(seed)

pred = model.predict(length, pref)
print(*pred)
