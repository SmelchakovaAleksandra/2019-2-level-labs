from math import log


REFERENCE_TEXTS = []


def clean_tokenize_corpus(texts: list) -> list:
    corpus = []
    if not texts or not isinstance(texts, list):
        return corpus
    for t in texts:
        if not isinstance(t, str):
            continue
        clean_text = ''
        t = t.replace('\n', ' ')
        t = t.replace('<br />', ' ')
        while '  ' in t:
            t = t.replace('  ', ' ')
        for symbol in t:
            if symbol.isalpha() or symbol == ' ':
                clean_text += symbol.lower()
        clean_text = clean_text.split()
        corpus.append(clean_text)
    return corpus


class TfIdfCalculator:
    def __init__(self, corpus):
        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []
        self.files = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']

    def calculate_tf(self):
        if not isinstance(self.corpus, list) or self.corpus == []:
            return []
        for t in self.corpus:
            if not isinstance(t, list):
                continue
            dic = {}
            words = len(t)
            for word in t:
                if not isinstance(word, str):
                    words -= 1
            for word in t:
                if not isinstance(word, str):
                    continue
                if word not in dic:
                    dic[word] = (t.count(word) / words)
            if dic:
                self.tf_values.append(dic)
        return self.tf_values

    def calculate_idf(self):
        if not isinstance(self.corpus, list) or self.corpus == []:
            return {}
        doc_count = len(self.corpus)
        for t in self.corpus:
            if not isinstance(t, list):
                doc_count -= 1
        for t in self.corpus:
            if not isinstance(t, list):
                continue
            for word in t:
                if isinstance(word, str):
                    doc_with_word = 0
                    for part in self.corpus:
                        if isinstance(part, list):
                            if word in part:
                                doc_with_word += 1
                    self.idf_values[word] = log(doc_count / doc_with_word)
        return self.idf_values

    def calculate(self):
        if self.tf_values and self.idf_values:
            for t in self.tf_values:
                tf_idf_dict = {}
                for word, tf in t.items():
                    tf_idf_dict[word] = tf * self.idf_values[word]
                self.tf_idf_values.append(tf_idf_dict)
        return self.tf_idf_values

    def report_on(self, word, document_index):
        if not self.tf_idf_values or document_index >= len(self.tf_idf_values):
            return ()
        tf_idf_dic = self.tf_idf_values[document_index]
        if word in tf_idf_dic:
            sorted_tf_idf = sorted(tf_idf_dic, key=tf_idf_dic.get, reverse=True)
            index = sorted_tf_idf.index(word)
        res = (tf_idf_dic[word], index)
        return res