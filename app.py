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

    st.markdown("""
    Este aplicativo permite que você calcule o campo harmônico maior ou menor de uma nota musical.
    Simplesmente selecione uma nota e escolha se você quer calcular o campo harmônico maior ou menor.
    """)

    nota = st.selectbox("Escolha uma nota musical:", ["C", "D", "E", "F", "G", "A", "B"])
    tipo = st.selectbox("Escolha o tipo de campo harmônico:", ["maior", "menor"])

    if st.button('Calcular'):
        try:
            campo_harmonico = get_campo_harmonico(nota, tipo)

            cols = st.beta_columns(7)
            for i, nota in enumerate(campo_harmonico):
                cols[i].markdown(f"## {nota}", unsafe_allow_html=True)
        except KeyError:
            st.write("Ocorreu um erro ao calcular o campo harmônico. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
