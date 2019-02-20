
from collections import Counter
import re
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd


class SoftwareCareerAnalysis:

    def __init__(self, key_words):

        self.key_words = key_words

    def software_key_word_analysis(self, file, fig):
        """Creates a list of times, in half hour increments, when all team members are available."""
        key_words = self.key_words
        list = []
        for line in file:
            for word in line.split():
                list.append(word)
        counts = Counter(list).most_common()
        keywords = pd.DataFrame(key_words)
        key_list = keywords[0].apply(clean_words).to_list()
        counts = pd.DataFrame(counts)
        counts[3] = counts[0].apply(clean_words)
        newcounts = counts[counts[3].isin(key_list)][[3, 1]].groupby(3).sum().reset_index()
        newcounts = newcounts.sort_values(by=1, ascending= False)
        print(newcounts)
        create_word_cloud(newcounts, fig)


def create_word_cloud(word_count, name):

    text = word_count[3].values
    wordcloud = WordCloud(
        width=5000,
        height=4000,
        background_color='black',
        stopwords=STOPWORDS).generate(str(text))

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig(name, dpi=200)


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
