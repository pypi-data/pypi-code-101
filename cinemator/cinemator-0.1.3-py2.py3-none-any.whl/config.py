OMDB_URL = "http://www.omdbapi.com"

API_KEY_PATH = "/Users/duduok/Desktop/secret.txt"
secrets = open(API_KEY_PATH, "r")
OMDBAPI_KEY = secrets.read()

message0 = "* This Command Line Tool is implemented to provide search functionality."
message1 = "* For instance, search for all movies with the word Planet In the title."
message2 = "* Show details of a specific movie."
message3 = "* We wanted to implement ith an option to show Rotten Tomatoes ratings too."
message4 = "* But during development we find out OMDB api is not providing that information any more"
message5 = "* We have kept the implementation to update the tool with fandango api for that details"

message = f"{message0}\n{message1}\n{message2}\n{message3}\n{message4}\n{message5}\n"