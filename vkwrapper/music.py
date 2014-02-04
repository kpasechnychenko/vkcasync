from vkwrapper.wrapper import Wrapper
from domain.exceptions import VkMusicException
from vkwrapper.misic_genres import Genres


class Music():

    def __on_success(self, request, result, on_success):
        on_success(result)
        pass


    def __on_error(self, request, error):
        raise Exception(error["error_msg"])
        pass

    def __execute_get_request(self, method_name, on_success, parameters=dict()):
        w = Wrapper()
        w.method_name = method_name
        w.get(parameters,
              on_success=lambda request, result: self.__on_success(request, result, on_success),
              on_error= lambda request, error: self.__on_error(request, error))
        pass

    def get(self, on_success, owner_id=None, album_id=None, audio_ids=None, need_user=0, offset=None, count=None):

        parameters = dict()

        if owner_id is None:
            w = Wrapper()
            parameters["owner_id"] = w.get_current_user()
        else:
            parameters["owner_id"] = owner_id
        if album_id is not None:
            parameters["album_id"] = album_id

        if audio_ids is not None and len(audio_ids) > 0:
            audio_ids = [str(ai) for ai in audio_ids]
            parameters["audio_ids"] = ','.join(audio_ids)

        parameters["need_user"] = need_user
        if offset is not None:
            parameters["offset"] = offset
        if count is not None:
            parameters["count"] = count

        self.__execute_get_request("audio.get", on_success, parameters)
        pass

    def get_by_id(self, user_audio_ids, on_success):

        if user_audio_ids is None or len(user_audio_ids) < 1:
            raise VkMusicException("user_audio_ids is None or empty")

        parameters = dict()
        try:
            aud = ["{0}_{1}".format(str(a[0]), str(a[1])) for a in user_audio_ids]
            parameters["audios"] = ",".join(aud)

        except BaseException:
            raise VkMusicException("user_audio_ids has incorrect format")

        else:
            self.__execute_get_request("audio.getById", on_success, parameters)

        pass

    def search(self,
               q,
               on_success,
               auto_complete=1,
               lyrics=0,
               performer_only=0,
               sortSort=2,
               search_own=0,
               offsetOffset=None,
               count=None):

        parameters = dict()

        if q is None or len(q) < 1:
            raise VkMusicException("search criteria is Null or empty")

        parameters["q"] = q
        parameters["auto_complete"] = auto_complete
        parameters["lyrics"] = lyrics
        parameters["performer_only"] = performer_only
        parameters["sortSort"] = sortSort
        parameters["search_own"] = search_own

        if offsetOffset is not None:
            parameters["offsetOffset"] = offsetOffset

        if count is not None:
            parameters["count"] = count

        self.__execute_get_request("audio.search", on_success, parameters)
        pass

    def get_albums(self, on_success, owner_id=None, offset=None, count=None):
        parameters = dict()

        if owner_id is None:
            w = Wrapper()
            parameters["owner_id"] = w.get_current_user()
        else:
            parameters["owner_id"] = owner_id

        if offset is not None:
            parameters["offset"] = offset

        if count is not None:
            parameters["count"] = count

        self.__execute_get_request("audio.getAlbums", on_success, parameters)
        pass

    def get_recommendations(self, on_success, target_audio=None, user_id=None, offset=None, count=None, shuffle=1):
        parameters = dict()

        if target_audio is not None and len(target_audio) > 0:
            try:
                aud = ["{0}_{1}".format(str(a[0]), str(a[1])) for a in target_audio]
                parameters["target_audio"] = ",".join(aud)

            except BaseException:
                raise VkMusicException("target_audio has incorrect format")

        if user_id is None:
            w = Wrapper()
            parameters["user_id"] = w.get_current_user()
        else:
            parameters["user_id"] = user_id

        if offset is not None:
            parameters["offset"] = offset

        if count is not None:
            parameters["count"] = count
        parameters["shuffle"] = shuffle

        self.__execute_get_request("audio.getRecommendations", on_success, parameters)
        pass

    def get_popular(self, on_success, only_eng=0, genre=Genres.Rock, offset=None, count=None):
        parameters = dict()
        parameters["only_eng"] = only_eng
        parameters["genre_id"] = genre

        if offset is not None:
            parameters["offset"] = offset

        if count is not None:
            parameters["count"] = count

        self.__execute_get_request("audio.getPopular", on_success, parameters)
        pass

    def get_count(self, on_success, owner_id=None):
        parameters = dict()

        if owner_id is None:
            w = Wrapper()
            parameters["owner_id"] = w.get_current_user()
        else:
            parameters["owner_id"] = owner_id

        self.__execute_get_request("audio.getCount", on_success, parameters)
        pass
