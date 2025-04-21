
import pandas as pd
df=pd.read_csv('Exam_Table.csv')

df['Count'].fillna(0, inplace=False).to_csv('b10_output1.csv', index=True)