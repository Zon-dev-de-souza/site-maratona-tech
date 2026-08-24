import re

from system import (
    PADRAO_CPF,
    PADRAO_CEP,
    PADRAO_TELEFONE,
    PADRAO_EMAIL,
    PADRAO_DOCUMENTO,
    PADRAO_NOME,
    PADRAO_IDADE,
)


def proteger_prompt(texto: str) -> str:

    protegido = texto

    # Documentos
    protegido = PADRAO_CPF.sub(
        "[CPF REMOVIDO]",
        protegido
    )

    protegido = PADRAO_DOCUMENTO.sub(
        "[DOCUMENTO REMOVIDO]",
        protegido
    )

    # Contatos
    protegido = PADRAO_EMAIL.sub(
        "[EMAIL REMOVIDO]",
        protegido
    )

    protegido = PADRAO_TELEFONE.sub(
        "[TELEFONE REMOVIDO]",
        protegido
    )

    # CEP
    protegido = PADRAO_CEP.sub(
        "[CEP REMOVIDO]",
        protegido
    )

    # Nome
    protegido = PADRAO_NOME.sub(
        "[NOME REMOVIDO]",
        protegido
    )

    # Idade
    protegido = PADRAO_IDADE.sub(
        "[IDADE REMOVIDA]",
        protegido
    )

    return protegido


def gerar_prompt_minimizado(texto: str) -> str:

    protegido = proteger_prompt(texto)

    # Informações de endereço
    protegido = re.sub(
        r"\b(?:rua|avenida|av\.|alameda|travessa)"
        r"\s+[^,.!?]+(?:,\s*\d+)?",
        "[ENDEREÇO REMOVIDO]",
        protegido,
        flags=re.IGNORECASE
    )

    # Nome da escola
    protegido = re.sub(
        r"\b(?:escola|colégio|colegio)"
        r"\s+[A-Za-zÀ-ÿ0-9 .'-]+",
        "minha escola",
        protegido,
        flags=re.IGNORECASE
    )

    # Evita espaços duplicados
    protegido = re.sub(
        r"\s{2,}",
        " ",
        protegido
    )

    return protegido.strip()import