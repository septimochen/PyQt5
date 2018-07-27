import pandas as pd


df = pd.read_csv("data/estatetop100.csv")


def search(word):
    ls = []
    for company in list(df.name):
        if word in company:
            ls.append(company)
    return ls


print(df.loc[df.name.isin(search("万科")), ('rank', 'name')])