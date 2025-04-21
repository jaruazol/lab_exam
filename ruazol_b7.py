
import pandas as pd
df=pd.read_csv('Exam_Table.csv')
replaced= df.replace(' ', '_')
df.columns.str.lower()


unique7 = df['Observer'].unique()
#print(unique7)
unique7.to_csv('b7_output1.csv', index=False)

