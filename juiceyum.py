import argparse
import json
import urllib.request
import sys

def load_repos():
    try:
        with open("repos.json", "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error leyendo repos.json: {e}")
        sys.exit(1)

def load_apps(repo_url):
    try:
        with urllib.request.urlopen(repo_url) as response:
            data = response.read().decode()
            return json.loads(data)
    except Exception as e:
        print(f"Error descargando repositorio de apps: {e}")
        sys.exit(1)

def install_app(app_name, apps):
    if app_name in apps:
        print(f"App '{app_name}' encontrada en repositorio.")
        # Aquí luego pones lógica para descargar e instalar
    else:
        print(f"App '{app_name}' NO encontrada en el repositorio.")

def main():
    parser = argparse.ArgumentParser(prog="juiceyum")
    subparsers = parser.add_subparsers(dest="command")

    install_parser = subparsers.add_parser("install", help="Instalar una app")
    install_parser.add_argument("app_name", help="Nombre de la app a instalar")

    args = parser.parse_args()

    if args.command == "install":
        repos = load_repos()
        # Usamos el repo principal
        repo_url = repos.get("juiceyum-apps")
        if not repo_url:
            print("No se encontró 'juiceyum-apps' en repos.json")
            sys.exit(1)

        apps = load_apps(repo_url)
        install_app(args.app_name, apps)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

