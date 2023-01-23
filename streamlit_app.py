# https://georgrmat-law-fitting-streamlit-app-ufa09l.streamlit.app/
import streamlit as st
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

proba_laws = {"poisson": stats.poisson,
              "nbinom": stats.nbinom}

N = st.slider('Number of simulations', 1, 100000, 100)
N2 =  st.slider('Sample size', 1, 500, 100)

law = st.radio("Choose your Probability Law", ["poisson", "nbinom"])

if law == "poisson":
  res_mean = []
  mu = st.number_input("mu", step = 10)
  for i in range(N):
    x = proba_laws[law].rvs(mu = mu, size = N2)    
    res_mean.append(np.mean(x))
  fig, ax = plt.subplots()
  b = st.number_input("bins", step = 10)
  ax.hist(res_mean, density = True, bins = b, edgecolor = (1, 1, 1))
  st.pyplot(fig)

    
elif law == "nbinom":
  res_p = []
  res_n = []
  n = st.slider('n', 1, 1000, 100)
  p = st.number_input("p", step = 0.1)
  for i in range(N):
    x = proba_laws[law].rvs(n = n, p = p, size = N2)
    p_hat = np.mean(x)/np.var(x)
    res_p.append(p_hat)
    res_n.append(np.mean(x)*p_hat/(1-p_hat))
  fig, ax = plt.subplots(2, 1)
  b2 = st.number_input("bins", step = 10)
  ax[0].hist(res_p, density = True, bins = b2, edgecolor = (1, 1, 1))
  ax[1].hist(res_n, density = True, bins = b2, edgecolor = (1, 1, 1))
  st.pyplot(fig)


#st.write("You have chosen", N, 'simulations')

"""
fig, ax = plt.subplots(2, 1)
b = st.number_input("bins", step = 10)
ax[0].hist(res_mean, density = True, bins = b, edgecolor = (1, 1, 1))
ax[1].hist(res_var, density = True, bins = b, edgecolor = (1, 1, 1))
st.pyplot(fig)
"""


#uploaded_file = None
#uploaded_file = st.file_uploader("Choose a file")
