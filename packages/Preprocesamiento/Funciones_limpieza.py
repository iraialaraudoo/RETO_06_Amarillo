
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def escalar_numericas_train_test(X_train, X_test, columnas_numericas=None):
    """
    Escala únicamente las columnas numéricas de un DataFrame usando MinMaxScaler.
    Primero ajusta el scaler con el conjunto de entrenamiento y luego transforma
    tanto train como test para evitar data leakage.

    Parámetros
    ----------
    X_train : pd.DataFrame
        DataFrame de entrenamiento con todas las variables.
    X_test : pd.DataFrame
        DataFrame de test con todas las variables.
    columnas_numericas : list, opcional
        Lista de columnas numéricas a escalar. Si no se pasa, se detectan automáticamente.

    Retorna
    -------
    X_train_scaled : pd.DataFrame
        DataFrame de entrenamiento con las columnas numéricas escaladas entre 0 y 1.
    X_test_scaled : pd.DataFrame
        DataFrame de test con las columnas numéricas escaladas usando los parámetros del scaler ajustado en train.
    """
    X_train_copy = X_train.copy()
    X_test_copy = X_test.copy()

    # Detectar columnas numéricas si no se pasan
    if columnas_numericas is None:
        columnas_numericas = X_train_copy.select_dtypes(include=['int64', 'float64']).columns.tolist()

    scaler = MinMaxScaler()
    X_train_copy[columnas_numericas] = scaler.fit_transform(X_train_copy[columnas_numericas])
    X_test_copy[columnas_numericas] = scaler.transform(X_test_copy[columnas_numericas])

    return X_train_copy, X_test_copy


# Función para hacer dummies variables categoricas 

def convertir_a_dummies_train_test(X_train, X_test, columnas_categoricas=None, drop_first=True):
    """
    Convierte columnas categóricas en variables dummies (one-hot encoding), 
    ajustando solo sobre el conjunto de entrenamiento y alineando el test para 
    que tenga exactamente las mismas columnas que el train.

    Parámetros
    ----------
    X_train : pd.DataFrame
        DataFrame de entrenamiento.
    X_test : pd.DataFrame
        DataFrame de test.
    columnas_categoricas : list, opcional
        Lista de columnas categóricas a convertir. Si no se pasa, se detectan automáticamente.
    drop_first : bool, default True
        Si True, elimina la primera categoría de cada variable para evitar multicolinealidad.

    Retorna
    -------
    X_train_dummies : pd.DataFrame
        DataFrame de entrenamiento con las columnas categóricas convertidas a dummies.
    X_test_dummies : pd.DataFrame
        DataFrame de test con las mismas columnas que X_train_dummies, completando con ceros si alguna categoría no existía en test.
    """
    X_train_copy = X_train.copy()
    X_test_copy = X_test.copy()

    # Detectar columnas categóricas si no se pasan
    if columnas_categoricas is None:
        columnas_categoricas = X_train_copy.select_dtypes(include=['object', 'category']).columns.tolist()

    # Convertir a dummies
    X_train_dummies = pd.get_dummies(X_train_copy, columns=columnas_categoricas, drop_first=drop_first)
    X_test_dummies = pd.get_dummies(X_test_copy, columns=columnas_categoricas, drop_first=drop_first)

    # Alinear columnas de test con train
    X_test_dummies = X_test_dummies.reindex(columns=X_train_dummies.columns, fill_value=0)

    return X_train_dummies, X_test_dummies


# Funcion para elegir el mejor umbral para cada modelo
import numpy as np
from sklearn.metrics import f1_score, recall_score, precision_score


def encontrar_mejor_umbral(
    model,
    X_val,
    y_val,
    metrica="f1",
    thresholds=np.arange(0.1, 0.9, 0.01)
):
    """
    Encuentra el mejor umbral según la métrica elegida.
    """

    y_proba = model.predict_proba(X_val)[:, 1]

    mejor_umbral = 0.5
    mejor_score = 0

    for t in thresholds:
        y_pred = (y_proba >= t).astype(int)

        if metrica == "f1":
            score = f1_score(y_val, y_pred)
        elif metrica == "recall":
            score = recall_score(y_val, y_pred)
        elif metrica == "precision":
            score = precision_score(y_val, y_pred)
        else:
            raise ValueError("Métrica no válida")

        if score > mejor_score:
            mejor_score = score
            mejor_umbral = t

    return mejor_umbral, mejor_score