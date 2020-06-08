import lib.nlp as nlp
import pandas as pd

if __name__ == "__main__":
    data = pd.read_excel('./data.xlsx', encoding='utf-8')
    index = 0
    for item in data['tweets']:

        item = str(item).strip()
        print(nlp.clean(item))
        break

        index += 1
