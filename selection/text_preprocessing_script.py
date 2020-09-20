import bigramm_model
import argparse
from os import makedirs, remove
from os.path import exists
from os.path import join as path_join

parser = argparse.ArgumentParser(description='Preprocessing script')
parser.add_argument('-d', action="store", dest="path")  # принимает путь к корпусу
parser.add_argument('-s', action="store", dest="save_way")  # принимает путь до папки куда выгрузить частоты
parser.add_argument('-n', action="store", dest="name")  # с таким именем будут сохранены частоты
args = parser.parse_args()

path = args.path
name = args.name
save_way = args.save_way

model = bigramm_model.model_v1()
corpus = model.fit(path)

model.generate(corpus)
model.save_freq(name, save_way)

# python C:\Users\idkon\Documents\tinkoff_generation\selection\text_preprocessing_script.py -n test_Main -d C:\Users\idkon\Documents\tinkoff_generation\selection\chistiy_ponedelnik.txt -s C:\Users\idkon\Documents\tinkoff_generation\selection\
