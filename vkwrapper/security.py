__author__ = 'kpasech'

from config import Config
from domain.exceptions.securityexception import SecurityException

class SecurityProvider:

    def get_access_key(self):
        return self.__get_security_token_from_local_storage() or self.__get_key_from_remote()


    def __get_key_from_remote(self):
        # TODO: IMPLEMENT GET TOKEN FUNCTIONALITY
        pass

    def __save_security_token_to_local_storage(self, token):
        # TODO: IMPLEMENT SAVE TOKEN FUNCTIONALITY TO LOCAL STORAGE
        pass

    def __get_security_token_from_local_storage(self):
        # TODO: IMPLEMENT GET TOKEN FUNCTIONALITY FROM LOCAL STORAGE
        return None
