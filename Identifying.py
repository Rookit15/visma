from UriParser import *


def main():

    try:
        urlString = "visma-identity://login?source=severa"
        path, result = UriParser.ParseUri(urlString)
        print("Login: ", path, result)

    except:
        print("Login URI was incorrect")
    try:
        urlString = "visma-identity://confirm?source=netvisor&paymentnumber=102226"
        path, result = UriParser.ParseUri(urlString)
        print("Confirm: ", path, result)

    except:
        print("Confirm URI was incorrect")
    try:
        urlString = "visma-identity://sign?source=vismasign&documentid=105ab44"
        path, result = UriParser.ParseUri(urlString)
        print("Sign: ", path, result)

    except:
        print("sign URI was incorrect")


main()
