from pathlib import Path

from configargparse import (
    ArgumentParser,
    ArgumentDefaultsHelpFormatter,
    YAMLConfigFileParser,
)
from configargparse import Namespace

BASE_DIR = Path(__file__).parent.resolve()
CONFIG_FILE_PATH = BASE_DIR.joinpath("config.yml")

ENV_VAR_PREFIX = "PD_"


def setup_args_parser() -> ArgumentParser:
    parser = ArgumentParser(
        auto_env_var_prefix=ENV_VAR_PREFIX,
        default_config_files=[CONFIG_FILE_PATH],
        config_file_parser_class=YAMLConfigFileParser,
        args_for_setting_config_path=["-c", "--config-file"],
        config_arg_help_message="Config file path",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )

    api_group = parser.add_argument_group("API")
    api_group.add_argument(
        "--host", type=str, default="localhost", help="API host"
    )
    api_group.add_argument("--port", type=int, default=8080, help="API port")
    api_group.add_argument(
        "--log-sql", action="store_true", help="log SQL queries"
    )

    # TODO
    # api_group.add_argument(
    #     "--ssl-cert", type=str, default="/ssl/cert.pem", help="SSL certificate"
    # )
    # api_group.add_argument(
    #     "--ssl-key", type=str, default="/ssl/key.pem", help="SSL key"
    # )
    # api_group.add_argument(
    #     "--ssl-password", type=str, default="dose-chip", help="SSL password"
    # )

    db_group = parser.add_argument_group("Database")
    db_group.add_argument(
        "--db-host", type=str, default="postgres", help="Database IP"
    )
    db_group.add_argument(
        "--db-port", type=int, default=5432, help="Database port"
    )
    db_group.add_argument(
        "--db-user", type=str, default="postgres", help="Database user name"
    )
    db_group.add_argument(
        "--db-password",
        type=str,
        default="postgres",
        help="Database user password",
    )
    db_group.add_argument(
        "--db-name",
        type=str,
        default="db",
        help="Name of the database to connect to",
    )

    return parser


def parse_args() -> Namespace:
    parser = setup_args_parser()
    args = parser.parse_args()
    args.db_url = get_db_url(args)
    return args


def get_db_url(args: Namespace) -> str:
    db_url = "postgresql+asyncpg://{}:{}@{}:{}/{}"
    db_url = db_url.format(
        args.db_user, args.db_password, args.db_host, args.db_port, args.db_name
    )
    return db_url
