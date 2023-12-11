import warnings

warnings.filterwarnings("ignore")

# import important libraries

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import pandas as pd

data_exp1 = (
    "data science is one of the most important courses in computer science",
    "this is one of the best data science courses",
    "the data scientists perform data analysis",
)

# create a reference object to the CountVectorizer constructor
# use the reference object to generate BoW matrix using the fit_transform() function

count_vectorizer = CountVectorizer()
c_vector_matrix_exp1 = count_vectorizer.fit_transform(data_exp1)
c_vector_matrix_exp1

# use get_feature_names_out() to extract vocabulary

c_tokens_exp1 = count_vectorizer.get_feature_names_out()
c_tokens_exp1

# convert BoW matrix to an array format
print("BAG OF WORDS\n")
print(c_vector_matrix_exp1.toarray())

# print("\nTFIDF\n")
tfidf_vect_exp1 = TfidfVectorizer()
t_tfidf_matrix_exp1 = tfidf_vect_exp1.fit_transform(data_exp1)
# print(t_tfidf_matrix_exp1)

# use get_feature_names_out() to extract vocabulary

t_tokens_exp1 = tfidf_vect_exp1.get_feature_names_out()
print("\nVOACBLURY\n")
print(t_tokens_exp1)

print("\nTERM FREQUENCY\n")
from collections import Counter


def calculate_term_frequency(sentence):
    # Tokenize the sentence into words
    words = sentence.split()
    # Count the frequency of each word
    term_frequency = Counter(words)
    return term_frequency


def main():
    sentences = [
        "data science is one of the most important courses in computer science",
        "this is one of the best data science courses",
        "the data scientists perform data analysis",
    ]

    # Calculate term frequency for each sentence
    for i, sentence in enumerate(sentences, start=1):
        term_frequency = calculate_term_frequency(sentence.lower())
        print(f"Term Frequency for Sentence {i}:")
        for word, freq in term_frequency.items():
            if i == 1:
                print(f"{word}: {freq}/12")
            if i == 2:
                print(f"{word}: {freq}/9")
            if i == 3:
                print(f"{word}: {freq}/6")
        print()


if __name__ == "__main__":
    main()


print("\INVERSE DOCUMENT FREQUENCY\n")

import math
from collections import Counter


def calculate_inverse_document_frequency(sentences):
    total_documents = len(sentences)
    term_presence = Counter()

    # Count the presence of each term in any document
    for sentence in sentences:
        terms_in_sentence = set(sentence.split())
        term_presence.update(terms_in_sentence)

    # Calculate IDF for each term
    inverse_document_frequency = {}
    for term, count in term_presence.items():
        inverse_document_frequency[term] = math.log(total_documents / count)

    return inverse_document_frequency


def main():
    sentences = [
        "data science is one of the most important courses in computer science",
        "this is one of the best data science courses",
        "the data scientists perform data analysis",
    ]

    # Calculate IDF for each term
    idf_values = calculate_inverse_document_frequency(sentences)

    # Print IDF values
    print("Inverse Document Frequency:")
    for term, idf in idf_values.items():
        print(f"{term}: {idf}")


if __name__ == "__main__":
    main()


# convert tf.idf matrix to a Pandas dataframe
print("\nTFIDF\n")
df_t_exp1 = pd.DataFrame(data=t_tfidf_matrix_exp1.toarray(), columns=t_tokens_exp1)
print(df_t_exp1)


# create a reference object to the TfidfVectorizer constructor
# use the reference object to generate tf.idf matrix using the fit_transform() function
tfidf_vect_exp2 = TfidfVectorizer()
tfidf_matrix_exp2 = tfidf_vect_exp2.fit_transform(data_exp1)
# print(tfidf_matrix_exp2)

# use get_feature_names_out() to extract vocabulary

t_tokens_exp2 = tfidf_vect_exp2.get_feature_names_out()
t_tokens_exp2

# convert tf.idf matrix to a Pandas dataframe

df_t_exp2 = pd.DataFrame(data=tfidf_matrix_exp2.toarray(), columns=t_tokens_exp2)
df_t_exp2

# generate cosine similarity matrix

t_cosine_similarity_matrix_exp2 = cosine_similarity(tfidf_matrix_exp2)

# convert cosine similarity matrix to Pandas dataframe

df_t_similarity_exp2 = pd.DataFrame(data=t_cosine_similarity_matrix_exp2)
print("\nCOSINE SIMILARITY FUNCTION\n")
print(df_t_similarity_exp2)

# import scityblock (manhattan distance) from scipy

from scipy.spatial.distance import cityblock

# calculate scityblock (manhattan distance) between two document vectors (text1, text2)

cityblock(df_t_exp2.iloc[0], df_t_exp2.iloc[1])

# calculate percentage scityblock (manhattan distance)
print("\nMANHATTAN DISTANCE\n")
print(1 / (cityblock(df_t_exp2.iloc[1], df_t_exp2.iloc[2])))

# import math library to use euclidean distance

import math

# calculate euclidean distance between two document vectors (text2, text3)
print("\nEUCLIDEAN DISTANCE\n")
print(math.dist(df_t_exp2.iloc[1], df_t_exp2.iloc[2]))
