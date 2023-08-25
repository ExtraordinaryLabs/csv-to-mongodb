import re
import pandas as pd



df = pd.read_csv('myfile.csv', sep=',')

columns_to_clean = ['Brand Profiles', 'Brand', 'Brand Personas', 'Brand Cohorts']


def remove_urls(text):
    return re.sub(r'\(https?://\S+\)', '', text)


for col in columns_to_clean:
    df[col] = df[col].apply(lambda x: remove_urls(x))

df.to_csv('cleaned_data.csv', sep=',', index=False)

print(df)
