# -*- coding: utf-8 -*-
"""Polynomial regresion.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JfnuI2UncRG70ybAaD93Oes3JtKDUHun
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

#Valores de arreglos
x = np.array([108, 115, 106, 97, 95, 91, 97, 83, 83, 78, 54, 67, 56, 53, 61, 115, 81, 78, 30, 45, 99, 32, 25, 28, 90, 89])
y = np.array([95, 96, 95, 97, 93, 94, 95, 93, 92, 86, 73, 80, 65, 69, 77, 96, 87, 89, 60, 63, 95, 61, 55, 56, 94, 93])

#Transformar los datos a un polinomi de grado 1, 2 y 3
transformer = PolynomialFeatures(degree=3, include_bias=False)
x_poly = transformer.fit_transform(x.reshape(-1,1))

#se crea modelo de regresion lineal
modelo = LinearRegression()
#entrenamos al modelo
modelo.fit(x_poly, y)

#datos para hacer predicciones
x_nuevo = np.array([120, 135])

#transformamos los nuevos datos a un polinomio
x_nuevo_poly = transformer.transform(x_nuevo.reshape(-1,1))
#realizamos predicciones
y_predi = modelo.predict(x_nuevo_poly)

#creamos la linea para el polinomio ajustado
x_fit = np.linspace(1,115,100)
x_fit_poly = transformer.transform(x_fit.reshape(-1,1))
y_fit = modelo.predict(x_fit_poly)

#graficamos los datos y el polinomio ajustado
plt.scatter(x, y)
plt.plot(x_fit, y_fit, color='red')
plt.show