# Aula 2 - Especificação Caso de Uso
 
**PCS 3643 – Laboratório de Engenharia de Software I**
 
**3º. Quadrimestre/2022**
 
**Prof. Kechi Hirama Data: Setembro/2022**
 
**Aula 02 – Especificação de Caso de Uso**
 
| --- | --- |
 
## Vocabulário:
 
Rota de Voo: informação estática sobre a rota do voo, inclui o código do voo, a companhia, o aeroporto de saída e o aeroporto de destino (ex: LATAM-GRU-CWB). Uma Rota de Voo tem múltiplos voos.
 
Voo: Execução de uma rota do voo, com horário de saída, horário de chegada e status.
 
## Cadastrar Rota (CRUD)
 
1. Nome: Cadastrar Rota (CRUD)
2. Descrição: Operações de Cadastro, Leitura, Update e Delete para rotas de determinada companhia aérea
3. Evento iniciador: Novo cadastro é solicitado ao operador de voo
4. Atores: Operador de voo
5. Pré-condições:
6. Sequência de eventos:
   1. Operador entra no menu do operador
   2. Operador clica em “Criar nova rota”
   3. Sistema solicita código, horário esperados e duração esperada
   4. Operador insere dados da rota
   5. Sistema verifica validade dos dados inseridos e se já existe tal rota
   6. Sistema insere nova rota e exibe confirmação da operação
   7. Fim do caso de uso
7. Pós-condição:
   1. Sucesso da operação
8. Fluxo alternativo:
   1. Fluxo alternativo 1:
       1. Operador recebe solicitação de alteração de rota
       2. Operador insere código da rota
       3. Sistema valida código e solicita dados novos
       4. Operador informa dados novos
       5. Sistema verifica validade dos dados inseridos
       6. Sistema atualiza rota e exibe confirmação da operação
       7. Fim do caso de uso
9. Exceções:
   1. Erro na validação dos campos (por exemplo: algum dos campos estava nulo)
   2. Código de rota já existente
 
## Alteração de status do voo
 
1. Nome: Alteração de status do voo
2. Descrição: Alteração entre os possíveis status (embarcando, cancelado, programado, taxiando, pronto, autorizado, em voo e aterrissado)
3. Evento iniciador: Mudança na situação do voo
4. Atores: Funcionário das companhias aéreas, piloto
5. Pré-condições: Status do voo é alterado
6. Sequência de eventos:
   1. Usuário seleciona alteração de status e insere código do voo
   2. Sistema valida código e exibe status do voo
   3. Usuário seleciona novo estado dentre os possíveis de acordo com sua permissão
   4. Usuário confirma a seleção para salvá-la
   5. Sistema atualiza voo e exibe confirmação da operação
   6. Fim do caso de uso
7. Pós-condição:
   1. Novo status do voo é visível aos usuários
8. Fluxo alternativo
   1. Fluxo alternativo 1:
       1. Usuário cancela alteração antes de salvá-la (6.4)
       2. Sistema exibe confirmação de cancelamento
       3. Fim do caso de uso
9. Exceções:
   1. Código de voo invalido
 
## Emitir relatório
 
1. Nome: Emitir relatório
2. Descrição: Processo de geração de relatórios de atrasos ou incidentes de companhia aérea ou destino, utilizando filtros para especificidade
3. Evento iniciador: Gerente solicita emissão de relatório
4. Atores: Gerente de operações
5. Pré-condições: Ter registros de voos
6. Sequência de eventos: 
   1 Gerente solicita geração de relatório ao sistema
   2 Sistema mostra os tipos de relatório
   3 Gerente seleciona “por companhia aérea”
   4 Sistema exibe opções de filtro: 	, período de partida/chegada, aeroporto de origem/destino, 
   5 Gerente escolhe filtros para o relatório
   6 Sistema exibe opções de filtro escolhidos e tipo de relatório
   7 Gerente solicita a emissão de relatório
   8 Sistema gera pdf com as informações solicitadas
   9 Fim do caso de uso
7. Pós-condição:
   1 Relatório em PDF gerado pelo sistema
8. Fluxo alternativo
   8.1 Fluxo Alternativo 1:
      8.1.1 Gerente seleciona “por destino”
      8.1.2 Volta para 6.3
9. Exceções:
   9.1 Nenhum voo encontrado
