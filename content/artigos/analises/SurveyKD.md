# A Survey on Knowledge Distillation of Large Language Models

> *Referência:* [A Survey on Knowledge Distillation of Large Language Models](https://arxiv.org/abs/2402.13116)

---
## 1. Resumo

Na era dos Large Language Models (LLMs), a **Destilação de Conhecimento (Knowledge Distillation)** surge como uma metodologia essencial para transferir conhecimento entre LLMs robustas e suas contrapartes mais leves.

Além disso, à medida que os LLMs de código aberto florescem, o KD desempenha um papel crucial tanto na compressão desses modelos quanto na facilitação de sua auto-melhoria, empregando-se como professores.

Crucialmente, esta pesquisa explora a interação entre **Aumento de Dados (Data Augmentation)** e a Destilação. 

---
## 2. Data Augmentation (DA)

O **Data Augmentation** é uma técnica usada para ampliar a quantidade e diversidade dos dados de treinamento de um modelo, criando variações artificiais a partir dos dados existentes.

Durante o processo de destilação, o modelo professor (um LLM maior e mais capacitado) pode ser usado para criar novos exemplos de dados, que são então utilizados para treinar o modelo aluno (menor e menos potente). O DA pode gerar exemplos focados em habilidades específicas que o aluno precisa adquirir.

Por exemplo, se o modelo professor é especialista em responder questões complexas em português, o DA pode ser usado para criar mais exemplos desse tipo, permitindo que o modelo aluno aprenda melhor essas habilidades.

---
## 3. Vantagens dos Modelos de Código Aberto

Em contraste aos modelos proprietários, modelos de código aberto como trazem vantagens notáveis:

- **Acessibilidade**: Sem taxas de licenciamento, esses modelos estão disponíveis para uma gama mais ampla de usuários.
- **Colaboração**: Incentivam um ambiente de pesquisa mais colaborativo e inclusivo.
- **Personalização**: Permitem soluções customizadas para necessidades específicas.

No entanto, eles também possuem desvantagens:

- **Escala reduzida**: O desempenho pode ser inferior em tarefas complexas ([Zheng et al., 2023a](https://arxiv.org/abs/2402.13116)).
- **Menor investimento em pré-treinamento**.
- **Menos etapas de ajuste fino** devido a restrições de recursos.

---
## 4. Introdução à Destilação

Este processo é semelhante à transferência do "conhecimento" de um professor para um aluno, onde o aluno (LLM menor) aprende a imitar as características de desempenho do professor (LLM maior).

Comparado aos algoritmos tradicionais de KD ([Gou et al., 2021](https://arxiv.org/abs/2402.13116)), o **aumento de dados (DA)** ([Feng et al., 2021](https://arxiv.org/abs/2402.13116)) emergiu como um paradigma predominante para a destilação de LLMs, utilizando pequenas sementes de conhecimento para gerar dados mais especializados ([Taori et al., 2023](https://arxiv.org/abs/2402.13116)).

Além disso, o KD continua sendo essencial para a **compressão de LLMs**, tornando-os mais eficientes sem perda significativa de desempenho. Mais recentemente, o uso de **LLMs de código aberto como professores** para seu próprio autoaperfeiçoamento mostrou-se promissor ([Yuan et al., 2024a](https://arxiv.org/abs/2402.13116); [Chen et al., 2024a](https://arxiv.org/abs/2402.13116)).

![img01](https://github.com/user-attachments/assets/2aa29c11-9d59-4df4-8259-74af05fa7bf0)

---
## 5. Conceito Antigo

A ideia de transferir conhecimento entre um modelo mais robusto e um modelo mais leve é antiga.

Historicamente, as técnicas de destilação de conhecimento, antes da era dos LLMs, concentravam-se principalmente na transferência de conhecimento de redes neurais complexas, muitas vezes incômodas, para arquiteturas mais compactas e eficientes [Kim, Rush](https://arxiv.org/abs/1606.07947).

Esse processo foi amplamente impulsionado pela necessidade de implantar modelos de aprendizado de máquina em ambientes com recursos limitados, como dispositivos móveis ou plataformas de computação de ponta, onde o poder computacional e a memória são limitados.

Esses métodos anteriores envolviam o treinamento de uma rede menor de alunos para imitar a saída de uma rede maior de professores.

Consulte a pesquisa [Gou et al. 2021](https://arxiv.org/abs/2006.05525) para obter mais detalhes sobre técnicas de destilação de conhecimento geral em IA e DL.

---
## 6. As coisas mudaram...

Em contraste, o advento dos LLMs revolucionou o cenário de destilação de conhecimento.

A era atual de destilação de conhecimento em LLMs muda o foco da mera compressão de arquitetura para a elicitação e transferência de conhecimento [Tunstall et al. (2023)](https://arxiv.org/abs/2310.16944). 

Essa mudança de paradigma se deve em grande parte ao conhecimento expansivo e profundo que LLMs possuem. E os parâmetros inacessíveis de LLMs dificultam compactá-los usando técnicas de poda ou quantização [Liu et al. (2023a)](https://arxiv.org/abs/2305.17888).

Ao contrário da era anterior, onde o objetivo era replicar o comportamento de saída do modelo do professor ou reduzir o tamanho do modelo, o foco atual na destilação de conhecimento baseada em LLM é elicitar o conhecimento específico que esses modelos têm.

A chave para essa abordagem moderna está em prompts heurísticos e cuidadosamente projetados, que são usados ​​para extrair conhecimento específico. O uso de prompts como meio de elicitação de conhecimento oferece uma abordagem mais flexível e dinâmica para a destilação. Ele permite uma extração mais direcionada de conhecimento, com foco em habilidades específicas ou domínios de interesse.

Além disso, esta era de destilação de conhecimento também enfatiza a transferência de qualidades mais abstratas, como padrões de raciocínio.
Isso contrasta fortemente com o foco anterior na replicação de saída. Indicando uma mudança em direção a uma transferência mais holística e abrangente de capacidades cognitivas.

As técnicas atuais envolvem não apenas a replicação de saídas, mas também a emulação dos processos de pensamento.

Isso envolve estratégias complexas como o prompt de cadeia de pensamento, onde o modelo do aluno é treinado para aprender o processo de raciocínio do professor, aprimorando assim suas capacidades de resolução de problemas e tomada de decisão.

> Ideia: atenção com a palavra *emular*. Lembre da emulação de consoles, jogos...

---
## 7. Relação com o Aumento de Dados Artificiais

Na era dos LLMs, o Aumento de Dados (DA) Wang et al. (2022a); Ye et al. (2022) surge como um paradigma crítico integral ao processo de destilação do conhecimento.

Ao contrário das técnicas tradicionais de DA, como a paráfrase de Gangal et al. (2022) ou a retrotradução de Longpre et al. (2019), que visam principalmente expandir o conjunto de dados de treinamento de uma maneira um tanto mecânica, o DA dentro do contexto dos LLMs se concentra na geração de dados de treinamento novos e ricos em contexto, adaptados a domínios e habilidades específicos.

Ao alavancar um conjunto de conhecimento semente, KD emprega DA para incitar LLMs a produzir dados explícitos que encapsulam habilidades específicas. 
Por meio de DA, LLMs são incitados a criar conjuntos de dados direcionados e de alta qualidade que não são apenas maiores em volume, mas também ricos em diversidade e especificidade.

---
## 8. Pipeline da Destilação de Conhecimento

![image](https://github.com/user-attachments/assets/fae44ad3-1de6-4440-ba15-ed0852368103)

O esboço deste pipeline pode ser amplamente categorizado em quatro estágios distintos.

**1. Habilidade Alvo:** O primeiro estágio envolve direcionar o professor LLM para uma habilidade alvo ou domínio específico. Isso é alcançado por meio de instruções ou modelos cuidadosamente elaborados que orientam o foco do LLM. Essas instruções são projetadas para obter respostas que demonstrem a proficiência do LLM em uma área específica, seja um domínio especializado como saúde ou direito, ou uma habilidade como raciocínio ou compreensão de linguagem.

**2. Conhecimento Semente:** Uma vez que a área-alvo é definida, o próximo passo é alimentar o professor LLM com conhecimento semente. Esse conhecimento semente normalmente compreende um pequeno conjunto de dados ou pistas de dados específicos relevantes para a habilidade de elicitação ou conhecimento de domínio do professor LLM. Ele atua como um catalisador, levando o professor LLM a gerar saídas mais elaboradas e detalhadas com base nessas informações iniciais. O conhecimento semente é crucial, pois fornece uma base sobre a qual o modelo do professor pode construir e expandir, criando, assim, exemplos de conhecimento mais abrangentes e aprofundados.

**3. Geração de Conhecimento:** Em resposta ao conhecimento semente e instruções de direção, o professor LLM gera exemplos de conhecimento. Esses exemplos são predominantemente na forma de diálogos de perguntas e respostas (QA) ou explicações narrativas, alinhando-se com as capacidades de processamento/compreensão de linguagem natural do LLM. Em certos casos especializados, as saídas também podem incluir logits ou recursos ocultos, embora isso seja menos comum devido à complexidade e aos requisitos específicos de tais formulários de dados. Os exemplos de conhecimento gerados constituem o núcleo do conhecimento de destilação, encapsulando a compreensão e as habilidades avançadas do professor LLM.

**4. Treinamento do Modelo do Aluno com um Objetivo de Aprendizagem Específico:** O estágio final envolve a utilização dos exemplos de conhecimento gerados para treinar o modelo do aluno. Este treinamento é guiado por uma função de perda que se alinha com os objetivos de aprendizagem. A função de perda quantifica o desempenho do modelo do aluno na replicação ou adaptação do conhecimento do modelo do professor. Ao minimizar essa perda, o modelo do aluno aprende a emular as habilidades-alvo ou o conhecimento de domínio do professor, adquirindo assim capacidades semelhantes. O processo envolve o ajuste iterativo dos parâmetros do modelo do aluno para reduzir a discrepância entre suas saídas e as do modelo do professor, garantindo a transferência efetiva do conhecimento.

---
## 9. Algoritmos de Destilação de Conhecimento

Esta seção navega pelo processo de destilação do conhecimento. Ela é categorizadz em duas etapas principais: ‘Conhecimento’, com foco em extrair conhecimento de LLMs de professores (Eq.1), e ‘Destilação’, centrada em injetar esse conhecimento em modelos de alunos (Eq.2). Elaboraremos esses dois processos nas seções subsequentes.

Na figura abaixo, veja um pequeno resumo dos diferentes algoritmos que iremos estudar.

![image](https://github.com/user-attachments/assets/46e1071a-fd97-47b0-a232-bb613b25d521)

---
## 9.1 Conhecimento 

### 9.1.1 Labeling

### 9.1.2 Expansion

### 9.1.3 Data Curation

### 9.1.4 Feature

### 9.1.5 FeedBack

### 9.1.6 Self-Knowledge

---
## 9.2 Destilação

### 9.2.1 Supervised Fine-Tuning

### 9.2.2 Divergence and Similarity

### 9.2.3 Reinforcement Learning

### 9.2.4 Ranking Optimization

---
