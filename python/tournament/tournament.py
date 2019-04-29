def build_results_array(tournament_results):
    """
    builds results. Returns an object of the following form:
    {
        team1: {
            matches_played: int,
            wins: int,
            draws: int, 
            losses: int,
        }
        team2: {
            ...
        }

        ...

        teamn: {
            ...
        }
    }
    """
    dict_of_results = {}
    array_of_input = []
    lines = tournament_results.split('\n')
    for line in lines:
        array_of_input.append(line.split(';'))

    for result in array_of_input:
        for team in result[0:2]:
            if team not in dict_of_results:
                dict_of_results[team] = {'matches_played': 0,
                                         'wins': 0,
                                         'draws': 0,
                                         'losses': 0,}
                                         
        if result[2] == "win":
            dict_of_results[result[0]]['wins'] += 1
            dict_of_results[result[1]]['losses'] += 1
        else if result[2] == "loss":
            dict_of_results[result[0]]['losses'] += 1
            dict_of_results[result[1]]['wins'] += 1
        else if result[2] == "draw":
            dict_of_results[result[0]]['draw'] += 1
            dict_of_results[result[1]]['draw'] += 1
        
        dict_of_results[result[0]]['matches_played'] += 1
        dict_of_results[result[1]]['matches_played'] += 1


def tally(tournament_results):
    results = build_results_array(tournament_results)
