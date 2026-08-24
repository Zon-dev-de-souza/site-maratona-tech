import re


PADRAO_CPF: str = r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b|\b\d{11}\b"

PADRAO_CEP: str = r"\b\d{5}-?\d{3}\b"

PADRAO_TELEFONE: str = (
    r"\b(?:\+?55\s?)?(?:\(?\d{2}\)?\s?)?\d{4,5}[-\s]?\d{4}\b"
)

PADRAO_RG: str = r"\b\d{2}\.?\d{3}\.?\d{3}-?[0-9Xx]\b"

PADRAO_NOME: str = (
    r"\b(meu nome é|sou o|sou a|me chamo)\s+([A-ZÀ-Ú][a-zà-ú]+)"
)


TERMOS_ENDERECO: list[str] = [
    "rua",
    "avenida",
    "alameda",
    "bairro",
    "moro na",
    "moro no",
]

TERMOS_FINANCEIROS: list[str] = [
    "salário",
    "renda",
    "mesada",
    "sem dinheiro",
    "pobre",
    "rico",
    "bolsa família",
    "ganho r$",
]

TERMOS_ESCOLA: list[str] = [
    "estudo na",
    "estudo no",
    "minha escola",
    "meu colégio",
    "minha turma",
]


def analisar_privacidade(texto: str) -> list[str]:
    if not texto.strip():
        return []

    alertas: list[str] = []
    texto_lower: str = texto.lower()

    # CPF
    if re.search(PADRAO_CPF, texto):
        alertas.append("CPF identificado no texto.")

    # CEP
    if re.search(PADRAO_CEP, texto):
        alertas.append("CEP identificado no texto.")

    # Telefone
    if re.search(PADRAO_TELEFONE, texto):
        alertas.append("Número de telefone identificado no texto.")

    # RG
    if re.search(PADRAO_RG, texto):
        alertas.append("RG identificado no texto.")

    # Endereço
    if any(termo in texto_lower for termo in TERMOS_ENDERECO):
        alertas.append("Informações de endereço identificadas.")

    # Idade
    match_idade = re.search(
        r"\b(\d{1,2})\s*(?:anos|anos de idade)\b|tenho\s*(\d{1,2})",
        texto_lower
    )

    if match_idade:
        idade_str = match_idade.group(1) or match_idade.group(2)

        if idade_str:
            idade = int(idade_str)

            if idade < 18:
                alertas.append(
                    f"Informação de menor de idade ({idade} anos) identificada."
                )
            else:
                alertas.append("Informação de idade identificada.")

    # Situação financeira
    if any(termo in texto_lower for termo in TERMOS_FINANCEIROS):
        alertas.append(
            "Informações de situação financeira identificadas."
        )

    # Escola
    if any(termo in texto_lower for termo in TERMOS_ESCOLA):
        alertas.append(
            "Informações sobre escola identificadas."
        )

    # Nome
    if re.search(PADRAO_NOME, texto):
        alertas.append("Nome próprio identificado.")

    return alertas


def proteger_texto(texto: str) -> str:
    texto_protegido = texto

    # CPF
    texto_protegido = re.sub(
        PADRAO_CPF,
        "[CPF REMOVIDO]",
        texto_protegido
    )

    # CEP
    texto_protegido = re.sub(
        PADRAO_CEP,
        "[CEP REMOVIDO]",
        texto_protegido
    )

    # Telefone
    texto_protegido = re.sub(
        PADRAO_TELEFONE,
        "[TELEFONE REMOVIDO]",
        texto_protegido
    )

    # RG
    texto_protegido = re.sub(
        PADRAO_RG,
        "[RG REMOVIDO]",
        texto_protegido
    )

    # Nome informado explicitamente
    texto_protegido = re.sub(
        PADRAO_NOME,
        r"\1 [NOME REMOVIDO]",
        texto_protegido
    )

    return texto_protegido