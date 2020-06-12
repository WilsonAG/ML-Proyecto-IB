import lib.tweets as tw
import lib.nlp as nlp

if __name__ == "__main__":
    # twts = tw.get(1)
    twts = ['Ecuador supera los 45.000 casos mientras aplica desescalada de confinamiento\nhttps://t.co/N5EKOg7AK4',
            'hola a todos ayudo justicia al mundo feliz']

    twts = nlp.do_nlp(twts)
    good_words = nlp.get_dictionary('data/new/buenas.txt')
    bad_words = nlp.get_dictionary('data/new/mala.txt')

    fii_good = nlp.get_fii(twts, good_words)
    simi = nlp.do_cosine_method(fii_good, good_words, twts)

    print(nlp.get_dictionary(False))
