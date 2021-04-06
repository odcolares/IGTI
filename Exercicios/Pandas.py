import pandas as pd

df = pd.read_csv("/home/odcolares/Documentos/temperature.csv")
#print(df)
#n = 3
#print(df.tail(n))
#print(df.head(n))
#print(df.columns)
#print(df.describe())
#print(df.info( ))

#print(df[['date', 'classification']]) #Acessando multiplas coluna
#print(df.iloc[:, 1]) #Acessando atraves de indices
#print(df.loc[:, ['temperatura', 'classification']]) #Acessando multiplas atraves de strings
#print(df.loc[:, 'temperatura']) #Acessando coluna
#df['date'] = pd.to_datetime(df['date']) #Trans o tipo da coluna date p/ datetime
#df = df.set_index('date') #Setando o indice


#print(df[df['temperatura'] > 28]) #indexacao boleana filtrando elementos das linhas
#print(df[df['classification'] == 'muito quente']) #indexacao boleana filtrando elementos das linhas

#print(df.sort_values(by='classification')) #ordena forma crescente por coluna
print(df.sort_values(by=['classification', 'temperatura'])) #ordena forma crescente por multiplas coluna

