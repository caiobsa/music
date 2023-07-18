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
    Simplesmente clique em uma nota e escolha se você quer calcular o campo harmônico maior ou menor.
    """)

    nota = st.empty()
    tipo = st.empty()
    notas = ["C", "D", "E", "F", "G", "A", "B"]
    tipos = ["maior", "menor"]

    nota_selecionada = st.session_state.get('nota_selecionada', None)
    tipo_selecionado = st.session_state.get('tipo_selecionado', None)

    if nota.button("C"):
        nota_selecionada = "C"
        st.session_state['nota_selecionada'] = nota_selecionada

    elif nota.button("D"):
        nota_selecionada = "D"
        st.session_state['nota_selecionada'] = nota_selecionada

    elif nota.button("E"):
        nota_selecionada = "E"
        st.session_state['nota_selecionada'] = nota_selecionada

    elif nota.button("F"):
        nota_selecionada = "F"
        st.session_state['nota_selecionada'] = nota_selecionada

    elif nota.button("G"):
        nota_selecionada = "G"
        st.session_state['nota_selecionada'] = nota_selecionada

    elif nota.button("A"):
        nota_selecionada = "A"
        st.session_state['nota_selecionada'] = nota_selecionada

    elif nota.button("B"):
        nota_selecionada = "B"
        st.session_state['nota_selecionada'] = nota_selecionada

    if tipo.button("Maior"):
        tipo_selecionado = "maior"
        st.session_state['tipo_selecionado'] = tipo_selecionado

    elif tipo.button("Menor"):
        tipo_selecionado = "menor"
        st.session_state['tipo_selecionado'] = tipo_selecionado

    if nota_selecionada and tipo_selecionado:
        try:
            campo_harmonico = get_campo_harmonico(nota_selecionada, tipo_selecionado)
            cols = st.columns(7)
            for i, nota in enumerate(campo_harmonico):
                cols[i].markdown(f"## {nota}", unsafe_allow_html=True)
        except KeyError:
            st.write("Ocorreu um erro ao calcular o campo harmônico. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
