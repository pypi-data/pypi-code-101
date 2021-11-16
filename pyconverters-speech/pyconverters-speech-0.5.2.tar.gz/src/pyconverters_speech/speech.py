import os
from enum import Enum
from functools import lru_cache
from typing import Type, List, cast

from pymultirole_plugins.v1.formatter import FormatterParameters
from starlette.datastructures import UploadFile
from pydantic import BaseModel, Field
from pymultirole_plugins.v1.converter import ConverterParameters, ConverterBase
from pymultirole_plugins.v1.schema import Document
from transformers import AutomaticSpeechRecognitionPipeline, pipeline, AutoTokenizer
from transformers.pipelines.automatic_speech_recognition import ffmpeg_read

_home = os.path.expanduser('~')
xdg_cache_home = os.environ.get('XDG_CACHE_HOME') or os.path.join(_home, '.cache')


class TrfModel(str, Enum):
    wav2vec2_base_960h = "facebook/wav2vec2-base-960h"


class SpeechParameters(ConverterParameters):
    model: TrfModel = Field(TrfModel.wav2vec2_base_960h,
                            description="""Which [Transformers model](
                            https://huggingface.co/models?pipeline_tag=automatic-speech-recognition) fine-tuned
                            for Speech Recognition to use, can be one of:<br/>
                            <li>`facebook/wav2vec2-base-960h`: The base model pretrained and fine-tuned on 960 hours of Librispeech on 16kHz sampled speech audio.""")


class SpeechConverter(ConverterBase):
    """Speech converter .
    """

    def convert(self, source: UploadFile, parameters: ConverterParameters) \
            -> List[Document]:
        params: SpeechParameters = \
            cast(SpeechParameters, parameters)

        # Create cached pipeline context with model
        p: AutomaticSpeechRecognitionPipeline = get_pipeline(params.model)
        inputs = source.file.read()
        result = p(inputs)
        doc = Document(identifier=source.filename, text=result['text'])
        doc.properties = {"fileName": source.filename, "encoding": "utf-8"}
        return [doc]

    @classmethod
    def get_model(cls) -> Type[BaseModel]:
        return SpeechParameters

@lru_cache(maxsize=None)
def get_pipeline(model):
    p = pipeline("automatic-speech-recognition", model=model.value, tokenizer=AutoTokenizer.from_pretrained(model.value))
    return p
