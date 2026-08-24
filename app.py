import streamlit as st

from recursos import RECURSOS
from system import analisar_privacidade
from protetor import (proteger_prompt, gerar_prompt_minimizado)


st.set_page_config(
    page_title="Projeto maratona tec",
    page_icon="📚",
    layout="wide"
)


# ---------- CABEÇALHO ----------

st.title("Projeto maratona tec")

st.write(
    "Recursos educacionais gratuitos e ferramentas para ajudar "
    "estudantes a estudar e usar a tecnologia com mais segurança."
)


# ---------- MENU ----------

pagina = st.sidebar.radio(
    "Navegação",
    [
        "🏠 Início",
        "📚 Recursos educacionais",
        "🛡️ Protetor de Prompt",
        "👥 Sobre o projeto"
    ]
)


# ---------- INÍCIO ----------

if pagina == "Início":

    st.header("Aprenda mais. Encontre recursos. Use tecnologia com segurança.")

    st.write(
        "O Educa+ reúne materiais educacionais gratuitos em um único lugar "
        "e oferece uma ferramenta para ajudar estudantes a identificar "
        "informações pessoais antes de compartilhá-las com uma IA."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📚 Recursos gratuitos")

        st.write(
            "Encontre cursos, vídeos, e-books e outros materiais "
            "para complementar seus estudos."
        )

    with col2:
        st.subheader("🛡️ Proteção de prompts")

        st.write(
            "Verifique se seu prompt contém informações pessoais "
            "desnecessárias antes de enviá-lo para uma inteligência artificial."
        )

    st.divider()

    st.info(
        "Projeto desenvolvido por estudantes para a Maratona Tech 2026."
    )


# ---------- RECURSOS ----------

elif pagina == "📚 Recursos educacionais":

    st.header("📚 Recursos educacionais gratuitos")

    st.write(
        "Selecione uma área para encontrar materiais gratuitos "
        "que podem ajudar nos seus estudos."
    )

    categoria = st.selectbox(
        "Escolha uma categoria:",
        list(RECURSOS.keys())
    )

    st.divider()

    for recurso in RECURSOS[categoria]:

        st.subheader(recurso["titulo"])

        st.write(recurso["descricao"])

        st.link_button(
            "🔗 Acessar recurso",
            recurso["url"]
        )

        st.divider()


# ---------- PROTETOR DE PROMPT ----------

elif pagina == "Protetor de Prompt":

    st.header("Protetor de Prompt")

    st.write(
        "Antes de enviar um texto para uma IA, verifique se ele "
        "contém informações pessoais desnecessárias."
    )

    texto = st.text_area(
        "Cole aqui o prompt que você pretende enviar:",
        height=220,
        placeholder=(
            "Exemplo: Tenho 16 anos, estudo na escola X "
            "e preciso de ajuda com matemática."
        )
    )

    if st.button("🔍 Analisar prompt", type="primary"):

        if not texto.strip():

            st.warning(
                "Digite ou cole algum texto antes de analisar."
            )

        else:

            resultado = analisar_privacidade(texto)

            alertas = resultado["alertas"]
            riscos = resultado["riscos"]

            st.subheader("🔎 Verificação")

            if alertas:

                st.warning(
                    f"Foram encontradas {len(alertas)} "
                    "possíveis informações pessoais."
                )

                for alerta in alertas:
                    st.write(f"⚠️ {alerta}")

            else:

                st.success(
                    "Nenhuma informação pessoal conhecida foi encontrada."
                )

            st.subheader("🛡️ Texto protegido")

            texto_protegido = proteger_prompt(texto)

            st.code(
                texto_protegido,
                language="text"
            )

            st.subheader("Análise do prompt")

            if riscos:

                for risco in riscos:

                    if risco["nivel"] == "alto":
                        icone = "🔴"

                    elif risco["nivel"] == "medio":
                        icone = "🟠"

                    else:
                        icone = "🟡"

                    st.markdown(
                        f"**{icone} {risco['informacao']} — "
                        f"{risco['nivel'].upper()}**"
                    )

                    st.write(risco["motivo"])

            else:

                st.success(
                    "O prompt não apresenta riscos relevantes "
                    "identificados pelas regras do sistema."
                )

            st.subheader("✨ Prompt minimizado")

            prompt_seguro = gerar_prompt_minimizado(texto)

            st.code(
                prompt_seguro,
                language="text"
            )

            st.info(
                "O sistema prioriza a minimização de dados: "
                "informações que não ajudam a responder ao objetivo "
                "do prompt podem ser removidas."
            )


# ---------- SOBRE ----------

elif pagina == "Sobre o projeto":

    st.header("Sobre o projeto")

    st.subheader("Educa+")

    st.write(
        "O Educa+ é um projeto desenvolvido por estudantes "
        "para a Maratona Tech 2026."
    )

    st.write(
        "O objetivo é facilitar o acesso a recursos educacionais "
        "gratuitos e incentivar o uso consciente da tecnologia "
        "no ambiente educacional."
    )

    st.divider()

    st.subheader("Objetivo")

    st.write(
        "Reunir materiais gratuitos para diferentes áreas de estudo "
        "em um único lugar, facilitando a busca por conteúdos "
        "complementares."
    )

    st.subheader("Uso consciente de IA")

    st.write(
        "O projeto também possui uma ferramenta de proteção de prompts. "
        "Ela utiliza regras e expressões regulares para identificar "
        "informações pessoais que podem ser desnecessárias em um prompt."
    )

    st.divider()

    st.subheader("Equipe")

    st.write(
        "Projeto desenvolvido pelo grupo:"
    )

    st.write(
        "- Nome do integrante 1\n"
        "- Nome do integrante 2\n"
        "- Nome do integrante 3\n"
        "- Nome do integrante 4"
    )

    st.divider()

    st.subheader("💻 Tecnologias")

    st.write(
        "- Python\n"
        "- Streamlit\n"
        "- Expressões regulares (Regex)\n"
        "- GitHub"
    )

    st.divider()

    st.caption(
        "Maratona Tech 2026"
    )
