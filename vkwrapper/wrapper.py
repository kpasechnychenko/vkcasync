from kivy.network.urlrequest import UrlRequest
from datetime import datetime
from vkwrapper.security import SecurityProvider
from domain.exceptions import WrapperException

class Wrapper():

    def __init__(self):
        self.auth_token = None
        self.exp_time = None
        self.user_id = None
        self.method_name = None
        self.url = "https://api.vk.com/method/{0}?access_token={1}{2}"

    def get(self, parameters, on_success=None, on_error=None):

        if self.auth_token is None or self.user_id is None or self.exp_time is None or \
                        datetime.now() >= self.exp_time:

            provider = SecurityProvider()
            self.auth_token, self.user_id, self.exp_time = provider.get_access_key()

        if self.method_name is None:
            raise WrapperException("API method name has not been specified")

        params = ""
        for key, value in parameters.items():
            params += "&{0}={1}".format(str(key), str(value))
            pass

        request = UrlRequest(self.url.format(self.method_name, self.auth_token, params),
                             on_success or self.on_success,
                             on_error or self.on_error)
        pass

    def get_current_user(self):
        user = None
        provider = SecurityProvider()
        auth_token, user, exp_time = provider.get_access_key()
        return user

    def get_current_token(self):
        auth_token = None
        provider = SecurityProvider()
        auth_token, user, exp_time = provider.get_access_key()
        return auth_token

    def get_current_exp_time(self):
        exp_time = None
        provider = SecurityProvider()
        auth_token, user, exp_time = provider.get_access_key()
        return exp_time
