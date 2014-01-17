__author__ = 'kpasech'

from config import Config
from storage import Storage
from domain.exceptions import SecurityException
from subprocess import check_output, CalledProcessError
from os import getcwd
import json
from datetime import datetime, timedelta

class SecurityProvider:

    def get_access_key(self):
        return self.__get_security_token_from_local_storage()


    def __get_key_from_remote(self):

        cmd = "{0}/external/oauth/oauth.exe".format(getcwd())
        try:
            result = check_output(["mono", cmd, Config.VKConfig.APP_ID, Config.VKConfig.SCOPE])
        except CalledProcessError as e:
            r = json.loads(e.output)
            raise SecurityException(r["description"])
            pass
        else:
            r = json.loads(result)
            if "auth_token" not in r:
                raise SecurityException("Unknown response  format from VK")

            auth_token = r["auth_token"]
            userId = r["userId"]
            expirationTime = r["expirationTime"]

            exp_time = datetime.now() + timedelta(seconds=int(expirationTime) - 1)
            self.__save_security_token_to_local_storage((auth_token, userId, exp_time))

            return auth_token, userId, exp_time
        pass

    def __save_security_token_to_local_storage(self, token):
        auth_token, userId, exp_time = (token)
        storage = Storage()
        storage.set("auth_token", auth_token)
        storage.set("userId", userId)
        storage.set("exp_time", str(exp_time))
        pass

    def __get_security_token_from_local_storage(self):
        storage = Storage()
        auth_token = storage.get("auth_token")
        userId = storage.get("userId")
        exp_time = storage.get("exp_time")

        date_format = "%Y-%m-%d %H:%M:%S.%f"

        if auth_token is None or userId is None or exp_time is None or \
                        datetime.now() >= datetime.strptime(exp_time, date_format):
            return self.__get_key_from_remote()

        return auth_token, userId, datetime.strptime(exp_time, date_format)
