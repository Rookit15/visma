from OwnParser import *


class UriParser:
    def ParseUri(uri):  # Parsing function starts
        parsed = OwnParser.ParseURI(uri)  # calls own parsing function

        if parsed["Scheme"] != "visma-identity://":  # check that scheme is right
            return -1

        match parsed["Path"]:  # different cases for different path's. always return -1 if address is incorrect and something goes wrong
            case "login":
                param = UriParser.ParseParameters(parsed["Parameters"], 0)
                # check that parameters are right
                if param[0] == "source" and '&' not in param[1]:
                    result = {param[0]: param[1]}
                    return parsed["Path"], result
                return -1

            case "confirm":
                param = UriParser.ParseParameters(parsed["Parameters"], 1)
                try:
                    # check that parameters are right
                    if param[0][0] == "source" and param[1][0] == "paymentnumber":
                        result = {param[0][0]: param[0]
                                  [1], param[1][0]: param[1][1]}
                        return parsed["Path"], result
                except:
                    return -1

            case "sign":
                param = UriParser.ParseParameters(parsed["Parameters"], 2)
                try:
                    # check that parameters are right
                    if param[0][0] == "source" and param[1][0] == "documentid":
                        result = {param[0][0]: param[0]
                                  [1], param[1][0]: param[1][1]}
                        return parsed["Path"], result
                except:
                    return -1

    # parse parameters from query, i is defining which path are we using
    def ParseParameters(query, i):
        if i == 0:        # return -1 if parameters aren't right which means URI is incorrect
            param = query.split('=')
            if isinstance(param[1], str):
                return param

        elif i == 1:
            a = query.split('&')
            param = []
            for i in a:
                param.append(i.split('='))

            try:  # payment number should be int and source should be string, return -1 if it isn't
                isinstance(param[0][1], str) and int(param[1][1])
                return param
            except:
                return -1

        elif i == 2:
            a = query.split('&')
            param = []
            for i in a:
                param.append(i.split('='))

            try:  # source and documentid should be string, return -1 if it isn't
                isinstance(param[0][1], str) and isinstance(param[1][1], str)
                return param
            except:
                return -1
