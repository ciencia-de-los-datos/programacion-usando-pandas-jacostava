import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")

# tbl0["_c2"] = tbl0["_c2"].astype('str')
# temp = tbl0.groupby('_c1')[str("_c2")].apply(lambda x: ':'.join(sorted(x))).reset_index()
# temp = temp.rename(columns={'_c2':'_c3'})
# temp = temp.rename(columns={'_c3':'_c1','_c1':'_c0'})
# temp.set_index('_c0',inplace=True)
# print(temp)

tbl2["_c5b"] = tbl2["_c5b"].astype('int')
df = pd.merge(tbl0,tbl2,how="left").drop(["_c2","_c3"], axis = 1)
df["_c1n"] = df["_c1"] + ":"
df.rename(columns={"_c1" : "_c1v", "_c1n" : "_c1"}, inplace=True)
sln2 = df.groupby("_c1")["_c5b"].sum()
print(sln2)