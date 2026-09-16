# Clasificador KNN

Aplicación de escritorio en Python que usa el algoritmo **K-Nearest Neighbors (KNN)** para predecir si un cliente comprará o no.

La interfaz gráfica fue creada con Tkinter. Para cada predicción se ingresan la edad, el salario, el número de hijos y el valor de `K`.

## Requisitos

- Python 3
- NumPy
- scikit-learn
- Tkinter (incluido normalmente con Python)

## Instalación

```bash
pip install numpy scikit-learn
```

## Ejecución

Desde la carpeta del proyecto, ejecute:

```bash
python main.py
```

## Uso

1. Ingrese la edad, el salario y el número de hijos del cliente.
2. Indique un valor entero positivo para `K`.
3. Seleccione **Predecir**.

El programa entrenará el modelo con el conjunto de datos incluido y mostrará si el cliente probablemente comprará o no.

## Tecnologías

- Python
- Tkinter
- NumPy
- scikit-learn
