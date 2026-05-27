
def whisper_cipher(text: str, shift: int) -> str:
    """
    Escribe una función que cree un cifrado simple desplazando
    las letras de una cadena una cantidad dada. Los caracteres
    no alfabéticos deben permanecer iguales.
    """
    result = ""
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].isupper():
                result += chr(((ord(text[i]) - ord("A") + shift) % 26)
                              + ord("A"))
            else:
                result += chr(((ord(text[i]) - ord("a") + shift) % 26)
                              + ord("a"))
        else:
            result += text[i]
    return result


if __name__ == "__main__":
    print(whisper_cipher("xyz", 3))
