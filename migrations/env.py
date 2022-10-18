from __future__ import with_statement
from alembic import context
from sqlalchemy import engine_from_config, pool
from logging.config import fileConfig
import logging

# este é o objeto Alembic Config, que fornece
# acesso aos valores dentro do arquivo .ini em uso.
config = context.config

# Interprete o arquivo de configuração para log do Python.
# Esta linha configura basicamente os loggers.
fileConfig(config.config_file_name)
logger = logging.getLogger('alembic.env')

# adicione o objeto MetaData do seu modelo aqui
# para suporte a 'geração automática'
# de myapp import mymodel
# target_metadata = mymodel.Base.metadata
from flask import current_app
config.set_main_option('sqlalchemy.url',
                       current_app.config.get('SQLALCHEMY_DATABASE_URI'))
target_metadata = current_app.extensions['migrate'].db.metadata

# outros valores da configuração, definidos pelas necessidades de env.py,
# pode ser adquirido:
# my_important_option = config.get_main_option("my_important_option")
#...etc


def run_migrations_offline():
    """Execute as migrações no modo 'offline'.

    Isso configura o contexto com apenas um URL
    e não um Motor, embora um Motor seja aceitável
    aqui também. Ignorando a criação do mecanismo
    nem precisamos que uma DBAPI esteja disponível.

    Chamadas para context.execute() aqui emitem a string dada para o
    saída do script.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Execute migrações no modo 'online'.

    Neste cenário, precisamos criar um Engine
    e associar uma conexão com o contexto.

    """

    # este retorno de chamada é usado para evitar que uma migração automática seja gerada
    # quando não há alterações no esquema
    # referência: http://alembic.zzzcomputing.com/en/latest/cookbook.html
    def process_revision_directives(context, revision, directives):
        if getattr(config.cmd_opts, 'autogenerate', False):
            script = directives[0]
            if script.upgrade_ops.is_empty():
                directives[:] = []
                logger.info('No changes in schema detected.')

    engine = engine_from_config(config.get_section(config.config_ini_section),
                                prefix='sqlalchemy.',
                                poolclass=pool.NullPool)

    connection = engine.connect()
    context.configure(connection=connection,
                      target_metadata=target_metadata,
                      process_revision_directives=process_revision_directives,
                      **current_app.extensions['migrate'].configure_args)

    try:
        with context.begin_transaction():
            context.run_migrations()
    finally:
        connection.close()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
