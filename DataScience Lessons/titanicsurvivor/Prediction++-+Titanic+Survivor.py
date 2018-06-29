
# coding: utf-8

# In[1]:


get_ipython().magic('matplotlib inline')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')


# In[56]:


titanicsurvivors=pd.read_csv('titanic-data.csv')


# <h1> First heurist </h1>        
#     Here's a simple heuristic to start off:
#        <ul>
#        <li>If the passenger is female, your heuristic should assume that the
#        passenger survived.</li>
#        <li>If the passenger is male, you heuristic should
#        assume that the passenger did not survive.</li>
#     

# In[21]:


predictions={} 
for passenger_index, passenger in titanicsurvivors.iterrows():
    passenger_id = passenger['PassengerId']
    if passenger['Sex']=='male':
        predictions[passenger_id]=0
    else:
        predictions[passenger_id]=1


# In[28]:


countCorrect=0
for passenger_index, passenger in titanicsurvivors.iterrows():
    passenger_id=passenger['PassengerId']
    if passenger['Survived']==predictions[passenger_id]:
        countCorrect=countCorrect+1


# In[32]:


titanicsurvivors.shape


# In[35]:


prediction_perc=countCorrect/891


# In[55]:


prediction_perc


#  <h1>Here's the algorithm, predict the passenger survived if:</h1>
#  <ul>
#     <li>If the passenger is female or</li>
#     <li>if his/her socioeconomic status is high AND if the passenger is under 18</li>
#  </ul>

# In[58]:


for passenger_index, passenger in titanicsurvivors.iterrows():
    passenger_id = passenger['PassengerId']
    if passenger['Pclass']==1 and passenger['Age']<18:
        predictions[passenger_id]=1
    else:
        if passenger['Sex']=='female':
            predictions[passenger_id]=1
        else:
            predictions[passenger_id]=0


# In[59]:


countCorrect=0
for passenger_index, passenger in titanicsurvivors.iterrows():
    passenger_id=passenger['PassengerId']
    if passenger['Survived']==predictions[passenger_id]:
        countCorrect=countCorrect+1


# In[60]:


prediction_perc=countCorrect/891


# In[61]:


prediction_perc

