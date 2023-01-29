class OwnParser:  # own parsing class and function

    def ParseURI(uriString):
        # every working address have these and parameters are added to dict if there are any
        parsed = {"Scheme": "", "Path": ""}

        parsed["Scheme"] = (uriString[0:17])

        Path = ""
        Param = ""
        selection = 0
        for i in uriString[17:]:  # finds path and parameters from address
            if i == '?':
                selection = 1
                continue
            if selection == 0:
                Path = Path + i
            elif selection == 1:
                Param = Param+i
        parsed["Path"] = Path
        parsed["Parameters"] = Param

        return parsed  # returns parsed dictionary which include parts of address
