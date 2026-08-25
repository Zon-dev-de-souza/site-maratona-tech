import streamlit as st

from recursos import RECURSOS
from system import analisar_privacidade
from protetor import proteger_prompt, gerar_prompt_minimizado


st.set_page_config(
    page_title="Projeto Maratona Tech",
    page_icon="📚",
    layout="wide"
)


# ============================================================
# MENU LATERAL
# ============================================================

st.sidebar.title("Projeto Maratona Tech")

st.sidebar.caption("Maratona Tech 2026")

st.sidebar.divider()

pagina = st.sidebar.radio(
    "Menu",
    [
        "🏠 Início",
        "📚 Recursos educacionais",
        "🛡️ Protetor de Prompt",
        "👥 Sobre o projeto"
    ]
)

# Espaçamento visual
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.divider()

st.sidebar.caption(
    "Projeto desenvolvido para a\n"
    "Maratona Tech 2026"
)


# ============================================================
# INÍCIO
# ============================================================

if pagina == "🏠 Início":

    st.title("Projeto Maratona Tech")

    st.subheader(
        "Recursos educacionais gratuitos para estudantes"
    )

    st.write(
        "Encontre materiais gratuitos para complementar seus estudos "
        "e aprenda a utilizar a tecnologia de forma mais consciente."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📚 Recursos educacionais")

        st.write(
            "Encontre cursos, vídeos, e-books e materiais gratuitos "
            "para diferentes áreas de estudo."
        )

        if st.button("Ver recursos", use_container_width=True):

            st.session_state["pagina"] = "📚 Recursos educacionais"
            st.rerun()

    with col2:

        st.subheader("🛡️ Protetor de Prompt")

        st.write(
            "Verifique informações pessoais antes de compartilhar "
            "um texto com uma inteligência artificial."
        )

        if st.button(
            "Proteger meu prompt",
            use_container_width=True
        ):

            st.session_state["pagina"] = "🛡️ Protetor de Prompt"
            st.rerun()

    st.divider()

    st.info(
        "🏆 Projeto desenvolvido por estudantes "
        "para a Maratona Tech 2026."
    )


# ============================================================
# RECURSOS EDUCACIONAIS
# ============================================================

elif pagina == "📚 Recursos educacionais":

    st.title("📚 Recursos educacionais")

    st.write(
        "Materiais gratuitos selecionados para ajudar "
        "nos seus estudos."
    )

    categoria = st.selectbox(
        "Escolha uma categoria:",
        list(RECURSOS.keys())
    )

    st.divider()

    recursos = RECURSOS[categoria]

    for recurso in recursos:

        st.subheader(recurso["titulo"])

        st.write(recurso["descricao"])

        st.link_button(
            "🔗 Acessar recurso",
            recurso["url"],
            use_container_width=False
        )

        st.divider()


# ============================================================
# PROTETOR DE PROMPT
# ============================================================

elif pagina == "Protetor de Prompt":

    st.title("Protetor de Prompt")

    st.write(
        "Antes de enviar um texto para uma IA, descubra se ele "
        "contém informações pessoais desnecessárias."
    )

    st.divider()

    texto = st.text_area(
        "Cole aqui o prompt:",
        height=220,
        placeholder=(
            "Exemplo: Tenho 16 anos, meu nome é João "
            "e preciso de ajuda com matemática."
        )
    )

    if st.button(
        "🔍 Analisar prompt",
        type="primary",
        use_container_width=True
    ):

        if not texto.strip():

            st.warning(
                "Digite ou cole algum texto primeiro."
            )

        else:

            resultado = analisar_privacidade(texto)

            alertas = resultado["alertas"]
            riscos = resultado["riscos"]

            # --------------------------------------------
            # VERIFICAÇÃO
            # --------------------------------------------

            st.subheader("🔎 Análise inicial")

            if alertas:

                st.warning(
                    f"Foram encontradas {len(alertas)} "
                    "possíveis informações pessoais."
                )

                for alerta in alertas:

                    st.write(
                        f"⚠️ {alerta}"
                    )

            else:

                st.success(
                    "Nenhuma informação pessoal conhecida "
                    "foi encontrada."
                )

            # --------------------------------------------
            # TEXTO PROTEGIDO
            # --------------------------------------------

            st.subheader("🛡️ Texto protegido")

            texto_protegido = proteger_prompt(texto)

            st.code(
                texto_protegido,
                language="text"
            )

            # --------------------------------------------
            # ANÁLISE DE RISCO
            # --------------------------------------------

            st.subheader("📊 Análise de risco")

            if riscos:

                for risco in riscos:

                    nivel = risco["nivel"]

                    if nivel == "alto":
                        icone = "🔴"

                    elif nivel == "medio":
                        icone = "🟠"

                    else:
                        icone = "🟡"

                    st.markdown(
                        f"### {icone} {risco['informacao']}"
                    )

                    st.write(
                        f"**Nível:** {nivel.upper()}"
                    )

                    st.write(
                        risco["motivo"]
                    )

            else:

                st.success(
                    "Nenhum risco relevante foi identificado."
                )

            # --------------------------------------------
            # PROMPT FINAL
            # --------------------------------------------

            st.subheader("✨ Prompt minimizado")

            prompt_seguro = gerar_prompt_minimizado(texto)

            st.code(
                prompt_seguro,
                language="text"
            )

            st.caption(
                "O objetivo é manter apenas as informações "
                "necessárias para realizar a tarefa."
            )


# ============================================================
# SOBRE O PROJETO
# ============================================================

elif pagina == "Sobre o projeto":

    st.title("Sobre o projeto")

    st.subheader("Projeto Maratona Tech")

    st.write(
        "Somos um projeto desenvolvido por estudantes "
        "para a Maratona Tech 2026."
    )

    st.write(
        "O projeto busca facilitar o acesso a recursos "
        "educacionais gratuitos e incentivar o uso consciente "
        "da tecnologia na educação."
    )

    st.divider()

    st.subheader("Nosso objetivo")

    st.write(
        "Reunir materiais educacionais gratuitos em um único "
        "lugar, facilitando o acesso dos estudantes a conteúdos "
        "que podem complementar seus estudos."
    )

    st.divider()

    st.subheader("🛡️ Por que o Protetor de Prompt?")

    st.write(
        "Estudantes utilizam cada vez mais ferramentas de "
        "inteligência artificial para estudar. Porém, podem "
        "acabar compartilhando informações pessoais "
        "desnecessárias."
    )

    st.write(
        "Por isso, criamos uma ferramenta que identifica "
        "possíveis dados pessoais e apresenta uma versão "
        "mais segura do prompt."
    )

    st.divider()

    st.subheader("👥 Equipe")

    st.write(
        "Projeto desenvolvido pelo grupo:"
    )

    st.write(
        "• Nome do integrante 1\n\n"
        "• Nome do integrante 2\n\n"
        "• Nome do integrante 3\n\n"
        "• Nome do integrante 4"
    )

    st.divider()

    st.subheader("💻 Tecnologias utilizadas")

    st.write(
        "• Python\n\n"
        "• Streamlit\n\n"
        "• Expressões Regulares (Regex)\n\n"
        "• GitHub"
    )

    st.divider()

    st.subheader("🏆 Maratona Tech 2026")

    st.write(
        "Este projeto foi desenvolvido como parte da "
        "participação do grupo na Maratona Tech 2026."
    )

    st.success(
        "Educação + Tecnologia + Uso consciente de IA"
    ) import streamlit as st

from recursos import RECURSOS
from system import analisar_privacidade
from protetor import proteger_prompt, gerar_prompt_minimizado


st.set_page_config(
    page_title="Projeto Maratona Tech",
    page_icon="📚",
    layout="wide"
)


# ============================================================
# MENU LATERAL
# ============================================================

st.sidebar.title("Projeto Maratona Tech")

st.sidebar.caption("Maratona Tech 2026")

st.sidebar.divider()

pagina = st.sidebar.radio(
    "Menu",
    [
        "🏠 Início",
        "📚 Recursos educacionais",
        "🛡️ Protetor de Prompt",
        "👥 Sobre o projeto"
    ]
)

# Espaçamento visual
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.divider()

st.sidebar.caption(
    "Projeto desenvolvido para a\n"
    "Maratona Tech 2026"
)


# ============================================================
# INÍCIO
# ============================================================

if pagina == "🏠 Início":

    st.title("Projeto Maratona Tech")

    st.subheader(
        "Recursos educacionais gratuitos para estudantes"
    )

    st.write(
        "Encontre materiais gratuitos para complementar seus estudos "
        "e aprenda a utilizar a tecnologia de forma mais consciente."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📚 Recursos educacionais")

        st.write(
            "Encontre cursos, vídeos, e-books e materiais gratuitos "
            "para diferentes áreas de estudo."
        )

        if st.button("Ver recursos", use_container_width=True):

            st.session_state["pagina"] = "📚 Recursos educacionais"
            st.rerun()

    with col2:

        st.subheader("🛡️ Protetor de Prompt")

        st.write(
            "Verifique informações pessoais antes de compartilhar "
            "um texto com uma inteligência artificial."
        )

        if st.button(
            "Proteger meu prompt",
            use_container_width=True
        ):

            st.session_state["pagina"] = "🛡️ Protetor de Prompt"
            st.rerun()

    st.divider()

    st.info(
        "🏆 Projeto desenvolvido por estudantes "
        "para a Maratona Tech 2026."
    )


# ============================================================
# RECURSOS EDUCACIONAIS
# ============================================================

elif pagina == "📚 Recursos educacionais":

    st.title("📚 Recursos educacionais")

    st.write(
        "Materiais gratuitos selecionados para ajudar "
        "nos seus estudos."
    )

    categoria = st.selectbox(
        "Escolha uma categoria:",
        list(RECURSOS.keys())
    )

    st.divider()

    recursos = RECURSOS[categoria]

    for recurso in recursos:

        st.subheader(recurso["titulo"])

        st.write(recurso["descricao"])

        st.link_button(
            "🔗 Acessar recurso",
            recurso["url"],
            use_container_width=False
        )

        st.divider()


# ============================================================
# PROTETOR DE PROMPT
# ============================================================

elif pagina == "🛡️ Protetor de Prompt":

    st.title("🛡️ Protetor de Prompt")

    st.write(
        "Antes de enviar um texto para uma IA, descubra se ele "
        "contém informações pessoais desnecessárias."
    )

    st.divider()

    texto = st.text_area(
        "Cole aqui o prompt:",
        height=220,
        placeholder=(
            "Exemplo: Tenho 16 anos, meu nome é João "
            "e preciso de ajuda com matemática."
        )
    )

    if st.button(
        "🔍 Analisar prompt",
        type="primary",
        use_container_width=True
    ):

        if not texto.strip():

            st.warning(
                "Digite ou cole algum texto primeiro."
            )

        else:

            resultado = analisar_privacidade(texto)

            alertas = resultado["alertas"]
            riscos = resultado["riscos"]

            # --------------------------------------------
            # VERIFICAÇÃO
            # --------------------------------------------

            st.subheader("🔎 Análise inicial")

            if alertas:

                st.warning(
                    f"Foram encontradas {len(alertas)} "
                    "possíveis informações pessoais."
                )

                for alerta in alertas:

                    st.write(
                        f"⚠️ {alerta}"
                    )

            else:

                st.success(
                    "Nenhuma informação pessoal conhecida "
                    "foi encontrada."
                )

            # --------------------------------------------
            # TEXTO PROTEGIDO
            # --------------------------------------------

            st.subheader("🛡️ Texto protegido")

            texto_protegido = proteger_prompt(texto)

            st.code(
                texto_protegido,
                language="text"
            )

            # --------------------------------------------
            # ANÁLISE DE RISCO
            # --------------------------------------------

            st.subheader("📊 Análise de risco")

            if riscos:

                for risco in riscos:

                    nivel = risco["nivel"]

                    if nivel == "alto":
                        icone = "🔴"

                    elif nivel == "medio":
                        icone = "🟠"

                    else:
                        icone = "🟡"

                    st.markdown(
                        f"### {icone} {risco['informacao']}"
                    )

                    st.write(
                        f"**Nível:** {nivel.upper()}"
                    )

                    st.write(
                        risco["motivo"]
                    )

            else:

                st.success(
                    "Nenhum risco relevante foi identificado."
                )

            # --------------------------------------------
            # PROMPT FINAL
            # --------------------------------------------

            st.subheader("✨ Prompt minimizado")

            prompt_seguro = gerar_prompt_minimizado(texto)

            st.code(
                prompt_seguro,
                language="text"
            )

            st.caption(
                "O objetivo é manter apenas as informações "
                "necessárias para realizar a tarefa."
            )


# ============================================================
# SOBRE O PROJETO
# ============================================================

elif pagina == "👥 Sobre o projeto":

    st.title("👥 Sobre o projeto")

    st.subheader("Educa+")

    st.write(
        "O Educa+ é um projeto desenvolvido por estudantes "
        "para a Maratona Tech 2026."
    )

    st.write(
        "O projeto busca facilitar o acesso a recursos "
        "educacionais gratuitos e incentivar o uso consciente "
        "da tecnologia na educação."
    )

    st.divider()

    st.subheader("🎯 Nosso objetivo")

    st.write(
        "Reunir materiais educacionais gratuitos em um único "
        "lugar, facilitando o acesso dos estudantes a conteúdos "
        "que podem complementar seus estudos."
    )

    st.divider()

    st.subheader("Por que o Protetor de Prompt?")

    st.write(
        "Estudantes utilizam cada vez mais ferramentas de "
        "inteligência artificial para estudar. Porém, podem "
        "acabar compartilhando informações pessoais "
        "desnecessárias."
    )

    st.write(
        "Por isso, criamos uma ferramenta que identifica "
        "possíveis dados pessoais e apresenta uma versão "
        "mais segura do prompt."
    )

    st.divider()

    st.subheader("👥 Equipe")

    st.write(
        "Projeto desenvolvido pelo grupo:"
    )

    st.write(
        "• Nome do integrante 1\n\n"
        "• Nome do integrante 2\n\n"
        "• Nome do integrante 3\n\n"
        "• Nome do integrante 4"
    )

    st.divider()

    st.subheader("💻 Tecnologias utilizadas")

    st.write(
        "• Python\n\n"
        "• Streamlit\n\n"
        "• Expressões Regulares (Regex)\n\n"
        "• GitHub"
    )

    st.divider()

    st.subheader("🏆 Maratona Tech 2026")

    st.write(
        "Este projeto foi desenvolvido como parte da "
        "participação do grupo na Maratona Tech 2026."
    )

    st.success(
        "Educação + Tecnologia + Uso consciente de IA"
    )
