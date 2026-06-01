
from app.models import categoria
from app.models import produtos
from app.models import usuario
from app.models import movimentacao

#gerar a migration
#python -m alembic revision --autogenerate -m "Criando as tabelas do banco de dados"
#python -m alembic upgrade head