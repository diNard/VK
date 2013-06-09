class Error(Exception):
    def __init__(self, code, msg):
        self.__code = code
        self.__msg = msg
    
    def __str__(self):
        return repr('VK Error #' + str(self.__code) + ': ' + self.__msg)