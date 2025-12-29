# Integrador WooCommerce

Sistema de sincronização bidirecional entre WooCommerce e banco de dados.

## Funcionalidades

- 🔄 Sincronização de **Pedidos** do WooCommerce para o banco de dados
- 📦 Sincronização de **Produtos** do banco de dados para o WooCommerce
- 🏥 Endpoint de health check
- 📊 Logging estruturado em JSON
- 🛡️ Tratamento de erros robusto

## Requisitos

- Python 3.8+
- Banco de dados (SQLite, PostgreSQL ou MySQL)
- Credenciais da API WooCommerce

## Instalação

1. Clone o repositório ou navegue até a pasta do projeto

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas credenciais:
- `WC_BASE_URL`: URL base do seu site WooCommerce
- `WC_KEY`: Chave da API WooCommerce
- `WC_SECRET`: Secret da API WooCommerce
- `DB_URL`: URL de conexão do banco de dados

## Uso

### Iniciar o servidor

```bash
python main.py
```

O servidor estará disponível em `http://localhost:8001`

### Documentação da API

Acesse `http://localhost:8001/docs` para ver a documentação interativa da API (Swagger UI)

### Endpoints Disponíveis

- `GET /health` - Health check
- `POST /pedidos/sincronizar` - Sincroniza pedidos do WooCommerce para o banco
- `POST /produtos/sincronizar` - Sincroniza produtos do banco para o WooCommerce

### Exemplo de Uso

#### Sincronizar Pedidos
```bash
curl -X POST http://localhost:8001/pedidos/sincronizar
```

#### Sincronizar Produtos
```bash
curl -X POST http://localhost:8001/produtos/sincronizar
```

## Estrutura do Projeto

```
IntegradorV2/
├── app/
│   ├── adapters/          # Adaptadores (banco, API externa)
│   │   ├── database.py
│   │   └── woocommerce_client.py
│   ├── api/               # Camada de API (FastAPI)
│   │   ├── routers/       # Rotas da API
│   │   └── deps.py        # Dependências
│   ├── core/              # Configurações e utilitários
│   │   ├── config.py
│   │   └── logger.py
│   ├── domain/            # Modelos de domínio
│   │   ├── models.py      # Modelos SQLAlchemy
│   │   └── schemas.py     # Schemas Pydantic
│   ├── services/          # Lógica de negócio
│   │   ├── pedidos_service.py
│   │   └── produtos_service.py
│   └── main.py            # Aplicação FastAPI
├── main.py                # Script de execução
├── requirements.txt       # Dependências Python
└── README.md             # Este arquivo
```

## Desenvolvimento

O projeto segue uma arquitetura em camadas:

1. **Adapters**: Responsáveis pela comunicação com sistemas externos
2. **Domain**: Modelos e schemas do domínio
3. **Services**: Lógica de negócio
4. **API**: Camada de apresentação (endpoints REST)

## Licença

Este projeto é privado.

