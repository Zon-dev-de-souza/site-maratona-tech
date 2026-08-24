import streamlit as st

from system import analisar_privacidade, proteger_texto
from ia import analisar_com_ia


st.set_page_config(
    page_title="Proteja seu Prompt",
    page_icon="🛡️",
    layout="centered"
)


st.title("🛡️ Proteja seu Prompt")

st.write(
    "Analise as informações que você pretende compartilhar "
    "com uma inteligência artificial."
)


texto = st.text_area(
    "Cole aqui o texto que você pretende enviar para uma IA:",
    height=200,
    placeholder="Exemplo: Tenho 16 anos e estudo na escola..."
)


if st.button("Analisar texto", type="primary"):

    if not texto.strip():
        st.warning("Digite ou cole algum texto antes de analisar.")

    else:
        alertas = analisar_privacidade(texto)
        texto_protegido = proteger_texto(texto)

      
        # RESULTADO
        st.subheader("Análise inicial")

        if alertas:
            st.warning(
                f"Foram encontradas {len(alertas)} "
                f"possíveis informações pessoais."
            )

            for alerta in alertas:
                st.write(f"⚠️ {alerta}")

        else:
            st.success(
                "Nenhum dado pessoal conhecido foi encontrado "
                "pelo detector."
            )

        # Texto protegido pelo sistema
        st.subheader("Texto protegido")

        st.code(
            texto_protegido,
            language="text"
        )

        # Análise contextual usando IA
        st.subheader("Análise contextual da IA")

        with st.spinner("Analisando o contexto..."):

            try:
                resultado = analisar_com_ia(texto_protegido)

                riscos = resultado.get("riscos", [])
                prompt_seguro = resultado.get("prompt_seguro", "")

                if riscos:

                    for risco in riscos:

                        nivel = risco.get("nivel", "medio")

                        if nivel == "alto":
                            icone = "🔴"
                        elif nivel == "medio":
                            icone = "🟠"
                        else:
                            icone = "🟡"

                        st.markdown(
                            f"**{icone} "
                            f"{risco.get('informacao', 'Informação')}**"
                        )

                        st.write(
                            risco.get(
                                "motivo",
                                "Possível informação desnecessária."
                            )
                        )

                else:
                    st.success(
                        "A IA não encontrou informações pessoais "
                        "desnecessárias."
                    )

                # Prompt final
                st.subheader("Prompt minimizado")

                st.code(
                    prompt_seguro,
                    language="text"
                )

            except Exception as erro:

                st.error(
                    "Não foi possível realizar a análise com a IA."
                )

                st.ccaptionf"Erro: {erro}")import