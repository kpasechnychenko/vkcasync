from external.videolan.vlc import Instance, EventType
from domain.exceptions import PlayerException

class Uplayer:

    def __init__(self):
        self.__instance = Instance()
        self.__player = self.__instance.media_player_new()

        self.on_media_player_end_reached = []
        self.on_media_player_position_changed = []
        self.on_media_state_changed = []
        self.on_media_player_media_changed = []
        self.on_media_player_opening = []
        self.on_media_player_buffering = []
        self.on_media_player_playing = []
        self.on_media_player_paused = []
        self.on_media_player_stopped = []
        self.on_media_player_encountered_error = []
        self.on_media_player_time_changed = []

        self.__events_register()

    def __events_register(self):
        event_manager = self.__player.event_manager()
        event_manager.event_attach(EventType.MediaPlayerEndReached,      self.__media_player_end_reached)
        event_manager.event_attach(EventType.MediaPlayerPositionChanged, self.__media_player_position_changed)
        event_manager.event_attach(EventType.MediaStateChanged, self.__media_state_changed)
        event_manager.event_attach(EventType.MediaPlayerMediaChanged, self.__media_player_media_changed)
        event_manager.event_attach(EventType.MediaPlayerOpening, self.__media_player_opening)
        event_manager.event_attach(EventType.MediaPlayerBuffering, self.__media_player_buffering)
        event_manager.event_attach(EventType.MediaPlayerPlaying, self.__media_player_playing)
        event_manager.event_attach(EventType.MediaPlayerPaused, self.__media_player_paused)
        event_manager.event_attach(EventType.MediaPlayerStopped, self.__media_player_stopped)
        event_manager.event_attach(EventType.MediaPlayerEncounteredError, self.__media_player_encountered_error)
        event_manager.event_attach(EventType.MediaPlayerTimeChanged, self.__media_player_time_changed)
        pass

    def __media_state_changed(self):
        if self.on_media_state_changed is not None:
            for item in self.on_media_state_changed:
                # pass to callback required params
                item()
        pass

    def __media_player_time_changed(self):
        if self.on_media_player_time_changed is not None:
            for item in self.on_media_player_time_changed:
                # pass to callback required params
                item()
        pass

    def __media_player_encountered_error(self):
        if self.on_media_player_encountered_error is not None:
            for item in self.on_media_player_encountered_error:
                # pass to callback required params
                item()
        pass

    def __media_player_stopped(self):
        if self.on_media_player_stopped is not None:
            for item in self.on_media_player_stopped:
                # pass to callback required params
                item()
        pass

    def __media_player_paused(self):
        if self.on_media_player_paused is not None:
            for item in self.on_media_player_paused:
                # pass to callback required params
                item()
        pass

    def __media_player_playing(self):
        if self.on_media_player_playing is not None:
            for item in self.on_media_player_playing:
                # pass to callback required params
                item()
        pass

    def __media_player_buffering(self):
        if self.on_media_player_buffering is not None:
            for item in self.on_media_player_buffering:
                # pass to callback required params
                item()
        pass

    def __media_player_opening(self):
        if self.on_media_player_opening is not None:
            for item in self.on_media_player_opening:
                # pass to callback required params
                item()
        pass

    def __media_player_media_changed(self):
        if self.on_media_player_media_changed is not None:
            for item in self.on_media_player_media_changed:
                # pass to callback required params
                item()
        pass

    def __media_player_end_reached(self):
        if self.on_media_player_end_reached is not None:
            for item in self.on_media_player_end_reached:
                # pass to callback required params
                item()
        pass

    def __media_player_position_changed(self):
        if self.on_media_player_position_changed is not None:
            for item in self.on_media_player_position_changed:
                # pass to callback required params
                item()
        pass

    def open(self, file_name):
        try:
            media = self.__instance.media_new(file_name)
        except NameError:
            raise PlayerException("Wrong file name %s" % file_name)
        else:
            self.__player.set_media(media)
        pass

    def play(self):
        self.__player.play()
        pass

    def stop(self):
        self.__player.stop()

    def pause(self):
        self.__player.pause()

    def set_pause(self, do_pause):
        self.__player.set_pause(do_pause)

    def get_length(self):
        return self.__player.get_length()

    def get_time(self):
        return self.__player.get_time()

    def get_position(self):
        return self.__player.get_position()

    def get_state(self):
        return self.__player.get_state()

    def set_time(self, i_time):
        self.__player.set_time(self, i_time)

    def set_position(self, f_pos):
        self.__player.set_position(f_pos)

    def audio_toggle_mute(self):
        self.__player.audio_toggle_mute()

    def audio_get_mute(self):
        return self.__player.audio_get_mute()

    def audio_set_mute(self, status):
        self.__player.audio_set_mute(status)

    def audio_get_volume(self):
        return self.__player.audio_get_volume()

    def audio_set_volume(self, i_volume):
        self.__player.audio_set_volume(i_volume)



