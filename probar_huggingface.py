from flask import Flask, request, jsonify, render_template
from llama_cpp import Llama
import time

app = Flask(__name__)

# Ruta al modelo GGUF
modelo_path = "C:/Users/hlpc0/Desktop/tesis/Page_Tesis/openhermes.gguf"

# Número de capas en GPU (ajustado para GTX 1650)
gpu_layers = 32

# Cargar modelo
print("\n🧠 Cargando modelo...")
llm = Llama(
    model_path=modelo_path,
    n_ctx=1024,
    n_threads=6,
    n_batch=64,
    n_gpu_layers=gpu_layers
)
print("✅ Modelo cargado.\n")

if gpu_layers > 0:
    print(f"🔍 GPU activada con {gpu_layers} capas (si tu instalación tiene cuBLAS).")
else:
    print("⚠️ Ejecutando completamente en CPU.")

# Prompt del sistema optimizado
system_prompt = (
    "Eres un asistente experto en educación financiera en Perú. "
    "Responde solo en español, de forma clara, breve y con frases separadas por saltos de línea. "
    "Evita explicaciones largas. Resume en máximo 2 frases.\n"
)
historial = system_prompt

# Respuestas predefinidas
respuestas_directas = {
    "hola": "¡Hola! ¿En qué puedo ayudarte sobre educación financiera?",
    "buenas": "¡Buenas! ¿Quieres saber sobre ahorro, AFP, presupuesto u otro tema?",
    "como estas": "Estoy lista para ayudarte con tu educación financiera. 😊",
    "de que trata esta pagina": "Esta página está diseñada para ayudarte a mejorar tu educación financiera con ayuda de una IA.",
    "quien te creo": "Fui creada por Hiver Leonardo Ponce Contreras y Niwell Gonzalo Quispe Lingán."
}

# Función para verificar si el tema es financiero
def es_pregunta_financiera(texto):
    temas_clave = [
        "ahorro", "finanzas", "dinero", "presupuesto", "gasto", "ingreso", "afp",
        "cts", "interés", "préstamo", "tarjeta", "crédito", "débito", "deuda",
        "educación financiera", "inversión", "banco", "ahorrar", "impuesto", "plan financiero",
        "economía personal", "morosidad", "historial crediticio", "billetera digital", "yape", "plin"
    ]
    return any(palabra in texto.lower() for palabra in temas_clave)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global historial
    user_input = request.json.get("message", "").lower().strip()

    # Verificar respuestas cortas predefinidas
    for frase, respuesta in respuestas_directas.items():
        if frase in user_input:
            return jsonify({"reply": respuesta, "tiempo": 0})

    # Verificar si la pregunta es de tema financiero
    if not es_pregunta_financiera(user_input):
        return jsonify({
            "reply": "Solo puedo responder preguntas relacionadas con educación financiera en Perú. Por favor, reformula tu consulta.",
            "tiempo": 0
        })

    # Preparar prompt
    prompt = historial + f"Usuario: {user_input}\nAsistente:"
    inicio = time.time()

    # Generar respuesta
    respuesta = llm(
        prompt,
        max_tokens=80,
        temperature=0.2,
        top_p=0.9,
        stop=["Usuario:", "Asistente:"]
    )

    tiempo = round(time.time() - inicio, 2)
    texto = respuesta["choices"][0]["text"].strip()

    # Truncar si excede
    if len(texto) > 350:
        texto = texto[:350].rsplit(".", 1)[0] + "."

    # Agregar al historial
    historial += f"Usuario: {user_input}\nAsistente: {texto}\n"

    # Limpiar historial si es muy largo
    if historial.count("Usuario:") > 15:
        historial = system_prompt

    return jsonify({"reply": texto, "tiempo": tiempo})

if __name__ == "__main__":
    app.run(debug=True)
