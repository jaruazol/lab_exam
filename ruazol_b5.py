
import pandas as pd
df=pd.read_csv('Exam_Table.csv')

avg_size =df.groupby('Species')['Size Est (cm)'].mean()

avg_size.to_csv('b5_output1.csv', index=True)