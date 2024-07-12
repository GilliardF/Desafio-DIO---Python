'''
Integrando o MongoDB e MySQL com Python

Criando ambiente virtual
python -m venv /home/gilliard/Documentos/Desafio-DIO---Python/
source /home/gilliard/Documentos/Desafio-DIO---Python/bin/activate
pip install -U pip setuptools wheel
pip install flake8
pip install sqlalchemy
pip install pymongo

=========================================================================

docker run --name lab_mongodb -p 27017:27017 \
-e MONGO_INITDB_ROOT_USERNAME=gilliard \
-e MONGO_INITDB_ROOT_PASSWORD=8921 \
-d mongo

'''

import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.engine.reflection import Inspector
from sqlalchemy.orm import Session
from sqlalchemy.sql import select



# Criando a base de dados

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id_user = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    cpf = Column(String(9), nullable=False)
    endereco = Column(String, nullable=False)
    
    contas = relationship('Conta', back_populates='users')
    
    def __repr__(self):
        return f'User [name={self.name}, cpf={self.cpf}, endereco={self.endereco}]'
    
class Conta(Base):
    __tablename__ = 'conta'
    
    id_account = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(String, nullable=False)
    agencia = Column(String, nullable=False)
    numero_conta = Column(String, nullable=False)
    id_cliente = Column(Integer, ForeignKey('users.id_user'))
    saldo = Column(Float, nullable=False)
    
    users = relationship('User', back_populates='contas')  
    
    def __repr__(self):
        return f'Conta [tipo={self.tipo}, agencia={self.agencia}, numero_conta={self.numero_conta}, saldo={self.saldo}]'

    
# Conecção com o banco de dados

engine = create_engine('sqlite:///database.db')

Base.metadata.create_all(engine)

insp = Inspector.from_engine(engine)
print(insp.get_table_names())
print(insp.default_schema_name)


# Inserindo dados no banco de dados

def insert_data(session, user, account):
    session.add(user)
    session.commit()
    
    account.id_cliente = user.id_user
    session.add(account)
    session.commit()
    
with Session(engine) as session:    
    user1 = User(name='Gilliard', cpf='123456789', endereco='N/A')
    account1 = Conta(tipo='corrente', agencia='0001', numero_conta='123456', saldo=1000.0)
    insert_data(session, user1, account1)
    
    user2 = User(name='Fulano', cpf='987654321', endereco='N/A')
    account2 = Conta(tipo='corrente', agencia='0001', numero_conta='654321', saldo=1000.0)
    insert_data(session, user2, account2)
    

# Consultando dados no banco de dados


stmt_user = select(User)
for user in session.execute(stmt_user):
    print(user)
    
stmt_account = select(Conta)
for account in session.execute(stmt_account):
    print(account)
    

'''
Criar outras modelos de consultas
'''
