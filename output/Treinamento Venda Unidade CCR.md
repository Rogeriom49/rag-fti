```markdown
# Controle de Vendas de Unidades em Construtoras

## Metadados
- **Título:** Controle de Vendas de Unidades em Construtoras
- **Seção:** Operacional
- **Tipo:** Tutorial/Demonstração

## Introdução
Este documento detalha o processo de controle de vendas de unidades (apartamentos) em uma construtora dentro do sistema, desde o cadastro da unidade até o ajuste das parcelas com base em indexadores como INCC e IGPM.

## 1. Cadastro de Centro de Custo e Unidades
### 1.1. Definição de Centro de Custo (CCR)
Anteriormente denominados "obra", os centros de custo (agora "Centro de Custo e Resultado - CCR") são essenciais para alocar custos e receitas a projetos específicos, como edifícios.

### 1.2. Cadastro do Edifício
1.  **Nome:** Cadastrar o nome do edifício (ex: Dourado do Mar) como um centro de custo.
2.  **Cliente:** Definir a própria construtora como cliente associado ao centro de custo.

### 1.3. Cadastro das Unidades
1.  **Unidades:** Cadastrar as unidades (ex: Apartamento 101, 202) atreladas ao centro de custo.
2.  **Valor:** Definir o valor de cada unidade.

## 2. Venda da Unidade
### 2.1. Acesso à Tela de Venda
Navegar até a tela de "Movimentações > Venda > Venda Unidade CCR".

### 2.2. Inclusão de Nova Venda
1.  **Incluir:** Clicar em "Incluir" para iniciar uma nova venda.
2.  **Data:** Preencher a data da venda.
3.  **Correção das Parcelas:** Escolher entre INCC e IGPM para correção das parcelas.

### 2.3. Informações da Venda
1.  **Cliente:** Selecionar o cliente que está comprando a unidade.
2.  **Unidade:** Escolher a unidade que está sendo vendida.
3.  **Funcionário/Corretor:** (Opcional) Atribuir o funcionário ou corretor responsável pela venda.
4.  **Plano de Contas:** Definir o plano de contas.
5.  **Valor da Venda:** Inserir o valor total da venda (ex: 450.000).
6.  **Valor para Imposto de Renda:** Informar o valor que deve aparecer no relatório de imposto de renda (ex: 280.000).

### 2.4. Salvando a Venda
Salvar as informações da venda. O sistema irá montar a negociação.

## 3. Parcelamento e Reforços
### 3.1. Definição do Parcelamento
1.  **Primeiro Vencimento:** Definir a data do primeiro vencimento da parcela (ex: 10/09).
2.  **Valor da Parcela:** Definir o valor de cada parcela (ex: 35.000).
3.  **Início da Correção:** Definir a data de início da correção (INCC/IGPM) para as parcelas (ex: 01/09).
4.  **Reforço:** Indicar se a parcela é um reforço ou não.
5.  **Contabilização:** Indicar se a parcela contabiliza com imposto de renda.
6.  **Cálculo de INCC/IGPM:** Escolher se haverá cálculo de INCC e/ou IGPM.

### 3.2. Lançamento de Reforços
1.  **Data do Reforço:** Definir a data do reforço (ex: 01/05/2026).
2.  **Valor do Reforço:** Definir o valor do reforço (ex: 50.000).
3.  **Parcelas:** Indicar o número de parcelas (ex: 1).
4.  **Correção:** Reforços geralmente não possuem correção de INCC/IGPM.

### 3.3. Finalização do Lançamento
Lançar todos os reforços para que o valor total da venda seja atingido.

## 4. Consulta e Histórico
### 4.1. Pesquisa do Contrato
Pesquisar o contrato de venda para visualizar o histórico financeiro.

### 4.2. Histórico Financeiro
Visualizar o histórico de parcelas, reforços e eventuais renegociações.

## 5. Ajuste de Parcelas com INCC/IGPM
### 5.1. Cadastro de Cotação do Indexador
1.  **Acesso:** Navegar até "Cadastro > Financeiro > Cotações > Indexador de INCC".
2.  **Inclusão:** Clicar em "Incluir" para adicionar uma nova cotação.
3.  **Percentual:** Definir o percentual de ajuste (ex: 2,63%).
4.  **Data de Validade:** Definir a data a partir da qual o ajuste será aplicado (ex: 01/09/2025).

### 5.2. Aplicação do Ajuste
O sistema revisitará as parcelas e ajustará os valores dos saldos com base na cotação do INCC/IGPM.

### 5.3. Visualização do Ajuste
Com o botão direito do mouse, é possível visualizar o detalhamento do INCC aplicado.

### 5.4. Histórico de Ajustes
O sistema armazena o histórico de todos os ajustes de INCC/IGPM, permitindo rastrear as mudanças nos valores das parcelas ao longo do tempo.

## 6. Rastreamento de Dados do INCC
### 6.1. Acesso aos Detalhes
Dando dois cliques na cota cadastrada, é possível ver os detalhes do INCC.

### 6.2. Informações Detalhadas
Visualizar o dia, a hora, o valor anterior, a correção aplicada e o novo valor da parcela após o ajuste.

## Considerações Finais
Este documento apresentou o processo de controle de vendas de unidades em construtoras, desde o cadastro inicial até o ajuste fino das parcelas com indexadores. A correta aplicação desses passos garante um controle financeiro eficiente e transparente.
```