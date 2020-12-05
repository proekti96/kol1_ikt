#!/usr/bin/env python
# coding: utf-8

# ##### Notebook за трудот "Promise and pitfalls of g-ratio estimation with MRI"
# ***

# Краток опис:
# Овој труд имал за цел да го проучи г-соодносот на фибер влакната, како сооднос на внатрешниот и надворешниот дијаметар на миелинската обвивка на миелинизираниот аксон. Снимањето во живо на овој г-сооднос, го зголемува нашето знаење за нервниот систем, како и способноста да дијагностицираме, следиме и лекуваме болести. Исто така, во рамки на овој труд, се разгледува методологијата за снимање на г-соодносот со Магнетна Резонанца, како и познатите стапици и предизвици со кои може да се соочат луѓето. Трудот ја потенцира големата важност што ја има снимањето со г-соодносот и како истото ни помага да ги разбереме болестите поврзани со миелинската обвивка, да развиеме терапии и да ја следиме прогресијата на заболувањето.

# In[1]:


import numpy as np


# Некои формули од трудот:

# $$
# g = \sqrt \frac {1} {1+\frac{MVF}{AVF}}
# $$

# $ AVF = (1 − MVF)(1 − v_{iso}) v_{ic} $

# $$
# g = \sqrt {1-\frac{MVF}{FVF}}
# $$

# $ MVF = cF + b $

# In[7]:


import plotly.graph_objects as go


# In[1]:


import chart_studio.plotly as py


# In[3]:


import pandas as pd


# In[18]:


import plotly.graph_objects as go
fig = go.Figure(
    data=[
        go.Bar(x=[0.70], y=[0.12]),
        go.Bar(x=[0.70, 0.17, 0.67, 0.75, 0.72, 0.74, 0.67, 0.75], y=[0.12, 0.17, 0.11, 0.15, 0.13, 0.14, 0.17, 0.16])],
    layout_title_text="Histograms Analysis of g-ratio"
)
fig.show()
