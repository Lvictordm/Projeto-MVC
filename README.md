# Instale o requiriments.txt


no terminal:
pip install -r requirements.txt  


# Iniciar o alembic
python -m alembic init migrations


# gerar a migration
Python -m alembic revision --autogenerate -m "criar tabela usuario"