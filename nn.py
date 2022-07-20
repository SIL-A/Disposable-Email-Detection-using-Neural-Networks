import pandas as pd

colnames = ["Emails","Value"]
df1 = pd.read_csv("email-ids.txt", names=colnames, sep='\t')
df1 = df1.assign(Value=0)
df2 = pd.read_csv("disposable-email-ids.txt", names=colnames, sep='\t')
df2 = df2.assign(Value=1)
df2 = pd.concat([df2, pd.DataFrame.from_records(df1)],ignore_index=True)
df2 = df2.sample(frac=1).reset_index(drop=True)
print(df2.tail())

df2.to_csv("dataset.csv")