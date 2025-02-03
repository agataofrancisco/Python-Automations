import speech_recognition as sr
import pyautogui
import time

def ouvir_comando():
    """Reconhece voz e retorna texto em PT-PT"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("A ouvir...")
        audio = r.listen(source)
    
    try:
        return r.recognize_google(audio, language='pt-PT').lower()
    except:
        return ""

def automatizar_chatgpt():
    """Automatiza interação com ChatGPT via pyautogui"""
    # Abrir navegador (Chrome)
    pyautogui.hotkey('winleft')
    time.sleep(1)
    pyautogui.write('edge')
    pyautogui.press('enter')
    time.sleep(3)
    
    # Acessar ChatGPT 
    pyautogui.write('https://chatgpt.com/')
    pyautogui.press('enter')
    time.sleep(5)  # Tempo para carregamento
    # Escrever mensagem
    pyautogui.write('Oi', interval=0.1)
    pyautogui.press('enter')

def main():
    """Controla fluxo principal"""
    while True:
        comando = ouvir_comando()
        if 'teste' in comando:
            print("Comando reconhecido. Iniciando...")
            automatizar_chatgpt()
            break

if __name__ == "__main__":
    main()