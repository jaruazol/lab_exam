import pandas as pd
df=pd.read_csv('Exam_Table.csv')
replaced= df.replace(' ', '_')
df.columns.str.lower()

genus_P=df[df['Genus']=='Pomacentrus']

genus_P.to_csv('b3_output1.csv', index=False)
