# UFSCar - ML in Production - EML2 - Atividade 1

## Projeto de classificação de Iris com esteira de CI com Actions do GitHub

Este repositório contém o código e os artefatos para a atividade 1 do módulo 2 de Engenharia de Machine Learning, parte do curso de pós-graduação *ML in Production* da UFSCar. O projeto consiste em um modelo de Machine Learning para classificar flores Iris, uma API Flask para predição online, Docker para containerização da aplicação e esteira de CI com três jobs de build, validação e teste.

## Estrutura do repositório

```
/ufscar-mlp-eml2-ativ1
├── Dockerfile
├── README.md
├── iris_model.pkl
├── requirements.txt
└── src
    ├── __init__.py
    ├── app.py
    ├── model.py
    └── tests
        ├── test_app.py
        └── test_model.py
```

## Pré-requisitos

Antes de começar, você precisará ter o Docker instalado em sua máquina. Você pode instalar o Docker seguindo as instruções no [site oficial do Docker](https://www.docker.com/products/docker-desktop).

## Como Rodar o Projeto

### Passo 1: Clonar o repositório

Clone o repositório para sua máquina local usando:

```bash
git clone https://github.com/plbalmeida/ufscar-mlp-eml2-ativ1.git
```

### Passo 2: Treinar o modelo de ML

Executar o seguinte comando:

```
python src/model.py
```

É esperado que o arquivo `iris_model.pkl` seja gerado na raíz do diretório do repositório.

### Passo 3: Push para a branch principal para executar a esteira de CI

Faça o push utilizando o seguinte comando para a branch `main`:

```
git push
```

### Passo 4: Rodar o container

Inicie o container com o seguinte comando:

```
docker run -p 5000:5000 ufscar-mlp-eml2-ativ2
```

O comando acima irá rodar o container e mapear a porta 5000 do container para a porta 5000 do seu host local.

## Como fazer predições

Com o container rodando, você pode enviar uma requisição POST para a API para fazer previsões. Use o seguinte comando cURL substituindo [5.1, 3.5, 1.4, 0.2] pelas características da flor que você deseja classificar:

```
curl -X POST -H "Content-Type: application/json" \
    -d '{"features": [5.1, 3.5, 1.4, 0.2]}' \
    http://localhost:5000/predict
```

A resposta da API será um JSON contendo a classe prevista pelo modelo. Por exemplo:

```
{
    "prediction": 0
}
```

Aqui, o número retornado corresponde à classe da flor Iris prevista pelo modelo (por exemplo, 0 para Iris-setosa).

# Contribuições

Contribuições são bem-vindas. Para contribuir, por favor, crie um pull request para revisão.

