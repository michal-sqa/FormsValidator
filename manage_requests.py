import _environment

def prepare_get_request(env, get_request_specification):
    separator = '&' if '?' in get_request_specification else '?'
    request = f"http://{env.server_and_port}{get_request_specification}{separator}loginname={env._user}&loginpassword={env._password}"
    return request