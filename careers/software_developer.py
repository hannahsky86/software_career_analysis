
from collections import Counter
import re
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import requests
import pandas as pd


class SoftwareCareerAnalysis:

    def __init__(self, key_words, other_words):

        self.key_words = key_words
        self.other_words = other_words

    def software_key_word_analysis(self, file, fig):
        """Creates a list of times, in half hour increments, when all team members are available.
            https://www.scriptol.com/programming/list-programming-languages.php
        """

        key_words = self.key_words

        mask = np.array(Image.open(
         requests.get('http://www.clker.com/cliparts/7/1/4/4/11954261251065555692liftarn_Su-27_silhouette.svg.med.png',
                                                                                        stream=True).raw))

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
    """
    text = str(words["Words"])

    word_cloud = WordCloud(
        width=500, height=500,
        background_color='black',
        max_words = 20000,
        repeat = True,
        stopwords=STOPWORDS,
        # contour_width=1,
        min_font_size=4,
        # contour_color='gray',
        # mask=mask
    ).generate(text)

    plt.figure( facecolor='blue', edgecolor='blue')
    plt.imshow(word_cloud,interpolation = 'bilinear')

    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig(name)


if __name__ == "__main__":
    """"""
    sd_fig = 'software_developer_word_cloud.png'
    sd_file = open("/Users/hannahroach/Desktop/software_careers_analysis/careers/software_developer.txt", "r")
    sd_key_words = open("/Users/hannahroach/Desktop/software_careers_analysis/careers/developer_key_words.txt", "r")
    other_words = open("/Users/hannahroach/Desktop/software_careers_analysis/careers/other_software_terms.txt", "r")
    SoftwareCareerAnalysis(sd_key_words, other_words).software_key_word_analysis(sd_file, sd_fig)
