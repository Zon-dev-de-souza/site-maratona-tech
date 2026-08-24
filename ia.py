import json
import requests
import streamlit as st


def analisar_com_ia(texto_protegido: str) -> dict:
    prompt = f"""
Você é um analisador de privacidade para estudantes.

Analise o texto abaixo e identifique informações pessoais ou
potencialmente sensíveis que não sejam necessárias para realizar
o objetivo principal do texto.

Regras:
- Não invente informações.
- Não considere toda informação pessoal automaticamente perigosa.
- Avalie se a informação é realmente necessária para o objetivo.
- Priorize a minimização de dados.
- O texto já passou por uma etapa de proteção usando Regex.
- Não remova informações necessárias para responder à pergunta.
- Retorne somente JSON válido.

Formato obrigatório:

{{
    "riscos": [
        {{
            "informacao": "nome da informação",
            "nivel": "baixo|medio|alto",
            "motivo": "explicação curta"
        }}
    ],
    "prompt_seguro": "versão do texto com informações desnecessárias removidas"
}}

Texto para analisar:

{texto_protegido}
"""

    api_key = st.secrets["OPENAI_API_KEY"]

    resposta = requests.post(
        "https://api.openai.com/v1/responses",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-5-mini",
            "input": prompt
        },
        timeout=60
    )

    resposta.raise_for_status()

    dados = resposta.json()

    texto_resposta = dados["output"][0]["content"][0]["text"]

    resultado = json.loads(texto_resposta)

    return resultado