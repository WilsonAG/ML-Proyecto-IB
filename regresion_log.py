import lib.regresion as reg
import lib.nlp as nlp


if __name__ == "__main__":
    train, test = reg.load_data('data/tweets/tweets.csv')
    model = reg.eval(train, test)
    datito = reg.test_model(model, train, test)

    error = reg.error(datito)
