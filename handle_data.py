'''
    Holds functions for finding the cities in each country and recommedation list.
'''



def get_list_of_cities(country, home_country, dataframe): 
    if country == home_country: return []

    current_cities = []
    for i in dataframe.values:
        if str(country) == str(i[2]).strip():
            current_cities.append(i.tolist())
     
    return current_cities


'''
    Takes in a list of cities and returns a list of cities with the highest total score.
'''
def get_best_list_of_cities(state):
    best_list_of_cities = []
    
    while len(best_list_of_cities) <= 2:
        selected_best = []

        for i in state:
            if selected_best == []:
                selected_best = i
            if i[3] > selected_best[3]:
                selected_best = i
        state.remove(selected_best)
        best_list_of_cities.append(selected_best)

    return best_list_of_cities





    