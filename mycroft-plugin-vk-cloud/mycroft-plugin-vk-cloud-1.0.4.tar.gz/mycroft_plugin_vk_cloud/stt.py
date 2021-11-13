import json
from mycroft.stt import STT
from requests import post


class VkCloudSTTPlugin(STT):
    def __init__(self):
        super(VkCloudSTTPlugin, self).__init__()
        self.service_token = self.credential.get("service_token")
        if self.service_token is None:
            raise ValueError("Service token for VK Cloud STT is not defined")

    def execute(self, audio, language=None):
        language = language or self.lang
        if not language.startswith("ru"):
            raise ValueError("VK Cloud STT is currently Russian only")

        headers = {
            "Authorization": "Bearer {}".format(self.service_token),
            "Content-Type": "audio/wave"
        }

        url = "https://voice.mcs.mail.ru/asr"
        response = post(url, headers=headers, data=audio.get_wav_data())
        if response.status_code == 200:
            result = json.loads(response.text)
            if ("result" not in result or
                    "texts" not in result["result"] or
                    len(result["result"]["texts"]) < 1):
                raise Exception(
                    "Transcription failed. Invalid or empty result. "
                    "Body: {}".format(response.text))
            return result["result"]["texts"][0]["text"]
        elif response.status_code == 401:  # Unauthorized
            raise Exception("Invalid service token for VK STT")
        raise Exception(
            "Request to VK Cloud STT failed: code: {}, body: {}".format(
                response.status_code, response.text))
