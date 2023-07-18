import streamlit as st

# Dicionário para mapear notas musicais aos seus campos harmônicos
CAMPOS_HARMONICOS_MAIOR = {
    "C": ["C", "Dm", "Em", "F", "G", "Am", "Bdim"],
    "D": ["D", "Em", "F#m", "G", "A", "Bm", "C#dim"],
    "E": ["E", "F#m", "G#m", "A", "B", "C#m", "D#dim"],
    "F": ["F", "Gm", "Am", "Bb", "C", "Dm", "Edim"],
    "G": ["G", "Am", "Bm", "C", "D", "Em", "F#dim"],
    "A": ["A", "Bm", "C#m", "D", "E", "F#m", "G#dim"],
    "B": ["B", "C#m", "D#m", "E", "F#", "G#m", "A#dim"],
}

CAMPOS_HARMONICOS_MENOR = {
    "C": ["Cm", "Ddim", "Eb", "Fm", "Gm", "Ab", "Bb"],
    "D": ["Dm", "Edim", "F", "Gm", "Am", "Bb", "C"],
    "E": ["Em", "F#dim", "G", "Am", "Bm", "C", "D"],
    "F": ["Fm", "Gdim", "Ab", "Bbm", "Cm", "Db", "Eb"],
    "G": ["Gm", "Adim", "Bb", "Cm", "Dm", "Eb", "F"],
    "A": ["Am", "Bdim", "C", "Dm", "Em", "F", "G"],
    "B": ["Bm", "C#dim", "D", "Em", "F#m", "G", "A"],
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
    if tipo == "pentatônica maior":
        return ESCALA_PENTATONICA_MAIOR[nota]
    elif tipo == "pentatônica menor":
        return ESCALA_PENTATONICA_MENOR[nota]
    else:
        return None

def get_campo_harmonico(nota, tipo):
    """ Retorna o campo harmônico maior, menor, sétima maior ou sétima menor de uma nota musical """
    if tipo == "maior":
        return CAMPOS_HARMONICOS_MAIOR[nota]
    elif tipo == "menor":
        return CAMPOS_HARMONICOS_MENOR[nota]
    elif tipo == "sétima maior":
        return CAMPOS_HARMONICOS_SETIMA_MAIOR[nota]
    elif tipo == "sétima menor":
        return CAMPOS_HARMONICOS_SETIMA_MENOR[nota]
    else:
        return None

def main():
    st.title('Campo Harmônico e Escalas Pentatônicas')

    st.markdown("""
    Este aplicativo permite que você calcule o campo harmônico e a escala pentatônica de uma nota musical.
    Simplesmente selecione uma nota e escolha o tipo de campo harmônico ou escala que você deseja calcular.
    """)

    nota = st.selectbox("Escolha uma nota musical:", ["C", "D", "E", "F", "G", "A", "B"])
    tipo = st.selectbox("Escolha o tipo:", ["maior", "menor", "sétima maior", "sétima menor", "pentatônica maior", "pentatônica menor"])

    try:
        if "pentatônica" in tipo:
            escala = get_escala(nota, tipo)
            cols = st.columns(5)
            for i, nota in enumerate(escala):
                cols[i].markdown(f"## {nota}", unsafe_allow_html=True)
        else:
            campo_harmonico = get_campo_harmonico(nota, tipo)
            cols = st.columns(len(campo_harmonico))
            for i, nota in enumerate(campo_harmonico):
                cols[i].markdown(f"## {nota}", unsafe_allow_html=True)
    except KeyError:
        st.write("Ocorreu um erro ao calcular o campo harmônico ou a escala. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
