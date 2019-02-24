
from collections import Counter
import re
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np
import pandas as pd
from os import path
import os

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

class SoftwareCareerAnalysis:

    def __init__(self, key_words, other_words):

        self.key_words = key_words
        self.other_words = other_words

    def software_key_word_analysis(self, file, fig):
        """Find the count of keyword each word in text"""

        key_words = self.key_words
        mask = np.array(Image.open("aircraft_carrier.jpg"))

        index_words = []
        for kw in key_words:
            for k in kw.split():
                index_words.append(k)

        for ow in other_words:
            for o in ow.split():
                o = re.sub(r'\d', '', o)
                o = o.replace(',', '').replace('.', '').strip()
                index_words.append(o)

        word_list = []
        for line in file:
            for word in line.split():
                for text in index_words:
                    if word == text:
                        word_list.append(word)

        words = Counter(word_list).most_common()
        words = pd.DataFrame(words)
        words.columns = ["Words", 'Counts']
        generate_wordcloud(words, mask, fig)


def generate_wordcloud(words, mask, name):
    """https://blog.goodaudience.com/how-to-generate-a-word-cloud-of-any-shape-in-python-7bce27a55f6e
    https://amueller.github.io/word_cloud/auto_examples/frequency.html
    https://pngtree.com/so/aircraft-carrier

    """
    text = str(words["Words"])

    WordCloud(
        width=800, height=365,
        background_color='black',
        max_words = 20000,
        repeat = True,
        stopwords=STOPWORDS,
        min_font_size=1,
        mask=mask
    ).generate(text).to_file(path.join(d,name))


if __name__ == "__main__":
    """"""
    sd_fig = 'software_developer_word_cloud.png'
    sd_file = open("/Users/hannahroach/Desktop/software_careers_analysis/careers/software_developer.txt", "r")
    sd_key_words = open("/Users/hannahroach/Desktop/software_careers_analysis/careers/developer_key_words.txt", "r")
    other_words = open("/Users/hannahroach/Desktop/software_careers_analysis/careers/other_software_terms.txt", "r")
    SoftwareCareerAnalysis(sd_key_words, other_words).software_key_word_analysis(sd_file, sd_fig)
