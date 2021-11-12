from cinemat.restful_events import make_get


def show_details(movie_name, plot, tomatoes):
    if tomatoes == "tomat":
        parameters = {"t": movie_name, "plot": plot, "tomatoes": "true"}
    else:
        parameters = {"t": movie_name, "plot": plot}
    response = make_get(parameters)

    for parameter, detail in response.items():
        print(f"{parameter} : {detail}")

    return print("Please see the details of the media above")

def show_details_imdb(imdb, plot):

    parameters = {"i":imdb, "plot": plot}
    response = make_get(parameters)

    for parameter, detail in response.items():
        print(f"{parameter} : {detail}")
    print("")    
    return print("Please see the details of the media above")
