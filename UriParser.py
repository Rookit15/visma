from OwnParser import *


class UriParser:
    def ParseUri(uri):  # Parsing function starts
        parsed = OwnParser.ParseURI(uri)  # calls own parsing function

        if parsed["Scheme"] != "visma-identity://":  # check that scheme is right
            return -1

        match parsed["Path"]:  # different cases for different path's. always return -1 if address is incorrect and something goes wrong
            case "login":
                result = UriParser.LoginParse(parsed["Parameters"])
                if result != -1:
                    return parsed["Path"], result
                else:
                    return -1

            case "confirm":
                result = UriParser.ConfirmParse(parsed['Parameters'])
                if result != -1:
                    return parsed["Path"], result

            case "sign":
                result = UriParser.SignParse(parsed["Parameters"])
                if result != -1:
                    return parsed["Path"], result
                else:
                    return -1

    def Split(query):
        a = query.split('&')
        param = []
        for i in a:
            param.append(i.split('='))
        return param

    def LoginParse(query):
        # return -1 if parameters aren't right which means URI is incorrect
        param = UriParser.Split(query)
        if isinstance(param[0][1], str):
            if param[0][0] == "source" and '&' not in param[0][1]:
                result = {param[0][0]: param[0][1]}
                # returns result parameters as dictionary
                return result
            else:
                return -1

    def ConfirmParse(query):
        param = UriParser.Split(query)
        try:  # payment number should be int and source should be string, return -1 if it isn't
            if isinstance(param[0][1], str) and int(param[1][1]):
                if param[0][0] == "source" and param[1][0] == "paymentnumber":
                    result = {param[0][0]: param[0]
                              [1], param[1][0]: param[1][1]}
                    # returns result parameters as dictionary
                    return result
            else:
                return -1
        except:
            return -1

    def SignParse(query):
        param = UriParser.Split(query)
        try:
            # check that parameters are right
            if isinstance(param[0][1], str) and isinstance(param[1][1], str):
                if param[0][0] == "source" and param[1][0] == "documentid":
                    result = {param[0][0]: param[0]
                              [1], param[1][0]: param[1][1]}
                    # returns result parameters as dictionary
                    return result
            else:
                return -1
        except:
            return -1
