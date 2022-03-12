class TstException(BaseException):
    def message(self):
        pass

class no_access_exception(TstException):
    def message(self):
        'It seems the task is from a private contest and tst cannot parse it'

class invalid_link_exception(TstException):
    def __init__(self, link: str):
        self.link = link

    def message(self):
        return f'You have entered link that is now accessible:\n{self.link}'
    
class server_error_exception(TstException):
    def message(self): 
        return f'The server has encountered a situation it does not know how to handle'

class invalid_hostname_exception(TstException):
    def __init__(self, hostname: str):
        self.hostname = hostname

    def message(self):
        return f'The {self.hostname} server is not supported by the tst'

class cpp_complilation_error_exception(TstException):
    def __init__(self, stderr: str):
        self.std = stderr

    def message(self):
        return f"COMPILATION ERROR:\n'{self.std}'"


class cpp_runtime_error_exception(TstException):
    def __init__(self, stderr):
        self.std = stderr

    def message(self):
        return f"RUNTIME ERROR\n{self.std}"
