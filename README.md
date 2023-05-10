<!-- knitting_portal/
├── app/
│ ├── **init**.py
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── routers/
│ │ ├── **init**.py
│ │ ├── products.py
│ │ └── users.py
│ └── scrapers/
│ ├── **init**.py
│ ├── base.py
│ └── somewebsite.py
├── tests/
│ ├── **init**.py
│ ├── conftest.py
│ └── test_main.py
├── Dockerfile
├── requirements.txt
├── README.md
└── .env -->

touch ./{main,database,models}.py
touch ./routers/{**init**,products,users}.py
touch ./scrapers/{**init**,base,wollplatz}.py

touch .env
