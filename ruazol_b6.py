import pandas as pd
df=pd.read_csv('Exam_Table.csv')

species_max=df['Species'].value_counts().idxmax()
species_max.to_csv('b6_output1.csv', index=False)