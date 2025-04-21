import pandas as pd
df=pd.read_csv('Exam_Table.csv')
replaced= df.replace(' ', '_')
lowercase_columns=df.columns.str.lower()
#replaced.to_csv('b1_output1.csv', index=False)
lowercase_columns.to_csv('b1_output2.csv', index=False)