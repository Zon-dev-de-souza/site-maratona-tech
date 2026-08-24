import re


# ============================================================
# PADRÕES
# ============================================================

PADRAO_CPF = re.compile(
    r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b"
)

PADRAO_CEP = re.compile(
    r"\b\d{5}-\d{3}\b|\b\d{8}\b"
)

PADRAO_TELEFONE = re.compile(
    r"""
    (?:
        (?:\+?55\s?)?
        (?:\(?\d{2}\)?\s?)?
        (?:9\d{4}|\d{4})
        [-\s]?
        \d{4}
    )
    """,
    re.VERBOSE
)

PADRAO_EMAIL = re.compile(
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
)

PADRAO_NOME = re.compile(
    r"\b(?:meu nome é|meu nome e|me chamo|sou o|sou a)"
    r"\s+([A-ZÁÀÃÂÉÊÍÓÔÕÚÇ][a-záàãâéêíóôõúç]+"
    r"(?:\s+[A-ZÁÀÃÂÉÊÍÓÔÕÚÇ][a-záàãâéêíóôõúç]+)?)",
    re.IGNORECASE
)

PADRAO_IDADE = re.compile(
    r"\b(?:tenho\s+)?(\d{1,2})\s*(?:anos|anos de idade)\b",
    re.IGNORECASE
)

PADRAO_DOCUMENTO = re.compile(
    r"\b(?:RG|rg|identidade)\s*(?:n[ºo.]?\s*)?"
    r"\d{7,9}\b"
)


# ============================================================
# TERMOS
# ============================================================

TERMOS_ENDERECO = [
    "rua",
    "avenida",
    "av.",
    "alameda",
    "travessa",
    "bairro",
    "cep",
    "moro na",
    "moro no",
    "moro em",
    "meu endereço",
    "meu endereco",
]

TERMOS_ESCOLA = [
    "minha escola",
    "meu colégio",
    "meu colegio",
    "estudo na",
    "estudo no",
    "minha turma",
    "minha sala",
    "professor",
    "professora",
    "escola",
    "colégio",
    "colegio",
]

TERMOS_FINANCEIROS = [
    "meu salário",
    "meu salario",
    "minha renda",
    "renda familiar",
    "mesada",
    "sem dinheiro",
    "sou pobre",
    "sou rico",
    "bolsa família",
    "bolsa familia",
    "ganho r$",
]

TERMOS_POLITICOS = [
    "voto no",
    "voto na",
    "meu partido",
    "partido político",
    "partido politico",
    "eleição",
    "eleicao",
    "esquerda",
    "direita",
]


# ============================================================
# ANÁLISE
# ============================================================

def analisar_privacidade(texto: str) -> dict:

    alertas = []
    riscos = []

    texto_lower = texto.lower()

    # ---------- CPF ----------

    if PADRAO_CPF.search(texto):

        alertas.append(
            "CPF identificado no texto."
        )

        riscos.append({
            "informacao": "CPF",
            "nivel": "alto",
            "motivo": (
                "O CPF é um identificador pessoal e normalmente "
                "não é necessário para perguntas educacionais."
            )
        })


    # ---------- TELEFONE ----------

    if PADRAO_TELEFONE.search(texto):

        alertas.append(
            "Número de telefone identificado no texto."
        )

        riscos.append({
            "informacao": "Telefone",
            "nivel": "alto",
            "motivo": (
                "Um número de telefone permite contato direto "
                "e geralmente não é necessário para estudar."
            )
        })


    # ---------- EMAIL ----------

    if PADRAO_EMAIL.search(texto):

        alertas.append(
            "Endereço de e-mail identificado no texto."
        )

        riscos.append({
            "informacao": "E-mail",
            "nivel": "alto",
            "motivo": (
                "O e-mail é um dado de contato que normalmente "
                "não é necessário para uma pergunta educacional."
            )
        })


    # ---------- CEP ----------

    if PADRAO_CEP.search(texto):

        alertas.append(
            "CEP identificado no texto."
        )

        riscos.append({
            "informacao": "CEP",
            "nivel": "medio",
            "motivo": (
                "O CEP pode ajudar a indicar uma localização "
                "e normalmente não é necessário para estudar."
            )
        })


    # ---------- RG ----------

    if PADRAO_DOCUMENTO.search(texto):

        alertas.append(
            "Documento de identificação identificado no texto."
        )

        riscos.append({
            "informacao": "RG",
            "nivel": "alto",
            "motivo": (
                "Documentos de identificação são dados pessoais "
                "que não são necessários para perguntas educacionais."
            )
        })


    # ---------- NOME ----------

    if PADRAO_NOME.search(texto):

        alertas.append(
            "Nome próprio identificado no texto."
        )

        riscos.append({
            "informacao": "Nome",
            "nivel": "baixo",
            "motivo": (
                "O nome pode identificar o estudante, mas nem sempre "
                "é necessário para responder à pergunta."
            )
        })


    # ---------- IDADE ----------

    match_idade = PADRAO_IDADE.search(texto)

    if match_idade:

        idade = int(match_idade.group(1))

        if idade < 18:

            alertas.append(
                f"Informação de menor de idade ({idade} anos) identificada."
            )

            riscos.append({
                "informacao": "Idade",
                "nivel": "medio",
                "motivo": (
                    "A idade pode revelar que o usuário é menor de idade. "
                    "Ela só deve ser compartilhada quando for relevante "
                    "para responder ao pedido."
                )
            })

        else:

            alertas.append(
                "Informação de idade identificada."
            )

            riscos.append({
                "informacao": "Idade",
                "nivel": "baixo",
                "motivo": (
                    "A idade pode ser relevante dependendo do objetivo "
                    "do prompt, mas nem sempre é necessária."
                )
            })


    # ---------- ENDEREÇO ----------

    if any(termo in texto_lower for termo in TERMOS_ENDERECO):

        alertas.append(
            "Informações de endereço identificadas."
        )

        riscos.append({
            "informacao": "Endereço",
            "nivel": "alto",
            "motivo": (
                "Um endereço pode revelar a localização do estudante "
                "e normalmente não é necessário para estudar."
            )
        })


    # ---------- ESCOLA ----------

    if any(termo in texto_lower for termo in TERMOS_ESCOLA):

        alertas.append(
            "Informações sobre escola/instituição identificadas."
        )

        riscos.append({
            "informacao": "Escola",
            "nivel": "medio",
            "motivo": (
                "O nome da escola pode identificar o estudante "
                "e normalmente pode ser substituído por uma descrição "
                "genérica, como 'minha escola'."
            )
        })


    # ---------- FINANCEIRO ----------

    if any(termo in texto_lower for termo in TERMOS_FINANCEIROS):

        alertas.append(
            "Informações de situação financeira identificadas."
        )

        riscos.append({
            "informacao": "Situação financeira",
            "nivel": "medio",
            "motivo": (
                "Informações financeiras podem ser pessoais e devem "
                "ser compartilhadas somente quando forem relevantes."
            )
        })


    # ---------- POLÍTICA ----------

    if any(termo in texto_lower for termo in TERMOS_POLITICOS):

        alertas.append(
            "Informações de opinião política identificadas."
        )

        riscos.append({
            "informacao": "Opinião política",
            "nivel": "medio",
            "motivo": (
                "Opiniões políticas podem revelar informações pessoais "
                "e não são necessárias para a maioria dos pedidos educacionais."
            )
        })


    return {
        "alertas": alertas,
        "riscos": riscos
    }