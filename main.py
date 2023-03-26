import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker
from models import Base, Publisher, Book, Shop, Stock, Sale


# данные для подключения к базе
dbname = "netology_db"
dbuser = "postgres"
dbpassword = "postgres"

DSN = f"postgresql://{dbuser}:{dbpassword}@localhost:5432/{dbname}"
engine = sq.create_engine(DSN)

def create_tables(engine):
    Base.metadata.create_all(engine)

create_tables(engine)

# сессия
Session = sessionmaker(bind=engine)
session = Session()

publisher_name = input("Какой издатель нужен? ")

sales = (
    session.query(Book.title, Shop.name, Sale.price, Sale.date_sale)
    .join(Stock)
    .join(Shop)
    .join(Sale)
    .join(Publisher)
    .filter(Publisher.name == publisher_name)
    .all()
)

for sale in sales:
    title, shop_name, price, date_sale = sale
    date_str = date_sale.strftime("%d-%m-%Y")
    print(f"{title} | {shop_name} | {price} | {date_str}")