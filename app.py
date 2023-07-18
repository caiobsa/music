def get_campo_harmonico(nota, tipo):
    """ Retorna o campo harmônico maior ou menor de uma nota musical """
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
            escala = get_escala(nota, tipo.split(" ")[1])
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
