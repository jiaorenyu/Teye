permit_token_list = []


def init(token_list):
    global permit_token_list
    permit_token_list = token_list


def is_token_valid(token):
    return token in permit_token_list
