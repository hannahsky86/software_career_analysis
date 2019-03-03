
from collections import Counter
import re
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np
import pandas as pd
from os import path
import os
import matplotlib.pyplot as plt


d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

class SoftwareCareerAnalysis:

    def __init__(self, key_words, other_words, file):

        self.key_words = key_words
        self.other_words = other_words
        self.file = file

    def software_key_word_analysis(self):
        """Find the count of keyword each word in text"""

        key_words = self.key_words
        other_words = self.other_words
        file = self.file

        index_list = []
        for kw in open(key_words, "r"):
            for k in kw.split():
                index_list.append(k)
        program_languages_df = create_word_list(file, index_list)
        generate_bar_chart(program_languages_df, "bar_chart_other_words_list.png")
        generate_wordcloud(program_languages_df, "word_cloud_program_languages.png")


        for ow in open(other_words, "r"):
            for o in ow.split():
                o = re.sub(r'\d', '', o)
                o = o.replace(',', '').replace('.', '').strip()
                index_list.append(o)

        complete_list_df = create_word_list(file, index_list)
        generate_bar_chart(complete_list_df, "bar_chart_program_languages.png")
        generate_wordcloud(complete_list_df, "word_cloud_software_words.png")


def create_word_list(file, index_words):

    word_list = []
    for line in open(file, "r"):
        for word in line.split():
            for text in index_words:
                if word == text:
                    word_list.append(word)
    word_cnt = Counter(word_list).most_common()
    words_df = pd.DataFrame(word_cnt)
    words_df.columns = ["Words", 'Counts']
    return words_df


def generate_bar_chart(words, name):

    fig, ax = plt.subplots(nrows=1, ncols=1)
    words = words.head(10)
    index = np.arange(len(words['Words']))
    ax.barh(index, words['Counts'])
    plt.xlabel('Words', fontsize=5)
    plt.ylabel('No of Words', fontsize=5)
    plt.xticks(index, words['Words'], fontsize=10, rotation=30)
    plt.title('Words')
    fig.savefig(path.join(d,name),dpi=200 )



def generate_wordcloud(words, name):
    """https://blog.goodaudience.com/how-to-generate-a-word-cloud-of-any-shape-in-python-7bce27a55f6e
    https://amueller.github.io/word_cloud/auto_examples/frequency.html
    https://pngtree.com/so/aircraft-carrier

    """
    text = str(words["Words"])

    WordCloud(
        width=850, height=550,
        background_color='black',
        max_words = 20000,
        repeat = True,
        stopwords=STOPWORDS,
        min_font_size=1,
    ).generate(text).to_file(path.join(d,name))


if __name__ == "__main__":
    """"""
    # sd_fig = 'software_developer_word_cloud.png'
    file = ("/Users/hannahroach/Desktop/software_careers_analysis/careers/software_developer.txt")
    sd_key_words = ("/Users/hannahroach/Desktop/software_careers_analysis/careers/developer_key_words.txt")
    other_words = ("/Users/hannahroach/Desktop/software_careers_analysis/careers/other_software_terms.txt")
    SoftwareCareerAnalysis(sd_key_words, other_words, file).software_key_word_analysis()
