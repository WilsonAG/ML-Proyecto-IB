import lib.tweets as tw
import lib.nlp as nlp

if __name__ == "__main__":
    # twts = tw.get(1)
    twts = ['Ecuador supera los 45.000 casos mientras aplica desescalada de confinamiento\nhttps://t.co/N5EKOg7AK4']

    twts = nlp.do_nlp(twts)
    print(twts)
