# Knitportal

## Getting Started

Navigate to the root folder of the application, then create a virtual environment for the application using the following command on the terminal

```zsh

 python3 -m venv ./
```

Activate the virtual environment

```zsh

source .venv/bin/activate
```

### Install the required dependencies

```zsh

pip3 install -r requirements.txt
```

### Run migration

```zsh

alembic upgrade head
```

### Start the server

```zsh

uvicorn knitportal.main:start
```

## Setting up the database(SQLite) connection

1. Download and install [TablePlus](https://tableplus.com/download). This app will be use for setting up the database connection.
2. Copy the full path of sql_app.db file found in the root folder of knitportal
3. Open the [TablePlus](https://tableplus.com/download) app, click on the plus(+) sign on the top of the app window to add a new database. Select SQLite and then click on the 'create' button.
4. A pop up SQLite Connection form will be displayed, input your desired nam in the name section, and then paste the copied sql_app.db file path in the database path section.
5. Click on 'connect'.

## Making GET and POST requests

1. Download and install <a href="https://www.postman.com/downloads/" target="_blank" rel="noopener noreferrer" >Postman</a>. This app will be used for the sending HTTP requests to the server.
2. Open the app
3. To send POST request, in our case, to scrape [https://www.wollplatz.de](https://www.wollplatz.de). Toggle the type of request to POST, paste this url `http://localhost:8000/scrape` in the url bar and then click on send
4. To send GET request, i.e., to view the scraped data from [https://www.wollplatz.de](https://www.wollplatz.de). Toggle the type of request to GET, paste this url `http://localhost:8000/products` in the url bar and then click on send. Alternatively, you can go to `http://localhost:8000/products` on browser to view the scraped data.

