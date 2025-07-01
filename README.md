# 🧠 Asistente de Educación Financiera con LLM (Local)

Este proyecto implementa un asistente educativo local utilizando un modelo de lenguaje **GGUF** optimizado para **CPU** y una interfaz web desarrollada con **Flask**. Está orientado a fortalecer la educación financiera de estudiantes peruanos de forma autónoma, sin depender de conexión a APIs externas.

---

## ⚙️ Tecnologías utilizadas

- Python 3.10+
- Flask
- llama-cpp-python
- Modelo local `openhermes.gguf`
- gdown (para descarga automatizada del modelo desde Google Drive)

---

## 📁 Estructura del proyecto

```
Page_Tesis/
├── static/
│   └── styles.css
├── templates/
│   └── index.html
├── openhermes.gguf  ← Modelo descargado (al ejecutar el script)
├── app.py           ← Código principal de la app Flask
├── download_model.py ← Script para descargar el modelo GGUF
├── requirements.txt ← Dependencias necesarias
```

---

## 🚀 Guía de uso (paso a paso)

### 1. Clonar el repositorio

Abre una terminal y ejecuta:

```bash
git clone https://github.com/LeoPoncexx/Proyecto_Solucion_Tesis.git
cd Proyecto_Solucion_Tesis
```

> Asegúrate de tener Git y Python instalados previamente.

---

### 2. Instalar las dependencias

Ejecuta:

```bash
pip install -r requirements.txt
```

Esto instalará `Flask`, `llama-cpp-python`, `gdown`, entre otros paquetes necesarios para el funcionamiento del asistente.

---

### 3. Descargar el modelo GGUF

Para usar el modelo local, necesitas descargarlo desde Google Drive. Ya tienes un script listo para hacerlo:

```bash
python download_model.py
```

Esto descargará automáticamente el archivo `openhermes.gguf` en la raíz del proyecto.

> Asegúrate de tener conexión a internet para este paso.

---

### 4. Ejecutar la aplicación Flask

Cuando el modelo esté descargado y las dependencias instaladas, simplemente corre:

```bash
python app.py
```

La app estará disponible en:  
📍 http://localhost:5000

---

### 5. Interactuar con el asistente

Desde el navegador, podrás:
- Hacer preguntas relacionadas con **educación financiera**.
- Usar un entorno 100% local y seguro.
- Consultar temas como ahorro, AFP, presupuestos, inversiones, deudas, entre otros.

---

## ¿Qué hace `download_model.py`?

Este script descarga el modelo `openhermes.gguf` desde un enlace público de Google Drive utilizando `gdown`. No necesitas modificarlo, solo ejecutarlo si no tienes el modelo en tu carpeta.

---

## Autores

- **Hiver Leonardo Ponce Contreras**  
- **Niwell Gonzalo Quispe Lingán**  
Facultad de Ingeniería de Sistemas – Universidad Privada del Norte

---

## Licencia

Este proyecto está destinado a fines educativos y académicos. No se permite su uso comercial sin autorización.
