import streamlit as st

from recursos import RECURSOS
from system import analisar_privacidade
from protetor import proteger_prompt, gerar_prompt_minimizado


# ============================================================
# CONFIGURAÇÃO
# ============================================================

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
        "👥 Sobre o projeto",
        "📩 Suporte"
    ]
)

st.sidebar.divider()

st.sidebar.caption(
    "Projeto desenvolvido por estudantes "
    "para a Maratona Tech 2026."
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
        "Um projeto desenvolvido para facilitar o acesso a "
        "materiais gratuitos de estudo e incentivar o uso "
        "consciente da tecnologia na educação."
    )

    st.divider()

    st.subheader("Comece por aqui")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### Recursos educacionais")

        st.write(
            "Encontre cursos, vídeos, e-books, documentações "
            "e outros materiais gratuitos para complementar "
            "seus estudos."
        )

        st.info(
            "Use o menu lateral e selecione "
            "\"📚 Recursos educacionais\"."
        )

    with col2:

        st.markdown("### Protetor de Prompt")

        st.write(
            "Verifique se seu texto possui informações pessoais "
            "antes de compartilhá-lo com uma inteligência artificial."
        )

        st.info(
            "Use o menu lateral e selecione "
            "\"🛡️ Protetor de Prompt\"."
        )

    st.divider()

    st.subheader("O que você encontra no projeto?")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("### Programação")

        st.write(
            "Materiais para Python, lógica de programação, "
            "HTML, CSS, JavaScript e desenvolvimento web."
        )

    with col2:

        st.markdown("### Estudos")

        st.write(
            "Conteúdos gratuitos para Português, Inglês "
            "e Matemática."
        )

    with col3:

        st.markdown("### Privacidade")

        st.write(
            "Uma ferramenta para identificar informações "
            "pessoais desnecessárias em prompts."
        )

    st.divider()

    st.subheader("Navegue pelo projeto")

    st.write(
        "Todas as funcionalidades estão disponíveis no "
        "menu lateral. Escolha uma opção para começar."
    )

    st.success(
        "Projeto desenvolvido por estudantes para a "
        "Maratona Tech 2026."
    )


# ============================================================
# RECURSOS EDUCACIONAIS
# ============================================================

elif pagina == "📚 Recursos educacionais":

    st.title("Recursos educacionais")

    st.write(
        "Materiais gratuitos selecionados para ajudar "
        "nos seus estudos."
    )

    st.divider()

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
            "Acessar recurso",
            recurso["url"]
        )

        st.divider()


# ============================================================
# PROTETOR DE PROMPT
# ============================================================

elif pagina == "🛡️ Protetor de Prompt":

    st.title("Protetor de Prompt")

    st.write(
        "Analise um texto antes de enviá-lo para uma "
        "inteligência artificial."
    )

    st.write(
        "O sistema identifica possíveis informações pessoais "
        "e cria uma versão minimizada do texto."
    )

    st.divider()

    texto = st.text_area(
        "Cole aqui o texto que pretende enviar para uma IA:",
        height=220,
        placeholder=(
            "Exemplo: Tenho 16 anos, meu nome é João "
            "e preciso de ajuda com matemática."
        )
    )

    if st.button(
        "Analisar prompt",
        type="primary",
        use_container_width=True
    ):

        if not texto.strip():

            st.warning(
                "Digite ou cole algum texto antes de analisar."
            )

        else:

            # =================================================
            # ANÁLISE
            # =================================================

            resultado = analisar_privacidade(texto)

            alertas = resultado.get("alertas", [])
            riscos = resultado.get("riscos", [])

            st.subheader("Análise inicial")

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

            # =================================================
            # TEXTO PROTEGIDO
            # =================================================

            st.subheader("Texto protegido")

            texto_protegido = proteger_prompt(texto)

            st.code(
                texto_protegido,
                language="text"
            )

            # =================================================
            # ANÁLISE DE RISCO
            # =================================================

            st.subheader("Análise de risco")

            if riscos:

                for risco in riscos:

                    nivel = risco.get(
                        "nivel",
                        "medio"
                    )

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
                        f"Nível: {nivel.upper()}"
                    )

                    st.write(
                        risco.get(
                            "motivo",
                            "Possível informação "
                            "desnecessária."
                        )
                    )

            else:

                st.success(
                    "Nenhum risco relevante foi identificado."
                )

            # =================================================
            # PROMPT MINIMIZADO
            # =================================================

            st.subheader("Prompt minimizado")

            prompt_seguro = gerar_prompt_minimizado(
                texto
            )

            st.code(
                prompt_seguro,
                language="text"
            )

            st.caption(
                "O objetivo é manter as informações necessárias "
                "para realizar a tarefa e reduzir a exposição "
                "de dados pessoais."
            )


# ============================================================
# SOBRE O PROJETO
# ============================================================

elif pagina == "👥 Sobre o projeto":

    st.title("Sobre o projeto")

    st.subheader("Projeto Maratona Tech")

    st.write(
        "O Projeto Maratona Tech é uma iniciativa desenvolvida "
        "por estudantes para a Maratona Tech 2026."
    )

    st.write(
        "A proposta é facilitar o acesso a recursos educacionais "
        "gratuitos e incentivar o uso consciente da tecnologia "
        "no ambiente escolar."
    )

    st.divider()

    st.subheader("Objetivo")

    st.write(
        "Reunir materiais educacionais gratuitos em um único "
        "lugar, permitindo que estudantes encontrem conteúdos "
        "para complementar seus estudos."
    )

    st.divider()

    st.subheader("Protetor de Prompt")

    st.write(
        "O projeto também apresenta uma ferramenta que identifica "
        "possíveis informações pessoais em textos destinados a "
        "inteligências artificiais."
    )

    st.write(
        "A ferramenta utiliza verificações automáticas para "
        "identificar dados como nomes, telefones, endereços "
        "e outras informações que podem ser desnecessárias."
    )

    st.divider()

    st.subheader("Tecnologias utilizadas")

    st.write(
        "Python, Streamlit e Expressões Regulares (Regex)."
    )

    st.divider()

    st.subheader("Equipe")

    st.write(
        "Projeto desenvolvido pelo nosso grupo para a "
        "Maratona Tech 2026."
    )

    st.write(
        "Integrantes:"
    )

    st.write(
        "- Integrante 1\n"
        "- Integrante 2\n"
        "- Integrante 3\n"
        "- Integrante 4"
    )

    st.divider()

    st.info(
        "Projeto desenvolvido para a Maratona Tech 2026."
    )


# ============================================================
# SUPORTE
# ============================================================

elif pagina == "📩 Suporte":

    st.title("Suporte")

    st.write(
        "Encontrou algum problema no site, encontrou um "
        "link quebrado ou tem alguma sugestão?"
    )

    st.write(
        "Entre em contato com a equipe do projeto."
    )

    st.divider()

    st.subheader("Contato")

    st.write(
        "E-mail para suporte:"
    )

    st.code(
        "SEU_EMAIL_AQUI"
    )

    st.write(
        "Substitua o endereço acima pelo e-mail oficial "
        "utilizado pelo grupo."
    )

    st.divider()

    st.subheader("Sugestões")

    st.write(
        "Também estamos abertos a sugestões de novos "
        "materiais educacionais e melhorias para o projeto."
        )
