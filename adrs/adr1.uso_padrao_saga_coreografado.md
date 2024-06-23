## ADR 1. Uso do padrão SAGA Coreografado 

### Status
Aceito

### Contexto
Dado o cenário de microserviços e a necessidade de assegurar que todas as bases de dados distribuídas estarão integras ao final de uma transação de compra, é necessário o uso de alguma técnica para lidar com esse desafio.

### Decisão
Foi optado por utilizar o padrão SAGA Coreografado, tendo como ponto principal da escolha sua simplicidade e rapidez na implementação.

O padrão orquestrado não foi usado devido haver somente um fluxo transacional para ser tratado, o que torna na prática inviável o esforço necessário para implementação do mesmo.

### Consequências
Será necessário provisionar um recurso gerenciador de mensageria para lidar com as mensagens de processos assíncronos(Saga coreografada), optou-se por utilizar o rabbit-mq.

### Conformidade
Após a implementação será possível analisar os logs da aplicação Python Celery e de assegurar que as mensagens estão sendo criadas e processadas.
