# Agentes Racionais

> Este capítulo introduz o conceito de **agentes** como entidades que percebem o ambiente e agem sobre ele.
> O foco está na construção de **agentes racionais**, aqueles que tomam decisões buscando maximizar o desempenho.

---
## 2.1 Agentes e Ambientes

### 🤖 O que é um Agente?
Um **agente** é qualquer coisa que pode **perceber** seu ambiente por meio de sensores e **agir** sobre ele por meio de atuadores.

> “Um agente recebe percepções do ambiente por meio de sensores e atua no ambiente por meio de atuadores.”

Exemplos:
- Humano: olhos (sensores), mãos/boca/pés (atuadores)
- Robô: câmeras/sensores de temperatura (sensores), motores/braços (atuadores)
- Software: leitura de arquivos (sensor), alteração em banco de dados (atuador)

---
### 🔁 Interação com o Ambiente

O agente se comporta com base na **sequência de percepções** que recebe.

**Função do Agente**:
```text
agente: Perceptos* → Ações
```

Ou seja, uma função que mapeia o histórico de percepções para uma ação.

---
## 2.2 Racionalidade

### ✅ O que é um Agente Racional?

Um **agente racional** é aquele que faz a **melhor ação possível** com base no conhecimento disponível, percepções recebidas e os objetivos definidos.

> “Um agente racional é aquele que faz a coisa certa — ou seja, que realiza a ação que causará o melhor resultado esperado com base nas percepções e no conhecimento disponível.”

---
### ❌ Racionalidade ≠ Perfeição

- **Perfeição**: exige onisciência e infalibilidade (irrealista).
- **Racionalidade**: depende do que o agente **sabe**, **percebe**, e **pode fazer** no momento.

> “A racionalidade não é onisciência — não exige que o agente acerte sempre, apenas que faça o melhor dado o que sabe.”

---
### ⚠️ Fatores que afetam a racionalidade

1. **Medida de desempenho**
2. **Conhecimento prévio do ambiente**
3. **Ações possíveis**
4. **Sequência de percepções recebidas**

---
## 2.3 Medidas de Desempenho

- Avaliam o sucesso do agente.
- Devem ser definidas com cuidado.
- Devem refletir **o objetivo do sistema**, e não o **comportamento interno** do agente.

Exemplo ruim: avaliar um aspirador por quão sujo estava antes vs. depois (pode trapacear).

Exemplo ideal: avaliar o **nível de limpeza** médio ao longo do tempo.

---
## 2.4 Ambientes de Tarefa (PEAS)

### 🔹 PEAS = Performance, Environment, Actuators, Sensors

Modelo usado para especificar completamente o ambiente de tarefa.

| Elemento       | Descrição                                  |
|----------------|--------------------------------------------|
| **P**          | Performance measure – medida de sucesso     |
| **E**          | Environment – ambiente em que opera         |
| **A**          | Actuators – como age sobre o ambiente       |
| **S**          | Sensors – como percebe o ambiente           |

---
### Exemplo: Robô aspirador

| PEAS              | Exemplo                                   |
|-------------------|--------------------------------------------|
| Performance       | Quantidade de sujeira removida, ruído, tempo |
| Environment       | Piso, paredes, sujeira, obstáculos          |
| Actuators         | Motores, escovas, aspirador                 |
| Sensors           | Sensores de sujeira, visão, proximidade     |

---
## 2.5 Tipos de Ambientes

Ambientes podem ser classificados segundo várias dimensões:

| Característica           | Explicação |
|--------------------------|-----------|
| **Totalmente observável** vs. **Parcialmente observável** | Se os sensores captam o estado completo do ambiente. |
| **Determinístico** vs. **Estocástico** | Se a próxima situação é completamente determinada pela atual e pelas ações. |
| **Episódico** vs. **Sequencial** | Se a experiência do agente se divide em episódios independentes ou não. |
| **Estático** vs. **Dinâmico** | Se o ambiente muda enquanto o agente pensa. |
| **Discreto** vs. **Contínuo** | Quantidade de percepções e ações possíveis. |
| **Ambiente de um agente** vs. **Multiagente** | Se há mais de um agente operando no mesmo ambiente. |

---
### Exemplos:

- Jogo de xadrez: totalmente observável, determinístico, sequencial, estático, discreto, multiagente.
- Robô de entrega: parcialmente observável, estocástico, sequencial, dinâmico, contínuo, multiagente.

---
## 2.6 Estrutura dos Agentes

Agentes são compostos por dois elementos principais:

1. **Função do agente**: mapeamento de perceptos para ações.
2. **Programa do agente**: implementação dessa função.

> “O programa do agente executa no hardware do agente — sua arquitetura.”

---
### Tipos de Agentes

#### 1. Agentes baseados em regras simples

- Se uma percepção → então uma ação.
- Fácil de entender, mas limitado para ambientes complexos.

#### 2. Agentes com estado interno

- Mantêm um modelo interno do mundo com base no histórico.
- Útil em ambientes **parcialmente observáveis**.

#### 3. Agentes com metas

- Usam **objetivos** para decidir quais ações tomar.
- Raciocinam sobre consequências.

#### 4. Agentes baseados em utilidade

- Vão além das metas: avaliam a **utilidade de diferentes estados**.
- Permitem decisões melhores quando há múltiplas soluções.

---
### Aprendizado em Agentes

Agentes inteligentes podem **aprender com a experiência**:

- Otimizar decisões
- Corrigir erros
- Adaptar-se a novos ambientes

> “Agentes aprendizes podem melhorar sua performance ao longo do tempo.”

---
## ✅ Conclusão

- Um agente é qualquer sistema que percebe e age.
- A racionalidade é definida pelo melhor resultado esperado, e não por perfeição.
- A especificação PEAS ajuda a definir claramente o ambiente de tarefa.
- Ambientes variam em muitos aspectos que afetam o design do agente.
- Diferentes arquiteturas de agentes (regras, estado, metas, utilidade) se aplicam a diferentes cenários.
- Aprendizado é fundamental para agentes adaptativos e eficazes.

---
