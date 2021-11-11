from utils.config_parser import GOREST_AUTH_TOKEN

HEADERS_WITH_AUTHORIZATION = {"Accept": "application/json",
                              "Content-Type": "application/json",
                              "Authorization": "Bearer " + GOREST_AUTH_TOKEN}

HEADERS_WITHOUT_AUTHORIZATION = {"Accept": "application/json",
                                 "Content-Type": "application/json"}
