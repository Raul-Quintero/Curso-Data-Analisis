#!/usr/bin/env python
# coding: utf-8

# # Proyecto 2

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


sldb=pd.read_csv("synergy_logistics_database.csv")


# In[4]:


sldb


# ## Opción 1) Rutas de importación y exportación.

# **Synergy logistics está considerando la posibilidad de enfocar sus esfuerzos en las 10 rutas más
# demandadas. Acorde a los flujos de importación y exportación**

# 1. Calculamos la suma de las rutas sin importar si es importación o expoertación, segunsu origen y destino (esta sera la ruta), por medio de transporte (forma que se traslado).

# In[5]:


rutas_ventas=sldb.groupby(["origin","destination", "transport_mode"]).sum()
rutas_ventas


# In[6]:


orden_rutas_ventas=pd.DataFrame(rutas_ventas)
orden_rutas_ventas=orden_rutas_ventas.sort_values(by=['total_value'], ascending=False)


# ### ¿cuáles son esas 10 rutas? 

# In[7]:


top10_rutas_ventas=orden_rutas_ventas[0:10]
t=top10_rutas_ventas["total_value"]
top10_rutas_ventas=t.reset_index()
top10_rutas_ventas


# In[ ]:





# #### ¿le conviene implementar esa estrategia?
# #### ¿porqué?

# - Para esto calculamos el porcentaje de la suma del top 10 rutas con respecto a las ventas totales

# In[8]:


#Ventas totales
rutas_ventas['total_value'].sum()

#Ventastop 10
top10_rutas_ventas['total_value'].sum()

#Porcentaje
porcentaje=(top10_rutas_ventas['total_value'].sum()/rutas_ventas['total_value'].sum())*100
porcentaje


# **El top 10 de las rutas de comercio es sólo del 27.36% por lo que no es conveniente enfocarnos sólo en estas. **

# In[ ]:





# ## Opción 2) Medio de transporte utilizado.

# *** ¿Cuáles son los 3 medios de transporte
# más importantes para Synergy logistics considerando el valor de las
# importaciones y exportaciones? ***

# -Para esto realizamos la suma de las ventas por medio de trasporte y los ordenamos de mayor a menor.

# In[9]:


tipos_transporte_sum=sldb.groupby("transport_mode").sum()
transporte_sum=tipos_transporte_sum.sort_values(by=['total_value'], ascending=False)


# In[10]:


#Total medios de tranporte
total_transporte = transporte_sum['total_value'].sum()
total_transporte


# In[11]:


transporte_sum["Procentaje %"]= (transporte_sum['total_value']/total_transporte)*100
transporte_sum


# - Presentamos los resulatos en formato de tabla y solo los 3 primeros (top 3)

# In[12]:


transporte_sum.drop(["register_id","year"], axis=1)


# In[13]:


top3_medios_de_transporte=transporte_sum.drop(["register_id","year"], axis=1)[0:3]
top3_medios_de_transporte


# *Los metodos de trasporte con mejores ventas son: mar, ferrocarril, aire. Por aire, es donde obtenemos casi el 50% de las ganancias*

# In[ ]:





# **¿Cuál es medio de transporte que podrían
# reducir?**

# In[30]:


#Columnas inesesarias
min_transporte=transporte_sum.drop(["register_id","year"], axis=1)

#Valor mínimo del medio de transporte 
min_medios_de_transporte=min_transporte.iloc[-1]

#Formato de tabla
min_medios_de_transporte.reset_index()


# *Sólo queda el metodo de transporte por tierra o carretera el porcentaje de este con respecto a las ventas es de 15.42% asi que es una buena cantidad, por lo que se recomendaria no eliminar algun tipo de transporte*

# In[ ]:





# ## Opción 3) Valor total de importaciones y exportaciones. 

# #### Si Synergy Logistics quisiera enfocarse en los países que le generan el 80% del valor de las exportaciones e importaciones 

# - **¿en qué grupo de países debería enfocar sus esfuerzos?**

# In[58]:


paises=sldb.groupby("origin").sum().drop(["register_id","year"], axis=1)


# In[59]:


#Porcentaje
paises['Porcentaje']= (paises['total_value']/total_ventas)*100
ordenamineto=paises.sort_values(by=['total_value'], ascending=False)
ordenamineto["sum_acumulada"]=ordenamineto.cumsum()["Porcentaje"]


# In[81]:


paises_ventas_90 = ordenamineto[ordenamineto["sum_acumulada"]<=91]
paises_ventas_90.count()
paises_ventas_90


# In[64]:


ordenamineto.count()


# In[ ]:





# In[ ]:




