from mycroft.configuration import Configuration
from mycroft.tts import TTS, TTSValidator
from requests import get

_API_URL = "https://voice.mcs.mail.ru/tts"


class VkCloudTTSPlugin(TTS):
    def __init__(self, lang, config):
        super(VkCloudTTSPlugin, self).__init__(lang, config,
                                               VkCloudTTSValidator(self), "mp3")
        config = Configuration.get().get("tts", {}).get("vk", {})
        self.service_token = config.get("service_token")
        self.tempo = config.get("tempo", 1.0)
        self.encoder = "mp3"

    def get_tts(self, sentence, wav_file):
        with open(wav_file, "wb") as f:
            for audio_content in self._synthesize(sentence):
                f.write(audio_content)
        return wav_file, None

    def _synthesize(self, text):
        headers = {"Authorization": "Bearer {}".format(self.service_token)}

        params = {
            "text": text,
            "tempo": self.tempo,
            "encoder": self.encoder
        }

        with get(_API_URL, params=params, headers=headers,
                 stream=True) as resp:
            if resp.status_code != 200:
                raise Exception(
                    "Request to VK TTS failed: code: {}, body: {}".format(
                        resp.status_code, resp.text))

            for chunk in resp.iter_content(chunk_size=None):
                yield chunk


class VkCloudTTSValidator(TTSValidator):
    def __init__(self, tts):
        super(VkCloudTTSValidator, self).__init__(tts)

    def validate_lang(self):
        pass

    def validate_connection(self):
        config = Configuration.get().get("tts", {}).get("vk", {})
        service_token = config.get("service_token")
        if service_token is not None:
            headers = {"Authorization": "Bearer {}".format(service_token)}
            r = get(_API_URL, headers=headers)
            if r.status_code == 400:  # Authorized, but bad request
                return True
            elif r.status_code == 401:  # Unauthorized
                raise Exception("Invalid service token for VK TTS")
            else:
                raise Exception(
                    "Unexpected HTTP code from VK Cloud TTS ({})".format(
                        r.status_code))
        else:
            raise ValueError(
                "Service token for VK Cloud TTS is not defined")

    def get_tts_class(self):
        return VkCloudTTSPlugin
