# Tech Challenge Fiap - Entrega Final
## Instruções para execução da aplicação
Executar os procedimentos descritos no readme dos repositórios abaixo:
- Criação de banco de dados(RDS): https://github.com/rafaelbgil/fiap-autoatendimento-db .
- Criação do cluster EKS: https://github.com/rafaelbgil/fiap-autoatendimento-k8s/tree/main .

## Link com a justificativa da escolha do padrão saga
https://github.com/rafaelbgil/fiap-autoatendimento-app-pedido/blob/main/adrs/adr1.uso_padrao_saga_coreografado.md

[ADR1. Uso do Padrão Saga Coreografado](/adrs/adr1.uso_padrao_saga_coreografado.md)

## Link com os relatórios do OWASP 
Os arquivos de relatório em formato html se encontram nesse repositório no diretório: **relatorios_owasp**, para acessar basta fazer o clone do repositório e abrir os arquivos html em algum navegador.

```bash
$ git clone https://github.com/rafaelbgil/fiap-autoatendimento-app-pedido.git
$ cd fiap-autoatendimento-app-pedido
$ firefox relatorios_owasp/confirmar_pagamento/webhook-1.html   # exemplo utilizando o navegador firefox
```

## Link com o relatório RPID 
https://github.com/rafaelbgil/fiap-autoatendimento-app-pedido/blob/main/relatorio_RIPD/ripd.pdf

[Relatorio RIPD](/relatorio_RIPD/ripd.pdf)
(será necessário fazer o clone do repositório para acessar)
## Link para o desenho da arquitetura
-  Link do desenho da arquitetura em cloud https://github.com/rafaelbgil/fiap-autoatendimento-app-pedido/blob/main/arquitetura/arquitetura_cloud.png
-  Link do desenho do funcionamento orquestão SAGA coreografada para a transação de atualização de status do pedido https://github.com/rafaelbgil/fiap-autoatendimento-app-pedido/blob/main/arquitetura/saga_coreografada.png

