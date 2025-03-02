<h1 align="center">Guia de Instalação - Ollama</h1>

> Versão em Vídeo: https://youtu.be/hCAJJ071WFA

Este tutorial ensina como instalar e testar o **Ollama**, uma plataforma para execução de Modelos de Linguagem localmente.  

---
## 🖥️ **1. Acesse o Site Oficial**  

🔗 **Site Oficial:** [https://ollama.com/](https://ollama.com/)  

Visite o site para obter informações sobre o Ollama e acessar os links de instalação.  

![image](https://github.com/user-attachments/assets/62d03fd5-c687-48b4-ab6b-7069ee3951a4)

---
## ⚙️ **2. Instale o Ollama no Seu Sistema**  

Escolha o comando correspondente ao seu sistema operacional.  

### **Para Linux:**  
Execute o seguinte comando no terminal:  
```shell
curl -fsSL https://ollama.com/install.sh | sh
```  

![image](https://github.com/user-attachments/assets/86414212-13d9-47f8-9cdf-f7ee56b511e4)

### **Para Windows/MacOS:**  
Baixe o instalador diretamente do site oficial e siga as instruções.  

---
## ✅ **3. Verifique a Instalação**  

Após a instalação, confirme se o Ollama foi instalado corretamente executando:  
```shell
ollama
```  
Se tudo estiver certo, o terminal exibirá informações sobre o Ollama.  

![image](https://github.com/user-attachments/assets/5da117e5-6e5b-40ac-ba2a-96f51023254e)

---
## 🚀 **4. Executando um Modelo no Ollama**  

Agora, você pode escolher um modelo para rodar. O comando básico para rodar um modelo é:  
```shell
ollama run <modelo>
```  

Exemplo:  
```shell
ollama run deepseek-r1:1.5b
```  

![image](https://github.com/user-attachments/assets/6a29fa20-7024-47b4-8d28-d51d937c88b7)

**Observação:** Se o modelo ainda não estiver instalado, o Ollama o baixará automaticamente antes de executá-lo.  

---
## 🛠 **5. Comandos Essenciais do Ollama**  

Aqui estão alguns comandos úteis para gerenciar modelos no Ollama:  

**Listar Modelos Instalados**  
```shell
ollama list
```  

![image](https://github.com/user-attachments/assets/e181474e-5734-44ce-b976-e35832e5557e)

**Baixar um Modelo Específico**  
```shell
ollama pull <modelo>
```  
O comando `pull` faz o download manual de um modelo antes do uso. Exemplo:  
```shell
ollama pull deepseek-r1:1.5b
```  

![image](https://github.com/user-attachments/assets/e88fff31-5a8f-4d4c-aea2-7dd43d54a293)

---

## 🎯 **6. Próximos Passos - VSCode e Python**  

Nos próximos tutoriais, veremos como integrar o Ollama ao **VSCode** e usá-lo com **Python** para criar aplicações com IA.  
