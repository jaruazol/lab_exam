
import pandas as pd
df=pd.read_csv('Exam_Table.csv')

avg_count = df.groupby('Interval' and 'Replicate')['Count'].mean()
avg_count.to_csv('b9_output1.csv', index=True)