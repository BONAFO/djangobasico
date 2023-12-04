def add_tuple(tuple_ob, data, insert_dict=False):
    #Parsing the tuple to a list
    aux = list(tuple_ob)
    
    
    if type(data) is list or type(data) is tuple:
        #If data is a list or a tuple itirate every value and save it
        for dat in data:
            aux.insert(len(aux), dat)
    elif type(data) is dict:
        #If data is a dict
        for dat in data:
            #IF insert_dict = True
            #Save every object inside of the dict as dicts
            if insert_dict:
                aux.insert(len(aux), {dat: data[dat]})
            #IF insert_dict = False
            #Save only the value
            else:
                aux.insert(len(aux), data[dat])
    else:
        #Else just insert it
        aux.insert(len(aux), data)
    return tuple(aux)
