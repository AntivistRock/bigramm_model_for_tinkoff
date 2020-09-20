from re import sub, findall
import codecs
import pickle
from random import choice


class model_v1:
    def __init__(self, freq=None, power=None):
        if freq is None and power is None:
            self.bigr_freq = dict()
            self.mono_freq = dict()
        else:
            self.bigr_freq = freq
            self.mono_freq = power
        self.train_text = ''

    # предобработка текста
    def fit(self, path):
        self.path = path
        with codecs.open(self.path, "r", "utf_8_sig") as self.f:
            self.st = self.f.read()
            self.letters = '[^-' + ''.join([chr(i) for i in range(1040, 1104)]) + ' ]'
            self.letters_only = sub(self.letters, '', self.st)
            self.train_text = self.letters_only.lower()
            return findall(r'\w+', self.train_text)

    # создание частот
    def generate(self, corpus):
        self.corpus = corpus
        if len(corpus) < 2:
            return 'ERROR: too small text'
        self.mono_freq[self.corpus[0]] = 1

        for i in range(1, len(self.corpus)):
            s = self.corpus[i - 1]
            t = self.corpus[i]

            # monogramm

            if t in self.mono_freq:
                self.mono_freq[t] += 1
            else:
                self.mono_freq[t] = 1

            # bigramm

            if s in self.bigr_freq:
                if t in self.bigr_freq[s]:
                    self.bigr_freq[s][t] += 1
                else:
                    self.bigr_freq[s][t] = 1
            else:
                self.bigr_freq[s] = dict()
                self.bigr_freq[s][t] = 1

    # функции для сохранения и загрузки частот
    def save_freq(self, name, folder_path):
        with open(folder_path + name + '_bigr_freq' + '.pkl', 'wb+') as f:
            print('Saving', len(self.bigr_freq), 'bigramm frequencies')
            pickle.dump(self.bigr_freq, f, pickle.HIGHEST_PROTOCOL)
        print('Bigramm frequency saved successfully.')
        with open(folder_path + name + '_power' + '.pkl', 'wb+') as f:
            print('Saving', len(self.mono_freq), 'monogramm frequencies')
            pickle.dump(self.mono_freq, f, pickle.HIGHEST_PROTOCOL)
        print('Monogramm frequency saved successfully.')

    def load_freq(self, name, folder_path):
        with open(folder_path + name + '_bigr_freq' + '.pkl', 'rb') as f:
            self.bigr_freq = pickle.load(f)
            print('Bigramm frequency uploaded successfully.')
        with open(folder_path + name + '_power' + '.pkl', 'rb') as f:
            self.mono_freq = pickle.load(f)
            print('Monogramm frequency uploaded successfully.')

    # предсказание length следующих символов по префиксу pref
    def predict(self, length, pref=None):

        if pref is None:
            self.ans = [choice(list(self.mono_freq.items()))[0]]
        else:
            self.letters = '[^' + ''.join([chr(i) for i in range(1040, 1104)]) + ' ]'
            self.pref = sub(self.letters, '', pref).lower()
            self.ans = findall(r'\w+', self.pref)

        for i in range(int(length)):
            if self.ans[-1] in self.bigr_freq and self.bigr_freq[self.ans[-1]]:
                self.ans.append(choice(list(self.bigr_freq[self.ans[-1]].items()))[0])
            else:
                self.ans.append(choice(list(self.mono_freq.items()))[0])
        return self.ans
