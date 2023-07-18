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

def get_campo_harmonico(nota, tipo):
    """ Retorna o campo harmônico maior ou menor de uma nota musical """
    if tipo == "maior":
        return CAMPOS_HARMONICOS_MAIOR[nota]
    elif tipo == "menor":
        return CAMPOS_HARMONICOS_MENOR[nota]
    else:
        return None

def main():
    st.title('Campo Harmônico')

    nota = st.text_input("Digite uma nota musical (C, D, E, F, G, A, B):")

    if st.button('Calcular'):
        try:
            campo_maior = get_campo_harmonico(nota.upper(), "maior")
            campo_menor = get_campo_harmonico(nota.upper(), "menor")

            st.write(f"Campo harmônico maior de {nota}: {', '.join(campo_maior)}")
            st.write(f"Campo harmônico menor de {nota}: {', '.join(campo_menor)}")
        except KeyError:
            st.write("Por favor, insira uma nota válida (C, D, E, F, G, A, B).")

if __name__ == "__main__":
    main()

