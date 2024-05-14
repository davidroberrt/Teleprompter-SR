import speech_recognition as sr

def listen_for_speech(recognizer, microphone):
    with microphone as source:
        print("Pode falar...")
        audio = recognizer.listen(source, timeout=0)

    try:
        text = recognizer.recognize_google(audio, language="pt-BR")
        print("Texto reconhecido: {}".format(text))
        return text.lower()
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio.")
        return ""
    except sr.RequestError as e:
        print(f"Erro no serviço de reconhecimento de fala: {e}")
        return ""

def display_text(current_text):
    print(current_text)
def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # Trechos do teleprompter
    trechos = [
        "Olá e bem-vindo ao nosso teleprompter de notícias",
        "Hoje as principais notícias são",
        "Lançamento do novo produto da empresa",
        "Previsão do tempo para o final de semana",
        "Fique atento para mais notícias ao longo do dia."
    ]

    current_trecho = 0

    print("Bem-vindo ao Teleprompter de Texto")

    while current_trecho < len(trechos):
        display_text(trechos[current_trecho])
        spoken_text = listen_for_speech(recognizer, microphone)
        if spoken_text and spoken_text == trechos[current_trecho].lower():
            current_trecho += 1

if __name__ == "__main__":
    main()
