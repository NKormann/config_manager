import json
import os
import sys
from typing import Dict
from colorama import init, Fore, Style
import ipaddress

init(autoreset=True)

CONFIG_FILENAME = 'config.json'


def ensure_config_file_exists(filename: str = CONFIG_FILENAME) -> None:
    """
    Verifica se o arquivo de configuração existe. Caso contrário, cria um arquivo vazio.

    Args:
        filename (str): Nome do arquivo de configuração.
    """
    if not os.path.isfile(filename):
        try:
            with open(filename, 'w') as file:
                json.dump({}, file, indent=4)
            print(f"\n{Fore.GREEN}Arquivo '{filename}' criado com sucesso.{Style.RESET_ALL}")
        except IOError as e:
            print(f"\n{Fore.RED}Erro ao criar o arquivo '{filename}': {e}{Style.RESET_ALL}")
            sys.exit(1)


def load_config(filename: str = CONFIG_FILENAME) -> Dict[str, str]:
    """
    Carrega a configuração do arquivo JSON.

    Args:
        filename (str): Nome do arquivo de configuração.

    Returns:
        Dict[str, str]: Dicionário com a configuração carregada.
    """
    try:
        with open(filename, 'r') as file:
            config = json.load(file)
            return config
    except json.JSONDecodeError:
        print(f"\n{Fore.YELLOW}O arquivo '{filename}' está vazio ou contém dados inválidos.{Style.RESET_ALL}")
        return {}
    except IOError as e:
        print(f"\n{Fore.RED}Erro ao ler o arquivo '{filename}': {e}{Style.RESET_ALL}")
        sys.exit(1)


def save_config(config: Dict[str, str], filename: str = CONFIG_FILENAME) -> None:
    """
    Salva a configuração no arquivo JSON.

    Args:
        config (Dict[str, str]): Dicionário com a configuração a ser salva.
        filename (str): Nome do arquivo de configuração.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(config, file, indent=4)
        print(f"\n{Fore.GREEN}Configuração salva com sucesso no arquivo '{filename}'.{Style.RESET_ALL}")
    except IOError as e:
        print(f"\n{Fore.RED}Erro ao escrever no arquivo '{filename}': {e}{Style.RESET_ALL}")
        sys.exit(1)


def display_menu() -> None:
    """
    Exibe o menu de opções para o usuário.
    """
    print(f"\n{Fore.CYAN}===== Gerenciador de Configuração ====={Style.RESET_ALL}")
    print(f"{Fore.CYAN}1 - Ler configuração (Read configuration){Style.RESET_ALL}")
    print(f"{Fore.CYAN}2 - Escrever configuração (Write configuration){Style.RESET_ALL}")


def read_configuration() -> None:
    """
    Lê e exibe a configuração atual do arquivo JSON.
    """
    config = load_config()
    if not config:
        print(f"\n{Fore.YELLOW}O arquivo não contém informações.{Style.RESET_ALL}")
    else:
        print(f"\n{Fore.GREEN}Configuração atual:{Style.RESET_ALL}")
        print(json.dumps(config, indent=4))


def is_valid_ip(ip: str) -> bool:
    """
    Valida se o IP fornecido tem um formato válido.

    Args:
        ip (str): Endereço IP a ser validado.

    Returns:
        bool: True se o IP for válido, False caso contrário.
    """
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


def write_configuration() -> None:
    """
    Solicita informações do usuário e salva no arquivo JSON.
    """
    print(f"\n{Fore.MAGENTA}=== Escrever Configuração ==={Style.RESET_ALL}")
    server_name = input(f"{Fore.CYAN}Informe o nome do servidor: {Style.RESET_ALL}").strip()
    server_ip = input(f"{Fore.CYAN}Informe o IP do servidor: {Style.RESET_ALL}").strip()
    server_password = input(f"{Fore.CYAN}Informe a senha do servidor: {Style.RESET_ALL}").strip()

    if not server_name or not server_ip or not server_password:
        print(f"\n{Fore.RED}Todos os campos são obrigatórios. Operação cancelada.{Style.RESET_ALL}")
        return

    if not is_valid_ip(server_ip):
        example_ip = "192.168.1.10"
        print(f"\n{Fore.RED}O endereço IP '{server_ip}' é inválido. Por favor, informe no formato válido -> {example_ip}.{Style.RESET_ALL}")
        return

    config = {
        "server_name": server_name,
        "server_ip": server_ip,
        "server_password": server_password
    }

    save_config(config)
    print(f"\n{Fore.GREEN}Configuração salva:{Style.RESET_ALL}")
    print(json.dumps(config, indent=4))


def get_user_choice() -> str:
    """
    Obtém a escolha do usuário.

    Returns:
        str: Opção escolhida pelo usuário.
    """
    return input(f"\n{Fore.CYAN}Digite a opção desejada: {Style.RESET_ALL}").strip()


def main() -> None:
    """
    Função principal que gerencia o fluxo do programa.
    """
    ensure_config_file_exists()

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == '1':
            read_configuration()
        elif choice == '2':
            write_configuration()
        else:
            print(f"\n{Fore.RED}Opção inválida. Por favor, tente novamente.{Style.RESET_ALL}")
            continue

        continuar = input(f"\n{Fore.CYAN}Deseja realizar outra operação? (s/n): {Style.RESET_ALL}").strip().lower()
        if continuar != 's':
            print(f"\n{Fore.GREEN}Encerrando o Gerenciador de Configuração. Até logo!{Style.RESET_ALL}\n")
            break


if __name__ == "__main__":
    main()
