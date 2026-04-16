from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "data" / "usuarios.csv"
OUTPUT_FILE = BASE_DIR / "data" / "usuarios_com_mensagens.csv"


def extrair_dados(caminho_arquivo: Path) -> pd.DataFrame:
    """Lê os dados do arquivo CSV e valida as colunas obrigatórias."""
    if not caminho_arquivo.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_arquivo}")

    df = pd.read_csv(caminho_arquivo)

    colunas_esperadas = {"id", "nome", "conta", "cartao"}
    colunas_encontradas = set(df.columns)

    if not colunas_esperadas.issubset(colunas_encontradas):
        faltando = colunas_esperadas - colunas_encontradas
        raise ValueError(f"Colunas obrigatórias ausentes no CSV: {faltando}")

    return df


def gerar_mensagem(nome: str, conta: str, cartao: str) -> str:
    """Gera uma mensagem personalizada para cada usuário."""
    nome = str(nome).strip()
    conta = str(conta).strip()
    cartao = str(cartao).strip()

    return (
        f"Olá, {nome}! Sua conta {conta} e seu cartão {cartao} foram processados com sucesso. "
        f"Aproveite as soluções digitais disponíveis para facilitar sua rotina financeira."
    )


def transformar_dados(df: pd.DataFrame) -> pd.DataFrame:
    """Cria a coluna de mensagens personalizadas."""
    df = df.copy()
    df["mensagem"] = df.apply(
        lambda linha: gerar_mensagem(
            nome=linha["nome"],
            conta=linha["conta"],
            cartao=linha["cartao"],
        ),
        axis=1,
    )
    return df


def carregar_dados(df: pd.DataFrame, caminho_saida: Path) -> None:
    """Salva os dados transformados em um novo CSV."""
    caminho_saida.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(caminho_saida, index=False, encoding="utf-8-sig")


def main() -> None:
    try:
        print("=" * 50)
        print("INICIANDO PROCESSO ETL")
        print("=" * 50)

        print("\n[1/3] Extraindo dados...")
        usuarios = extrair_dados(INPUT_FILE)
        print(f"Dados extraídos com sucesso: {len(usuarios)} registros encontrados.")

        print("\n[2/3] Transformando dados...")
        usuarios_transformados = transformar_dados(usuarios)
        print("Mensagens personalizadas geradas com sucesso.")

        print("\n[3/3] Carregando dados...")
        carregar_dados(usuarios_transformados, OUTPUT_FILE)
        print(f"Arquivo final salvo em: {OUTPUT_FILE}")

        print("\nPROCESSO ETL CONCLUÍDO COM SUCESSO!")

    except Exception as erro:
        print("\nERRO NO PROCESSO ETL")
        print(f"Detalhes: {erro}")
        raise


if __name__ == "__main__":
    main()
