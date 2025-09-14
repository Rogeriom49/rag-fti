```markdown
# Venda com Entrega Futura: Guia Completo

**Metadados:**

*   **Título:** Venda com Entrega Futura: Guia Completo
*   **Seção:** Processos de Venda
*   **Tipo:** Tutorial, Passo a Passo
*   **Palavras-chave:** Venda com Entrega Futura, CFOP, Nota Fiscal, Pedido de Venda, Estoque, Financeiro

## 1. Introdução

Este guia detalha o processo de venda com entrega futura, abordando desde o conceito até a execução no sistema. O objetivo é fornecer um passo a passo claro e completo para realizar esse tipo de venda de forma eficiente, garantindo o controle fiscal e financeiro.

## 2. Conceito de Venda com Entrega Futura

A **venda com entrega futura** é um processo no qual a venda é realizada e a nota fiscal de cobrança é emitida em um primeiro momento, e a entrega dos produtos é efetuada posteriormente, através de uma ou mais notas fiscais de entrega.

## 3. Configuração Inicial: CFOPs

A correta configuração das **CFOPs (Códigos Fiscais de Operações e Prestações)** é crucial para o processo de venda com entrega futura. Serão utilizadas duas CFOPs principais:

*   **CFOP de Cobrança (Ex: 5922 ou 6922):** Utilizada na primeira nota fiscal, referente à cobrança.
*   **CFOP de Entrega (Ex: 5117 ou 6117):** Utilizada nas notas fiscais subsequentes, referentes à entrega dos produtos.

### 3.1. CFOP de Cobrança (5922/6922)

*   **Objetivo:** Emitir a nota fiscal de cobrança sem movimentar o estoque.
*   **Configuração:**
    *   **Movimentar Estoque:** Não (não há circulação de mercadoria no momento da cobrança).
    *   **Gerar Financeiro:** Sim (haverá a cobrança).
    *   **Tributação:** Isento (não há circulação de mercadoria, apenas cobrança).
*   **Observação:** A CFOP deve estar configurada para não movimentar o estoque, pois a mercadoria não está sendo entregue neste momento.

### 3.2. CFOP de Entrega (5117/6117)

*   **Objetivo:** Emitir as notas fiscais de entrega dos produtos, movimentando o estoque.
*   **Configuração:**
    *   **Movimentar Estoque:** Sim (agora há circulação de mercadoria).
    *   **Gerar Financeiro:** Não (a cobrança já foi realizada na nota anterior).
    *   **Tributação:** Nenhuma (a tributação será a do cadastro do produto).
*   **Observação:** A CFOP não deve ter tributação vinculada, pois a tributação utilizada será a do cadastro do produto, que será aplicada no momento da circulação da mercadoria.

## 4. Verificação das CFOPs no Sistema

Para verificar as configurações das CFOPs no sistema, siga os passos:

1.  Acesse: **Cadastros fiscais > CFOP**.
2.  Localize a CFOP desejada (ex: 5922).
3.  Verifique as configurações:
    *   **Gerar financeiro:** Sim/Não (conforme o tipo da CFOP).
    *   **Movimentar estoque:** Sim/Não (conforme o tipo da CFOP).
    *   **Tributação vinculada:** Verificar se está configurada corretamente (ex: simples remessa com impostos isentos para a CFOP de cobrança).

## 5. Configurações Adicionais no Sistema

Além das CFOPs, algumas configurações adicionais no sistema são importantes:

### 5.1. Parâmetros Fiscais NFE

Na aba **CFOP** (em **Administração > Parâmetros fiscais NFE**), é possível configurar as CFOPs de simples faturamento (estadual e interestadual) e as CFOPs de entrega (5117/6117), para que o sistema as traga automaticamente em cada situação.

### 5.2. Parâmetros do Sistema

Nos parâmetros do sistema, é importante configurar para que a **CFOP seja informada na venda**. Isso é necessário porque, no processo de venda com entrega futura, haverá momentos em que haverá financeiro e outros não, momentos em que movimentará estoque e outros não. O controle estará atrelado à CFOP utilizada na venda.

## 6. Processo de Venda com Entrega Futura: Passo a Passo

Todo o processo de venda com entrega futura deve ser iniciado pelo **pedido de venda**. O pedido de venda é crucial para o controle do que precisa ser entregue ou não.

### 6.1. Criação do Pedido de Venda

1.  **Abertura do Pedido:** Inicie um novo pedido de venda.
2.  **Seleção do Cliente:** Selecione o cliente.
3.  **Tipo de Pedido:** Defina o tipo do pedido como **entrega futura**.
4.  **Adição dos Produtos:** Adicione os produtos ao pedido (um ou mais).
5.  **Confirmação e Salvar:** Confirme e salve o pedido. Não é necessário gerar a reserva automaticamente.
6.  **Não gerar venda:** Não gere a venda neste momento.

### 6.2. Geração da Venda (Nota de Cobrança)

1.  **Pesquisar o Pedido:** Localize o pedido de venda criado.
2.  **Gerar Venda:** Clique na opção para gerar a venda a partir do pedido.
3.  **Verificação da CFOP:** O sistema deverá trazer automaticamente a CFOP correta (ex: 6922 para entrega futura, cobrança).
4.  **Salvar a Venda:** Salve a venda. Isso gerará a conta a receber do cliente e emitirá a nota fiscal de cobrança.
5.  **Confirmação da Nota:** É fundamental que a nota fiscal de cobrança esteja confirmada para que seja possível emitir as notas fiscais de entrega posteriormente.
6.  **Observação:** A nota fiscal de cobrança sairá como isenta de impostos, pois não há circulação de mercadoria.

### 6.3. Geração das Notas Fiscais de Entrega

O segredo do processo está no pedido de venda. É através dele que será feito o controle das entregas.

1.  **Acesso ao Pedido de Venda:** Acesse o pedido de venda original.
2.  **Verificação da Quantidade a Entregar:** No pedido, verifique a quantidade de produtos a serem entregues.
3.  **Geração da Nota Fiscal de Entrega:** No pedido, clique em **Mais opções > Gerar nota fiscal eletrônica de entrega**.
4.  **Edição da Quantidade (Opcional):** Se necessário, edite a quantidade a ser entregue nesta nota fiscal.
5.  **Informar transportadora (Opcional):**
6.  **Confirmação da CFOP:** O sistema deverá trazer a CFOP correta (ex: 5117).
7.  **Verificação da Tributação:** A tributação deverá ser a do cadastro do produto.
8.  **Confirmação e Salvar:** Confirme e salve a nota fiscal de entrega. Isso baixará o produto do estoque, mas não gerará financeiro.
9.  **Repetição do Processo:** Repita o processo para cada entrega parcial, até que a quantidade a entregar seja zero.

### 6.4. Acompanhamento do Saldo a Entregar

1.  **Acesso ao Pedido de Venda:** Acesse o pedido de venda original.
2.  **Verificação da Quantidade a Entregar:** No pedido, verifique a quantidade de produtos a serem entregues.
3.  **Relatório de Saldo a Entregar (Futuro):** Nas próximas versões do sistema, haverá um relatório específico para verificar o saldo a entregar de cada pedido de venda.

## 7. Resumo do Processo

1.  **Pedido de Venda:** Inicie o processo com o pedido de venda, definindo o tipo como "entrega futura".
2.  **Venda (Cobrança):** Gere a venda a partir do pedido, emitindo a nota fiscal de cobrança (CFOP 5922/6922).
3.  **Notas de Entrega:** Gere as notas fiscais de entrega (CFOP 5117/6117) a partir do pedido de venda, conforme a necessidade.
4.  **Controle:** Acompanhe o saldo a entregar através do pedido de venda.

## 8. Considerações Finais

O processo de venda com entrega futura exige atenção aos detalhes e uma correta configuração do sistema. Ao seguir este guia e manter o controle através do pedido de venda, é possível realizar esse tipo de venda de forma eficiente e segura.
```