import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# step 1 Load data


df=pd.read_csv("Tokyo 2021 dataset v3.csv")

# step 2 Explore

print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())

#  step 3 Clean

print(df.isnull().sum())
df.drop_duplicates(inplace=True)


# step 4 Function + if,elif,else

def medal(total):
    if total>= 100:
        return "excellent"
    elif total>= 50:
        return "good"
    else:
        return "average"
    
print (medal(113))


# step 5 Filter, sort, rename
    
gold = df[df["Gold Medal"] > 20]
print (gold)

print(df.sort_values(by="Total",ascending=False))

df.rename(columns={"Gold Medal":"Gold"}, inplace=True)
print(df.rename)

# step 7 GroupBy

print(df.groupby("Continent")
      ["Total"].sum())


# setp 8 NumPy

arr = np.array(df["Total"])
print(arr.mean())
print(arr.max())


# step 9  List + loop + condition

countries=list(df["Team/NOC"])
for i in countries:
    if "United" in i:
        print(i)


# step 10 File handling

with open ("output.txt","w") as f:
    f.write("Tokyo Olympics project")



# step 11 Matplotlib
colors=[
    "blue",  #USA
    "red",   #china
    "green", #japan
    "navy",  #Great Britain
    "purple" #ROC
]
plt.figure(figsize=(10,5))  #chart size
plt.bar(df["Team/NOC"][:5],
df["Gold"][:5], color=colors)
plt.xticks(rotation=20,ha="right")
plt.xlabel("countries")
plt.ylabel("Gold Medals")
plt.title("Top 5 countries by Gold models")
plt.tight_layout()
plt.show()

# step2 Seaborn

sns.barplot(x="Team/NOC", y="Gold", data=df.head())
plt.xticks(rotation=45)
plt.show()

#histogram

plt.figure(figsize=(7,5))
plt.hist(df["Gold"], bins=10,
         color="orange",
         edgecolor="black")

plt.title("Distribution of Gold Medals")
plt.xlabel("Gold Medals")
plt.ylabel("Frequency")
plt.show()


#scattar

plt.figure(figsize=(7,5))
plt.scatter(df["Gold"], df["Total"],
            color="red")

plt.title("Gold vs Total Medals")
plt.xlabel("Gold Medals")
plt.ylabel("Total Medals")
plt.show()


#pie

plt.figure(figsize=(6,6))
plt.pie(df["Gold"][:5],
        labels=df["Team/NOC"][:5],
        autopct="%1.1f%%",
        startangle=90)

plt.title("Gold Medal Distribution")
plt.show()