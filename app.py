import streamlit as st

# Dicionário para mapear notas musicais aos seus campos harmônicos
CAMPOS_HARMONICOS_MAIOR = {
    "C": ["C", "D", "E", "F", "G", "A", "B"],
    "D": ["D", "E", "F#", "G", "A", "B", "C#"],
    "E": ["E", "F#", "G#", "A", "B", "C#", "D#"],
    "F": ["F", "G", "A", "A#", "C", "D", "E"],
    "G": ["G", "A", "B", "C", "D", "E", "F#"],
    "A": ["A", "B", "C#", "D", "E", "F#", "G#"],
    "B": ["B", "C#", "D#", "E", "F#", "G#", "A#"],
}

CAMPOS_HARMONICOS_MENOR = {
    "C": ["C", "D", "D#", "F", "G", "G#", "A#"],
    "D": ["D", "E", "F", "G", "A", "A#", "C"],
    "E": ["E", "F#", "G", "A", "B", "C", "D"],
    "F": ["F", "G", "G#", "A#", "C", "C#", "D#"],
    "G": ["G", "A", "A#", "C", "D", "D#", "F"],
    "A": ["A", "B", "C", "D", "E", "F", "G"],
    "B": ["B", "C#", "D", "E", "F#", "G", "A"],
}

CAMPOS_HARMONICOS_SETIMA_MAIOR = {
    "C": ["C", "D", "E", "F", "G", "A", "B", "C"],
    "D": ["D", "E", "F#", "G", "A", "B", "C#", "D"],
    "E": ["E", "F#", "G#", "A", "B", "C#", "D#", "E"],
    "F": ["F", "G", "A", "A#", "C", "D", "E", "F"],
    "G": ["G", "A", "B", "C", "D", "E", "F#", "G"],
    "A": ["A", "B", "C#", "D", "E", "F#", "G#", "A"],
    "B": ["B", "C#", "D#", "E", "F#", "G#", "A#", "B"],
}

CAMPOS_HARMONICOS_SETIMA_MENOR = {
    "C": ["C", "D", "D#", "F", "G", "G#", "A#", "C"],
    "D": ["D", "E", "F", "G", "A", "A#", "C", "D"],
    "E": ["E", "F#", "G", "A", "B", "C", "D", "E"],
    "F": ["F", "G", "G#", "A#", "C", "C#", "D#", "F"],
    "G": ["G", "A", "A#", "C", "D", "D#", "F", "G"],
    "A": ["A", "B", "C", "D", "E", "F", "G", "A"],
    "B": ["B", "C#", "D", "E", "F#", "G", "A", "B"],
}

ESCALA_PENTATONICA_MAIOR = {
    "C": ["C", "D", "E", "G", "A"],
    "D": ["D", "E", "F#", "A", "B"],
    "E": ["E", "F#", "G#", "B", "C#"],
    "F": ["F", "G", "A", "C", "D"],
    "G": ["G", "A", "B", "D", "E"],
    "A": ["A", "B", "C#", "E", "F#"],
    "B": ["B", "C#", "D#", "F#", "G#"],
}

ESCALA_PENTATONICA_MENOR = {
    "C": ["C", "D#", "F", "G", "A#"],
    "D": ["D", "F", "G", "A", "C"],
    "E": ["E", "G", "A", "B", "D"],
    "F": ["F", "G#", "A#", "C", "D#"],
    "G": ["G", "A#", "C", "D", "F"],
    "A": ["A", "C", "D", "E", "G"],
    "B": ["B", "D", "E", "F#", "A"],
}

def get_escala(nota, tipo):
    """ Retorna a escala pentatônica maior ou menor de uma nota musical """
    if tipo == "maior":
        return ESCALA_PENTATONICA_MAIOR[nota]
    elif tipo == "menor":
        return ESCALA_PENTATONICA_MENOR[nota]
    else:
        return None

def get_campo_harmonico(nota, tipo):
    """
