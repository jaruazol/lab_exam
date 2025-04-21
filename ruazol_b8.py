import pandas as pd
df=pd.read_csv('Exam_Table.csv')

pd.Series(df['Visibility (m)'] > 8).to_csv('b8_output1.csv', index=True)

