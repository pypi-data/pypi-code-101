from cinemat.restful_events import make_get




def pretty_printer(media_list,parameter_type):
    print("")
    print(f"==============================  Search results by {parameter_type}  =====================================")
    print("")
    for i in range(1, len(media_list)):
        print(f"{i}) {media_list[i]['Title']}, Release Year:{media_list[i]['Year']}, category:{media_list[i]['Type']}")
    print("")
    print("==============================================================================================")
    return print("")
    
def find(title, parameter, parameter_type):
    if parameter_type == "type":
        if parameter in ['movie', 'series', 'episode']:
            parameters = {"s": title, "type": parameter}
        else:    
            print('Please enter a valid type: movie, series, episode')
    elif parameter_type == "imdb":
        parameters = {"s":title, "i":parameter}
    elif parameter_type == "year":
        parameters = {"s":title, "y":parameter}
    else:
        parameters = {"s":title}
    response = make_get(parameters)
    if response['Response']=='False':
        return print('OOOPS!!! Sorry, Media not found')
    else:    
        media_list = response["Search"]
        return pretty_printer(media_list,parameter_type)


