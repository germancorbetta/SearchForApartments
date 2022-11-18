import yaml
import requests
import sqlite3

# Load Properties
try:
    with open("configuration.yml", "r") as stream:
        try:
            properties = yaml.safe_load(stream)

            apiToken = properties["telegram"]["apiToken"]
            telegramChats = properties["telegram"]["chats"]
            databaseName = properties["database"]["name"]
            pages = properties["pages"]

        except yaml.YAMLError as exc:
            print(exc)

except FileNotFoundError:
    print("Missing configuration.yml file")
    exit()

# Recover sites from properties file
def loadSites():
    return pages

# Send Telegram Message to every Chat ID
def sendToTelegram(message):
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
    for chat in telegramChats:
        requests.post(apiURL, json={'chat_id': chat, 'text': message})
    
# Create Database
def CreateLinksTable():
    connection=sqlite3.connect(databaseName)
    try:
        connection.execute("""create table links (
                                codigo integer primary key autoincrement,
                                url text
                        )""")
        print("Table LINKS created")                        
    except Exception as e:
        print("Using pre-existent database table")           
    finally:
        connection.close()

# Insert url into database
def InsertLink(url):
    connection=sqlite3.connect(databaseName)
    try:
        connection.execute("insert into links(url) values (?)", (url,))
        connection.commit()
    except Exception as e:
        print(e)                    
    finally:
        connection.close()

# Boolean to check if url exists in database (return True = it exists)
def LinkExists(url):
    connection=sqlite3.connect(databaseName)
    try:
        cursor=connection.execute("select url from links where url=?", (url,))
        row=cursor.fetchall()
        if len(row)>0:
            return True
        else:
            return False
    except Exception as e:
        print(e)                    
    finally:
        connection.close()
