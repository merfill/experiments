
import numpy as np
import json
import codecs


class Dictionary:


    def __init__(self, embedding_size = 32):
        self._embedding_size = embedding_size
        self._ids2embeddings = {}
        self._words2ids = {}
        self._ids2words = {}
        np.random.seed()


    def get_word_by_id(self, id):
        if id not in self._ids2words:
            raise Exception('incorrect id is passed: {}'.format(id))
        return self._ids2words[id]


    def get_embedding_by_id(self, word):
        if id not in self._ids2embeddings:
            raise Exception('incorrect id is passed: {}'.format(id))
        return self._ids2embeddings[id]


    def get_id_by_word(self, word):
        if word in self._words2ids:
            id = self._words2ids[word]
        else:
            id = len(self._words2ids)
            self._words2ids[word] = id
            self._ids2words[id] = word
            self._ids2embeddings[id] = np.random.random([self._embedding_size])
        return id


    def get_ids(self, words):
        return [self.get_id_by_word(w) for w in words]


    def get_dict_size(self):
        return len(self._ids2words.keys())


    @classmethod
    def load(cls, file_path):
        with codecs.open(file_path, encoding='utf-8') as f:    
            data = json.load(f)
            r = cls(data['embedding_size'])
            r._ids2embeddings = {int(k): np.array(v) for k, v in data['ids2embeddings'].items()}
            r._words2ids = data['words2ids']
            r._ids2words = {int(k): v for k, v in data['ids2words'].items()}
        return r


    def save(self, file_path):
        data = {}
        data['embedding_size'] = self._embedding_size
        data['ids2embeddings'] = {}
        for k, v in self._ids2embeddings.items():
            data['ids2embeddings'][k] = v.tolist()
        data['words2ids'] = self._words2ids
        data['ids2words'] = self._ids2words
        with codecs.open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f)
