import streamlit as st  # Biblioteca para criar a interface web interativa
from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage, HumanMessage
from Prompt_Web_Doctor import PromptWebDoctor  


# Configurando a página da aplicação Streamlit
st.set_page_config(page_title="Chat WebDoctor")  # Definindo o título da página
st.header("Chat WebDoctor")  # Definindo o cabeçalho da página


# Inicializando o histórico de mensagens
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = [
        AIMessage("Bem-Vindo ao WebDoctor! Quais as suas queixas?")] 


# Acessando o histórico de mensagens armazenado na sessão
chat_history = st.session_state["chat_history"]
# Iterando sobre o histórico de mensagens para exibir as mensagens passadas
for history in chat_history:
    if isinstance(history, AIMessage):
        st.chat_message("ai").write(history.content)
    if isinstance(history, HumanMessage):
        st.chat_message("human").write(history.content)


# Solicitando o input de sintomas do usuário
sintomas = st.chat_input("Aguardando sua resposta...")  # Aguardando a resposta do usuário


# Quando o usuário fornecer sintomas
if sintomas:
    
    # Exibindo a mensagem do usuário no chat
    st.chat_message("user").write(sintomas)

    # Adicionando os sintomas fornecidos ao histórico de chat
    st.session_state["chat_history"] += [HumanMessage(sintomas)]
    
    # Gerando o prompt para o modelo baseado nos sintomas fornecidos
    prompt = PromptWebDoctor.prompt_inicial(sintomas)

    # Inicializando o modelo ChatOllama com parâmetros especificados (como o modelo e a temperatura)
    llm = ChatOllama(model="llama3.2:1b", temperature=0.7)
    
    # Gerando a resposta do modelo
    output = llm.stream(prompt)  

    # Exibindo a resposta gerada pelo modelo no chat
    with st.chat_message("ai"):
        ai_message = st.write_stream(output)  # Escrevendo a resposta do modelo no chat

    # Adicionando a mensagem gerada pelo modelo ao histórico de chat
    st.session_state["chat_history"] += [AIMessage(ai_message)]
