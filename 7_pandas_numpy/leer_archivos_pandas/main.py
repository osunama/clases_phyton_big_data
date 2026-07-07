import pandas as pd

df_txt = pd.read_csv("./texto.txt")
print(df_txt.to_dict())