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
    tf = nlp.get_tf_word_bag(fii_good, good_words, twts, True)
    wtf = nlp.get_tf_word_bag(fii_good, good_words, twts, False)
    df = nlp.get_df_idf(good_words, tf, wtf, False)
    idf = nlp.get_df_idf(good_words, tf, wtf, True)
    tb_tf_idf = nlp.get_mtx_tf_idf(good_words, twts, wtf, idf)

    print(sum(tb_tf_idf[0]))
