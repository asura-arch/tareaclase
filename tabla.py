mport numpy as np
from sklearn.neighbors import KNeighborsClassifier
# Datos de entrenamiento
matrizx= np.array([[0, 0],
              [4, 1],
              [1, 0],
              [4, 1],
              [20, 3],
              [4, 1],
              [0, 3],
              [1, 0]])
# Clases correspondientes
y = np.array([0, 0, 1, 1, 1, 0, 3, 4])

knn = KNeighborsClassifier(n_neighbors=1, metric='manhattan')

new_case = np.array([[2.5, 2.5]])
predicted_class = knn.predict(new_case)

print(f"La clase predicha para el caso {new_case[0]} es: 
      {predicted_class[0]}")


