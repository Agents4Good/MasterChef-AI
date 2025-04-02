# Guia de Uso da API do DeepInfra

---

## Habemus acesso aos modelos do DeepInfra!! 🎊

É necessário seguir algumas regras:

1. **Cada grupo (frente) tem sua própria chave de API**, então cada grupo só deve usar sua chave.

2. **Bom senso**: os créditos não são infinitos, são para todo o projeto. Use-os com responsabilidade.

3. **Simule o custo do experimento** antes de rodá-lo. Assim, você terá uma ideia do valor a ser gasto. O script abaixo pode ajudar.

4. **As chaves devem ser compartilhadas com segurança**. Envie apenas em grupos privados ou mensagens diretas. Peça acesso ao pós-graduando que trabalha com você. 😉

---

# Instalando Bibliotecas

```python
!pip install openai pandas tiktoken
```

---

# Primeira Inferência

## Criando um Cliente OpenAI

```python
from openai import OpenAI

API_KEY = "SUA CHAVE PRIVADA AQUI"
BASE_URL = "https://api.deepinfra.com/v1/openai"

openai = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL,
)

def get_completion(prompt, model):
    chat_completion = openai.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return chat_completion.choices[0].message.content
```

## Escolhendo o Modelo e o Prompt

> Escolha entre os modelos disponíveis: [Lista de Modelos](https://deepinfra.com/models/text-generation)

```python
get_completion("What is the capital of France?", "deepseek-ai/DeepSeek-R1-Turbo")
```

```json
{"type": "string"}
```

---

# Estimando o Custo do Experimento

1. Carregue um arquivo CSV chamado **data.csv** contendo colunas de entrada e saída.
2. Defina o preço por token do modelo escolhido ([Tabela de Preços](https://deepinfra.com/pricing)).
3. Execute o código abaixo para obter uma estimativa do custo.

---

## Definindo o Custo por Token

```python
# Custo por token
INPUT_COST = 0.23 / 1_000_000  # 0.23 = Custo por 1M de tokens
OUTPUT_COST = 0.40 / 1_000_000
```

## Carregando os Dados

```python
import pandas as pd

df = pd.read_csv("data.csv")
df
```

## Contando Tokens e Calculando Custo

```python
import tiktoken

MODEL = 'gpt-3.5-turbo'  # Model tokenizer

def count_tokens(text):
    """Conta o número de tokens em um texto usando o tokenizador do OpenAI."""
    encoding = tiktoken.encoding_for_model(MODEL)
    return len(encoding.encode(text)) if pd.notna(text) else 0

# Contagem de tokens

df["input_tokens"] = df["input"].apply(lambda x: count_tokens(str(x)))
df["output_tokens"] = df["output"].apply(lambda x: count_tokens(str(x)))

# Cálculo de custos

df["input_cost"] = df["input_tokens"] * INPUT_COST
df["output_cost"] = df["output_tokens"] * OUTPUT_COST
df["total_cost"] = df["input_cost"] + df["output_cost"]

# Resumo

total_input_tokens = df["input_tokens"].sum()
total_output_tokens = df["output_tokens"].sum()
total_cost = df["total_cost"].sum()

print(f"Total Input Tokens: {total_input_tokens}")
print(f"Total Output Tokens: {total_output_tokens}")
print(f"Estimated Total Cost: {total_cost:.5f} $")
```

```python
Total Input Tokens: 137
Total Output Tokens: 348
Estimated Total Cost: 0.00017 $
```

