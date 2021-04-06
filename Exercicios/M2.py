import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/home/odcolares/Documentos/bike-sharing.csv")
print(df.shape)
print('A media da coluna WindSpeed foi: ', df.windspeed.mean())
print('A media da coluna Temp foi: ', (df.temp.mean()))
print(('Quantos registros existem para o ano de 2011'), df[df.year == 0].shape)
print(('Quantos registros existem para o ano de 2012'), df[df.year == 1].shape)
print(('Ano de 2011:'), df[df.year == 0].total_count.sum())
print(('Ano de 2012:'), df[df.year == 1].total_count.sum())
print(('Lista de media de locacao/estacao do ano: '), df.groupby(['season']).total_count.mean())
print(df.groupby(['hour']).total_count.mean().sort_values(ascending=False))
print(df.groupby(['weekday']).total_count.mean().sort_values(ascending=False))
print(('Quarta'), df[df.weekday == 3].groupby(['hour']).total_count.mean().sort_values(ascending=False))