# Alucard: Aluguel de Carros
Este é um sistema web desenvolvido no curso Técnico em Informática para Web do Senac com o objetivo de ser uma sistema simple para aluguel de carros.

## Funcionalidades
1. Login/Logout (autenticação)
2. CRUD dos carros para utilizar no aluguel
3. Criar um tributo de ‘status’ para identificar se o carro está alugado ou não.
4. Implementar permissões nas páginas:
a. Páginas públicas (index, listagem de carros, ...)
b. Páginas restrição de acesso (Criar, atualizar, alugar um carro, ...)
5. Criar página para o aluguel de usuário logado.

## Requisitos
Eu quero que no sistema tenha um serviço de autenticação para clientes e funcionários da empresa.

Como um funcionário, eu quero poder adicionar, visualizar as informações, editar e deletar um carro.

Eu quero saber as seguintes características do carro: 

- **Modelo e Marca do Carro:** Identificação clara do modelo e marca do carro para os usuários escolherem de acordo com suas preferências.
- **Ano de Fabricação:** Informação sobre o ano de fabricação do carro, auxiliando os usuários a avaliarem a idade do veículo.
- **Capacidade de Passageiros e Bagagem:** Número de assentos no veículo e informações sobre a capacidade de bagagem, ajudando os clientes a selecionarem um carro que atenda às suas necessidades.
- **Transmissão:** Especificação se o carro possui transmissão automática ou manual, permitindo aos usuários escolherem conforme sua preferência.
- **Combustível:** Tipo de combustível utilizado pelo carro (gasolina, diesel, elétrico, etc.), considerando as preferências dos usuários e as restrições ambientais.
- **Disponibilidade e Reservas:** Informações sobre a eficiência do consumo de combustível, auxiliando os usuários a estimarem os custos de operação.
- **Preços e Taxas:** Detalhes sobre os preços de aluguel, taxas adicionais, depósito de segurança e outras despesas associadas.

Como um cliente eu quero poder vizualizar os carros disponíveis e fazer o aluguel de um carro.

O aluguel do carro deve ter as seguintes características:

- **Detalhes do Carro**
  - Modelo e Marca
  - Ano de Fabricação
- **Período de Aluguel**
  - Data e Hora de Início e Término
- **Quilometragem**
  - Quilometragem Inicial e Final
- **Custo e Taxas**
- **Informações do Locatário**
  - Nome do Locatário
  - Informações de Contato
- **Status do Aluguel**
- **Ações Disponíveis**
  - Opção de Devolução
  - Extensão do Aluguel
- **Método de Pagamento**

O sistema deve ter páginas públicas e privadas. As págs. públicas são:
- Home;
- Listagem de carros;
- Detalhes do carro;
- Login;

As págs. privadas são:
- Págs de CRUD;
- Admin;
- Aluguel;
- Info do cliente;

As págs. de aluguel e info. do cliente podem ser acessadas pelo cliente somente quando logado.