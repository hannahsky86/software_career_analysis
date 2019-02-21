
from collections import Counter
import re
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import requests


class SoftwareCareerAnalysis:

    def __init__(self, key_words):

        self.key_words = key_words

    def software_key_word_analysis(self, file, fig):
        """Creates a list of times, in half hour increments, when all team members are available.
            https://www.scriptol.com/programming/list-programming-languages.php
        """

        key_words = self.key_words

        mask = np.array(Image.open(
            requests.get('http://www.clker.com/cliparts/7/1/4/4/11954261251065555692liftarn_Su-27_silhouette.svg.med.png', stream=True).raw))
        text = ''
        for kw in key_words:
            text += kw

        word_list = []
        for line in file:
            for word in line.split():
                if word in text.split():
                    word_list.append(word)

        words = Counter(word_list).most_common()
        words = pd.DataFrame(words)
        words.columns = ['Names', 'Count']
        print(words)
        create_word_cloud(words, fig, mask)


def create_word_cloud(word_list, name, mask):
    text = word_list["Names"].values
    wordcloud = WordCloud(
        width=5000,
        height=4000,
        background_color='black',
        stopwords=STOPWORDS, mask=mask).generate(str(text))

    plt.figure(figsize=(10,10), facecolor='white', edgecolor='blue')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig(name, dpi=400)


def clean_words(word):
    """"""
    # for word in counts:
    w = word.strip().lower()
    w = re.sub('[!@$.,-]', '', w)
    return w


if __name__ == "__main__":
    """"""
    sd_fig = 'software_developer_word_cloud.png'
    sd_file = open("/Users/hannahroach/Desktop/software_careers_analysis/careers/software_developer.txt", "r")
    sd_key_words = open("/Users/hannahroach/Desktop/software_careers_analysis/careers/developer_key_words.txt", "r")
    SoftwareCareerAnalysis(sd_key_words).software_key_word_analysis(sd_file, sd_fig)
