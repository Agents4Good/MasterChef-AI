# WebDoctor 

---
## Contextualização

Hoje, vamos sair do terminal e criar nossa primeira aplicação web, usando **Streamlit**.

Essa aplicação será um **Chat Médico**, onde o usuário informa sintomas e recebe uma orientação inicial de um assistente médico simulado pelo modelo de linguagem.

---
## Objetivo

O objetivo é criar uma interface simples de chat, onde:
- O usuário escreve seus sintomas.
- O modelo de IA (executado via **LangChain e ChatOllama**) analisa os sintomas e dá um retorno.
- As mensagens são exibidas em formato de chat, com histórico, igual em aplicativos reais de conversa.

---
## Exemplo

![image](https://github.com/user-attachments/assets/7af20c68-8694-44a2-8e6d-01aa294b6e06)

---
## Instalando as Dependências

**Nota:** Lembre de usar o ambiente virtual ativo, .venv

Instale o Streamlit com:
```bash
pip install streamlit
```

Instale o LangChain Ollama:
```bash
pip install langchain-ollama
```

Para o Histórico de mensagens, instale o LangChain Core:
```bash
pip install langchain-core
```

---
## Passo a passo do código

### Configuração inicial da página Streamlit

```python
st.set_page_config(page_title="Chat WebDoctor")
st.header("Chat WebDoctor")
```

- Configura a página com título e cabeçalho personalizados.

---
### Configurando o histórico de chat

```python
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = [
        AIMessage("Bem-Vindo ao WebDoctor! Quais as suas queixas?")
    ]
```

- Armazena o histórico de mensagens no *session_state*, começando com uma mensagem inicial.

---
### Exibindo o histórico de mensagens

```python
chat_history = st.session_state["chat_history"]

for history in chat_history:
    if isinstance(history, AIMessage):
        st.chat_message("ai").write(history.content)
    if isinstance(history, HumanMessage):
        st.chat_message("human").write(history.content)
```

- Mostra as mensagens anteriores no formato de chat (IA e usuário).

---
### Capturando a mensagem do usuário

```python
sintomas = st.chat_input("Aguardando sua resposta...")
```

- Input para o usuário digitar seus sintomas.

---
### Adicionando a mensagem do usuário ao histórico

```python
if sintomas:
    st.chat_message("user").write(sintomas)
    st.session_state["chat_history"] += [HumanMessage(sintomas)]
```

- Adiciona a mensagem do usuário ao histórico e exibe no chat.

---
### Montando o prompt (PromptWebDoctor)

```python
prompt = PromptWebDoctor.prompt_inicial(sintomas)
```

- Usa uma função externa para montar o prompt personalizado para o modelo.

Exemplo do arquivo Prompt_Web_Doctor.py:

```python
class PromptWebDoctor:
    @staticmethod
    def prompt_inicial(sintomas):
        return f"""
        Você é um médico assistente virtual especializado em fornecer orientações iniciais.
        O paciente informou os seguintes sintomas:
        {sintomas}
        Com base nesses sintomas, forneça uma análise inicial, possíveis causas e oriente se é necessário buscar um médico presencialmente.
        """
```

---
### Inicializando o modelo ChatOllama

```python
llm = ChatOllama(model="llama3.2:1b", temperature=0.7)
```

- Configura o modelo a ser usado e sua temperatura.

---
### Gerando resposta com stream

```python
output = llm.stream(prompt)
```

- A resposta é gerada e transmitida em tempo real.

---
### Exibindo a resposta da IA

```python
with st.chat_message("ai"):
    ai_message = st.write_stream(output)
```

- Exibe a resposta do modelo como uma mensagem no chat.

---
### Salvando a resposta no histórico

```python
st.session_state["chat_history"] += [AIMessage(ai_message)]
```

- Adiciona a resposta da IA no histórico.

---
## Conclusão e Demonstração

Para rodar a aplicação:

```bash
streamlit run app.py
```

---
