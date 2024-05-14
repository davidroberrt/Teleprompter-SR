import speech_recognition as sr
import time

def display_text(text):
    print(text)

def listen_for_speech():
    # Inicializa o reconhecedor de fala
    recognizer = sr.Recognizer()

    # Configura o microfone como a fonte de áudio
    with sr.Microphone() as source:
        print("Por favor, fale...")
        recognizer.adjust_for_ambient_noise(source)  # Ajusta para o ruído ambiente
        audio = recognizer.listen(source, timeout=5)  # Escuta até 5 segundos de áudio

    try:
        # Usa o reconhecedor de fala para converter o áudio em texto
        text = recognizer.recognize_google(audio, language="pt-BR")
        return text
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
        return ""
    except sr.RequestError as e:
        print(f"Erro no serviço de reconhecimento de fala: {e}")
        return ""

def teleprompter(text):
    lines = text.split('\n')
    num_lines = len(lines)
    current_line = 0

    while current_line < num_lines:
        display_text('\n'.join(lines[current_line:]))
        time.sleep(1)  # Aguarda um segundo

        # Captura a fala do usuário
        spoken_text = listen_for_speech().lower()

        # Verifica se a fala do usuário corresponde à linha atual do teleprompter
        if spoken_text in lines[current_line].lower():
            current_line += 1

# Texto do teleprompter
text = """Olá! Bem-vindo ao Teleprompter de Fala.
Aqui ficará as notícias...
Pressione Ctrl+C para sair.
Por momento será via terminal, mas irei atualizar para GUI Interface"""

# Chama a função do teleprompter com o texto
teleprompter(text)
