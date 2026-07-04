from deep_translator import GoogleTranslator

def coditranslate(text: str, target_lang: str):
    try:
        translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
        return translated
    except Exception as e:
        return f"Translation Error: {e}"

