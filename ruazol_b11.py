
import pandas as pd
df=pd.read_csv('Exam_Table.csv')

df.duplicated(subset=['Species', 'Observer', 'Interval', 'Replicate'], keep=False)
duplicated=pd.DataFrame(df.duplicated)
duplicated.to_csv('b11_output1.csv', index=False)
#AttributeError: 'function' object has no attribute 'to_csv'


