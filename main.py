# %% [markdown]
# # API JUEGOS OLIMPICOS

# %%
import pandas as pd
import numpy as np
from fastapi import FastAPI

# %% [markdown]
# INSTANCIANDO FASTAPI

# %%
app = FastAPI()

# %% [markdown]
# CARGAR DATASETS

# %%
df = pd.read_parquet('Data/Datasets.parquet')

# %% [markdown]
# DECORADOR

# %% [markdown]
# FUNCIONES

# %%
app.get("/")
def index():
    return{"API:online"}

# %%
@app.get('/medals.counts/{pais}')
def medal_contury(pais:str):
    filtro = df[df['italy']==pais]
    medals =filtro[medals].value_counts()
    dic = {}
    for i in range(len(medals)):
     dic[medals.index [i]] = int(medals.values[i])
    return dic    

# %%
@app.get('/medals.counts/{year}')
def medal_contury(year:str):
    filtro = df[df['Team']==year]
    medals =filtro[medals].value_counts()
    dic = {}
    for i in range(len(medals)):
     dic[medals.index [i]] = int(medals.values[i])
    return dic    

# %%
medal_contury(2012)

# %%
@app.get("/medals.counts/{Nombre}")
def athletes(nombre:str):
    filtro = df[df['Name']==nombre]
    dic={}
    if filtro == 0:
        return {'Error':'Revisa los datos ingresados'}
    dic['nombre']=nombre
    dic['sexo']=filtro['sex'].values[0]
    dic['Edad']=filtro['Age'].values[0]
    dic['pais']=list(filtro['Team'].values_counts().index)
    dic['Juegos']=list(filtro['Games'].value_counts().index)
    dic['Eventos']=list(filtro['Event'].value_counts().index)
    medallas={}
    for i in range(len(filtro['Medal'].value_counts)):
        medallas[filtro['Medal'].value_counts().index[i]]=filtro['Medal'].value_counts().values[i]
    dic['Medallas'] = medallas
    return dic


