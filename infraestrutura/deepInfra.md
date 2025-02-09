# [DeepInfra](https://deepinfra.com/)

---
## Motivação

O avanço dos modelos de linguagem tem levado ao desenvolvimento de arquiteturas cada vez maiores e mais sofisticadas. No entanto, rodar esses modelos localmente exige hardware potente, como GPUs de última geração, tornando o acesso a esses modelos inviável para muitas empresas e desenvolvedores individuais. 

Plataformas como a **DeepInfra** surgem para solucionar esse problema, oferecendo infraestrutura escalável para rodar inferências de modelos de linguagem sem a necessidade de possuir hardware especializado. Dessa forma, usuários podem acessar modelos avançados sob demanda, pagando apenas pelo uso e sem necessidade de manutenção de servidores dedicados.

---
## Introdução ao DeepInfra

DeepInfra oferece preços variados dependendo do modelo. Alguns são cobrados por milhão de tokens, enquanto outros são tarifados pelo tempo de uso da inferência. Não há contratos de longo prazo nem custos antecipados, e a escalabilidade ocorre automaticamente conforme a demanda.

A plataforma fornece uma API compatível com a OpenAI, exemplos de código e a possibilidade de deploy de modelos em GPUs Nvidia (A100, H100, etc.), garantindo baixa latência e boa performance. No entanto, não há informações detalhadas sobre a velocidade de inferência dos modelos.

---
## Faturamento

O sistema de faturamento do DeepInfra é baseado no uso dos serviços. Para utilizar a plataforma, é necessário adicionar um cartão de crédito ou realizar um pré-pagamento. As cobranças ocorrem das seguintes formas:

- Uma fatura é gerada no início de cada mês ou ao atingir o limite do nível de uso.
- O sistema opera com **níveis de uso**, onde, conforme os gastos aumentam, o usuário é movido automaticamente para um nível superior.
- Cada nível possui um limite de faturamento, e uma nova fatura é gerada ao atingir esse limite.

---
## Modelos e Preços

A tabela a seguir apresenta alguns dos principais modelos disponíveis e seus custos por milhão de tokens:

| Modelo | Custo (Entrada) | Custo (Saída) |
|--------|----------------|---------------|
| **meta-llama/Llama-3.3-70B-Instruct** | $0.23 | $0.40 |
| **meta-llama/Llama-3.3-70B-Instruct-Turbo** | $0.12 | $0.30 |
| **deepseek-ai/DeepSeek-R1** | $0.75 | $2.40 |
| **deepseek-ai/DeepSeek-R1-Distill-Llama-70B** | $0.23 | $0.69 |
| **deepseek-ai/DeepSeek-V3** | $0.49 | $0.89 |

---
## Recursos Adicionais

- **Compatibilidade com API OpenAI**
- **Escalabilidade Automática** baseada na demanda
- **Suporte para GPUs Nvidia** (A100, H100, etc.)
- **Detalhes Técnicos** para modelos, incluindo benchmarks, papers e repositórios

---
Para mais detalhes, acesse [DeepInfra](https://deepinfra.com/).
