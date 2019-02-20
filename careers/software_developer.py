
from collections import Counter
import re
import pandas as pd


class SoftwareCareerAnalysis:

    def __init__(self, file, key_words):
        self.file = file
        self.key_words = key_words


    def software_developers(self):
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
        newcounts = newcounts.sort_values(by=1, ascending = False)
        print(newcounts)


def clean_words(word):
    """"""
    # for word in counts:
    w = word.strip().lower()
    w = re.sub('[!@#$.,-]', '', w)
    return w


if __name__ == "__main__":
    """"""
    file = open("/Users/hannahroach/Desktop/software_careers_analysis/careers/software_developer.txt", "r")
    key_words = open("/Users/hannahroach/Desktop/software_careers_analysis/careers/developer_key_words.txt", "r")
    SoftwareCareerAnalysis(file, key_words).software_developers()
