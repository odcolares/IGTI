import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/home/odcolares/Documentos/temperature.csv")
#df.plot(figsize=(10, 5), grid=True);  #passar o arquivo, mudar tamanho, add grid
#df.plot(style='-o', figsize=(10, 5), grid=True) #Add stilo na linha (-o, --, -.)
#df.plot(linewidth=2, figsize=(10, 5), grid=True); #Deixa alinha mais grossa
df.plot(color='red', figsize=(10, 5), grid=True); # add cores
plt.show() #mostrar o arquivo

