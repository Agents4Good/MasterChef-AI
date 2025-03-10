# A Survey on Knowledge Distillation of Large Language Models

> *Referência:* [A Survey on Knowledge Distillation of Large Language Models](https://arxiv.org/abs/2402.13116)

---
## Resumo

Na era dos Large Language Models (LLMs), a **Knowledge Distillation (KD)** surge como uma metodologia essencial para transferir capacidades avançadas dos principais LLMs proprietários, como o GPT-4, para suas contrapartes de código aberto, como **LLaMA** e **Mistral**.

Além disso, à medida que os LLMs de código aberto florescem, o KD desempenha um papel crucial tanto na compressão desses modelos quanto na facilitação de sua auto-melhoria, empregando-se como professores. Essa função é crítica na transmissão de conhecimento avançado para modelos menores e na sua utilidade para compressão e autoaperfeiçoamento. Os três pilares fundamentais são: **algoritmo, habilidade e verticalização**.

Crucialmente, a pesquisa explora a interação entre **Data Augmentation (DA)** e KD, ilustrando como DA surge como um paradigma poderoso dentro da estrutura KD para reforçar o desempenho dos LLMs. O DA é usado para gerar dados de treinamento específicos de habilidades e ricos em contexto. Este trabalho tem como objetivo fornecer um guia perspicaz para pesquisadores e profissionais, oferecendo uma visão geral detalhada das metodologias atuais na destilação de conhecimento e propondo futuras direções de pesquisa.

---
## Data Augmentation (DA)

O **Data Augmentation** é uma técnica usada para ampliar a quantidade e diversidade dos dados de treinamento de um modelo, criando variações artificiais a partir dos dados existentes.

Durante o processo de destilação, o modelo professor (um LLM maior e mais capacitado) pode ser usado para criar novos exemplos de dados, que são então utilizados para treinar o modelo aluno (menor e menos potente). O DA pode gerar exemplos focados em habilidades específicas que o aluno precisa adquirir.

Por exemplo, se o modelo professor é especialista em responder questões complexas em português, o DA pode ser usado para criar mais exemplos desse tipo, permitindo que o modelo aluno aprenda melhor essas habilidades.

---
## Problematização dos Modelos Proprietários

Uma desvantagem significativa dos modelos proprietários é sua **acessibilidade limitada e custo elevado** ([OpenAI et al., 2023](https://arxiv.org/abs/2402.13116)). Esses modelos geralmente vêm com taxas de uso substanciais e acesso restrito, tornando-os menos acessíveis para indivíduos e organizações menores.

Em termos de **privacidade e segurança de dados** ([Wu et al., 2023a](https://arxiv.org/abs/2402.13116)), o uso desses LLMs frequentemente envolve o envio de dados confidenciais para servidores externos, o que levanta preocupações sobre privacidade e segurança.

---
## Vantagens dos Modelos de Código Aberto

Em contraste, modelos de código aberto como **[LLaMA](https://arxiv.org/abs/2402.13116)** ([Touvron et al., 2023]) e **[Mistral](https://arxiv.org/abs/2402.13116)** ([Jiang et al., 2023a]) trazem vantagens notáveis:

- **Acessibilidade e adaptabilidade**: Sem taxas de licenciamento ou políticas restritivas, esses modelos estão disponíveis para uma gama mais ampla de usuários.
- **Colaboração e inovação**: Incentivam um ambiente de pesquisa mais colaborativo e inclusivo.
- **Personalização**: Permitem soluções mais customizadas para necessidades específicas.

No entanto, eles também possuem desvantagens:

- **Escala reduzida**: O desempenho pode ser inferior em tarefas complexas ([Zheng et al., 2023a](https://arxiv.org/abs/2402.13116)).
- **Menor investimento em pré-treinamento**.
- **Menos etapas de ajuste fino** devido a restrições de recursos.

---
## Introdução à Destilação

A **destilação de conhecimento** envolve alavancar as capacidades mais avançadas dos principais modelos proprietários, como **GPT-4** ou **Gemini**, como estrutura de orientação para aprimorar as competências de LLMs de código aberto.

Este processo é semelhante à transferência do "conhecimento" de um professor para um aluno, onde o aluno (LLM de código aberto) aprende a imitar as características de desempenho do professor (LLM proprietário).

Comparado aos algoritmos tradicionais de KD ([Gou et al., 2021](https://arxiv.org/abs/2402.13116)), o **aumento de dados (DA)** ([Feng et al., 2021](https://arxiv.org/abs/2402.13116)) emergiu como um paradigma predominante para a destilação de LLMs, utilizando pequenas sementes de conhecimento para gerar dados mais especializados ([Taori et al., 2023](https://arxiv.org/abs/2402.13116)).

Além disso, o KD continua sendo essencial para a **compressão de LLMs**, tornando-os mais eficientes sem perda significativa de desempenho. Mais recentemente, o uso de **LLMs de código aberto como professores** para seu próprio autoaperfeiçoamento mostrou-se promissor ([Yuan et al., 2024a](https://arxiv.org/abs/2402.13116); [Chen et al., 2024a](https://arxiv.org/abs/2402.13116)).

![img01](https://github.com/user-attachments/assets/2aa29c11-9d59-4df4-8259-74af05fa7bf0)

---
## Benefícios da Destilação de Conhecimento

Os benefícios do KD na era dos LLMs são amplos: ([Gu et al., 2024](https://arxiv.org/abs/2402.13116)):

- **Redução da lacuna** entre modelos proprietários e de código aberto ([Chiang et al., 2023](https://arxiv.org/abs/2402.13116); [Xu et al., 2023a](https://arxiv.org/abs/2402.13116)).
- **Simplificação dos requisitos computacionais**, promovendo a sustentabilidade ambiental.
- **Acesso democratizado** às capacidades de última geração, promovendo maior participação e diversidade na pesquisa de IA.
- **Catalisação da inovação**, permitindo soluções mais robustas, versáteis e acessíveis em vários setores.

---
## Em construção
