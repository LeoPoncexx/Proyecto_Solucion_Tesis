import subprocess

# ID del archivo en Google Drive (reemplazado con el ID correcto)
file_id = "162PVVTaXBjiv3plekaOv4y_CPBx3k3Hm"  # ID de tu archivo
output_path = "openhermes.gguf"  # Archivo descargado en la raíz del proyecto

# Descargar el archivo usando gdown
print("⬇️  Descargando modelo desde Google Drive...")
try:
    subprocess.run(["gdown", "--id", file_id, "--output", output_path], check=True)
    print(f"✅ Modelo descargado en: {output_path}")
except subprocess.CalledProcessError:
    print("❌ Error al descargar el modelo. Verifica el ID o la conexión a internet.")
