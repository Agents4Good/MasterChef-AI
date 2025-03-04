<h1 align="center">DeepSeek-R1 1.5B</h1>

**Nota:** Antes de começar, certifique-se de que já instalou o Ollama seguindo este guia: [Ollama - Instalação](https://github.com/Agents4Good/CozinhaLLM/blob/main/ollama/install.md)

---
## 🚀 Executando o DeepSeek no Ollama

Teste o DeepSeek diretamente pelo terminal com o seguinte comando:
```shell
ollama run deepseek-r1:1.5b
```

![image](https://github.com/user-attachments/assets/52b0f43e-5b31-4ab2-bd29-6fe6cd7c24e7)

---
## 🔍 Informações do Modelo

Visualize informações detalhadas do modelo utilizando o comando:
```shell
/show info
```

![image](https://github.com/user-attachments/assets/cb76d0a8-d45b-4d2f-b7fc-8049900a9ef6)

---
## 💬 Interagindo pelo Terminal

![image](https://github.com/user-attachments/assets/6d6e97e1-be30-464d-843c-f5de91efb13c)

**Nota:** Por ser um modelo menor (1.5B parâmetros), ele pode cometer erros em tarefas complexas, como tradução de linguagens.

---
## 🛠 Configurando um Ambiente Virtual

Para utilizar o modelo localmente em um editor de código, como o VSCode, crie um ambiente virtual Python.

**1️⃣ Instale o Virtualenv**
```shell
pip install virtualenv
```

**2️⃣ Crie um diretório para o projeto e acesse-o**

> Suponha que eu criei o diretório: "my-project"

```shell
cd my-project
```

**3️⃣ Crie o ambiente virtual**
```shell
python -m venv venv
```

**Venv:** O comando acima irá criar um diretório venv, que contém tudo que o ambiente virtual precisa.

**4️⃣ Ative o ambiente virtual**

🔹 Windows:
```shell
venv\Scripts\activat
```

🔹 Linux/Mac:
```shell
source venv/bin/activate
```

**5️⃣ Desativando o ambiente virtual**
```shell
desactivate
```

Para reativar, basta executar novamente o comando de ativação.

Ficou com dúvidas sobre o ambiente virtual? Acesse os links a seguir.<br>
[Tutorial Completo Venv - Medium](https://dev.to/franciscojdsjr/guia-completo-para-usar-o-virtual-environment-venv-no-python-57bo)<br>
[Documentação](https://docs.python.org/pt-br/3.13/library/venv.html)

---
## 📦 Instalando a Biblioteca Ollama

Com o ambiente virtual ativado, instale a biblioteca Ollama:
```shell
pip install ollama
```

---
## 💻 Configuração no VSCode

Abra o diretório do seu projeto no **VSCode** e certifique-se de que está usando o ambiente virtual correto.

![Untitled design](https://github.com/user-attachments/assets/34483997-5cc7-4428-9967-2c648cef13f2)

---
## 📝 Exemplo de Código em Python e Ollama

```python
from ollama import chat
from ollama import ChatResponse

response: ChatResponse = chat(model='deepseek-r1:1.5b', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])

print(response['message']['content'])
# Ou acesse diretamente os campos da resposta
print(response.message.content)
```

**Nota:** Caso enfrente erros ao acessar a biblioteca `ollama`, verifique se o ambiente virtual está ativo.

---
## 🦜 LangChain

Para facilitar nossas vidas, existe um framework chamado LangChain, que potencializa nossas aplicações de IA.

Veja o mesmo código mostrado na seção anterior, mas dessa vez com o LangChain.

```python
from langchain_ollama import ChatOllama

chat = ChatOllama(model="deepseek-r1:1.5b")

response = chat.invoke("Why is the sky blue?")
print(response.content)
```

**Nota:** No tópico "Aplicações", há exemplos de uso do LangChain.
