# Gerenciador de Configuração

Este projeto é um **Gerenciador de Configuração** simples feito em Python. Ele permite que os usuários leiam e escrevam configurações em um arquivo `config.json`, contendo informações sobre o servidor, como nome, IP e senha. O programa utiliza a biblioteca `colorama` para adicionar cores ao terminal, tornando a experiência mais interativa e visualmente amigável.

## Funcionalidades

- **Verificar ou criar arquivo de configuração**: Garante que o arquivo `config.json` exista. Caso contrário, cria um arquivo vazio.
- **Leitura de configuração**: Permite ler e exibir as configurações atuais do arquivo `config.json`.
- **Escrita de configuração**: Permite que o usuário insira um nome de servidor, endereço IP e senha, salvando-os no arquivo de configuração.
- **Validação de IP**: Valida se o endereço IP fornecido está em um formato correto.
- **Interface de terminal**: Utiliza o pacote `colorama` para fornecer uma interface de terminal colorida e amigável.

## Pré-requisitos

Certifique-se de ter o Python 3.6+ instalado em seu sistema.

### Dependências

- **colorama**: Para adicionar cores no terminal.
- **ipaddress**: Biblioteca padrão do Python para validar endereços IP.

Você pode instalar as dependências usando o pip:

```bash
pip install colorama
```

## Como usar

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/NKormann/config_manager.git
   cd config_manager
   ```

2. **Execute o programa**:

   ```bash
   python config_manager
   ```

   O programa exibirá um menu com as seguintes opções:

   - **1 - Ler configuração (Read configuration)**: Exibe as configurações atuais salvas no arquivo `config.json`.
   - **2 - Escrever configuração (Write configuration)**: Permite que o usuário insira um novo nome de servidor, IP e senha, validando o IP antes de salvar.

3. **Interação**:

   - Selecione uma das opções do menu.
   - Para ler as configurações, a aplicação exibirá as informações contidas no arquivo `config.json`.
   - Para escrever configurações, insira o nome do servidor, o endereço IP e a senha quando solicitado. O IP será validado, e o programa informará se o IP for inválido.
   - Você poderá realizar múltiplas operações em sequência ou sair do programa.

## Estrutura do Projeto

```bash
config_manager/
│
├── config.json         # Arquivo de configuração gerado automaticamente
├── config_manager.py   # Script principal com o código do gerenciador
├── README.md           # Documentação do projeto
```

## Exemplos

### 1. Ler Configuração

Quando o arquivo de configuração estiver vazio ou inválido, será exibida uma mensagem apropriada.

Exemplo de saída:

```bash
===== Gerenciador de Configuração =====
1 - Ler configuração (Read configuration)
2 - Escrever configuração (Write configuration)

Digite a opção desejada: 1

O arquivo 'config.json' está vazio ou contém dados inválidos.
```

### 2. Escrever Configuração

Quando a opção de escrita é selecionada, você será solicitado a fornecer o nome do servidor, IP e senha. O endereço IP será validado antes de ser salvo.

Exemplo de entrada:

```bash
===== Gerenciador de Configuração =====
1 - Ler configuração (Read configuration)
2 - Escrever configuração (Write configuration)

Digite a opção desejada: 2

=== Escrever Configuração ===
Informe o nome do servidor: MeuServidor
Informe o IP do servidor: 192.168.0.1
Informe a senha do servidor: senha123
Configuração salva com sucesso
