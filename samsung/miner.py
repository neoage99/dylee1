from konlpy.tag import Okt
import re
from nltk.tokenize import word_tokenize
class Samsung:
    def __init__(self):
        pass

    @staticmethod
    def read_file(self):
        okt = Okt()
        okt.pos("삼성전자 글로벌센터 전자사업부", stem=True)
        filename = 'data/kr-Report_2018.txt'
        with open(filename, 'r', encoding='utf-8') as f:
            texts = f.read()
        return texts

    @staticmethod
    def extract_hangeul(texts):
        temp = texts.replace('\n', ' ')
        tokenizer = re.compile(r'[^ㄱ-힣]+')
        temp = tokenizer.sub('',temp)
        # print(temp[:300])
        return temp

    @staticmethod
    def change_token(texts):
        tokens = word_tokenize()_