
# coding: utf-8

# <h1>Venda de Jogos de Viode Game da História</h1>
# <br>
# Este será meu primeiro projeto de DS, baseado em um tutorial. O dataset foi obtido <a href="https://www.kaggle.com/gregorut/videogamesales">aqui</a>

# In[27]:


#get_ipython().magic('matplotlib inline')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')


# In[6]:


videogames=pd.read_csv('/home/tchellita/Documentos/vgsales.csv')


# In[5]:


videogames.head(10)


# In[7]:


videogames.describe()


# In[8]:


videogames.dtypes


# In[9]:


videogames.shape


# In[10]:


videogames.columns=['Ranking', 'Nome','Plataforma','Ano','Gênero','Editora','Vendas Ameridca do Norte','Vendas EUA',
                   'Vendas Japao','Outras Vendas','Vendas Global']


# In[11]:


videogames.head(10)


# In[12]:


videogames[videogames['Ano'].isnull()].head()


# In[10]:


videogames['Plataforma'].value_counts()


# In[13]:


titulos_lancados = videogames['Plataforma'].value_counts()
titulos_lancados.plot()


# In[14]:


videogames['Plataforma'].value_counts().head(10).plot(kind='bar',figsize=(11,5),grid=False,rot=0,
                                                                        color='green')
plt.title('Os 10 videogames com mais titulos lançados')
plt.xlabel('Videogame')
plt.ylabel('Qtd de jogos lançados')
plt.show()


# In[15]:


top10maisvendidos=videogames[['Nome','Vendas Global']].head(10).set_index('Nome').sort_values('Vendas Global',ascending=True)
top10maisvendidos.plot(kind='barh',figsize=(11,7),grid=False,color='darkred',legend=False)
plt.title('Os 10 videogames mais vendidos no mundo')
plt.xlabel('Total de vendidos(milhoes de dolares)')
plt.show()


# In[16]:


crosstab_vg = pd.crosstab(videogames['Plataforma'], videogames['Gênero'])
crosstab_vg.head()


# In[19]:


crosstab_vg['Total']=crosstab_vg.sum(axis=1)
crosstab_vg.head()


# In[20]:


top10_platforms = crosstab_vg[crosstab_vg['Total'] > 1000].sort_values('Total', ascending = False)


# In[21]:


top10_final = top10_platforms.append(pd.DataFrame(top10_platforms.sum(), columns=['total']).T, ignore_index=False)


# In[29]:


sns.set(font_scale=1)
plt.figure(figsize=(18, 9))
sns.heatmap(top10_final, annot=True, vmax=top10_final.loc[:'PS', :'Strategy'].values.max(), vmin=top10_final.loc[:, :'Strategy'].values.min(), fmt='d')
plt.xlabel('GÊNERO')
plt.ylabel('CONSOLE')
plt.title('QTD DE TÍTULOS POR GÊNERO E CONSOLE')
plt.show()

