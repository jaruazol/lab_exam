import pandas as pd
df=pd.read_csv('Exam_Table.csv')
replaced= df.replace(' ', '_')
df.columns.str.lower()

species_count =pd.Series(df['Species'].value_counts())

#saving file
species_count.to_csv('b4_output1.csv', index=True)