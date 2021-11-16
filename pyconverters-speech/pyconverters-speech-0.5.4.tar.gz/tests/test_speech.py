from pathlib import Path
from typing import List
from starlette.datastructures import UploadFile
from pyconverters_speech.speech import SpeechConverter, SpeechParameters
from pymultirole_plugins.v1.schema import Document


def test_speech():
    model = SpeechConverter.get_model()
    model_class = model.construct().__class__
    assert model_class == SpeechParameters
    converter = SpeechConverter()
    parameters = SpeechParameters()
    testdir = Path(__file__).parent
    source = Path(testdir, 'data/2.wav')
    with source.open("rb") as fin:
        docs: List[Document] = converter.convert(UploadFile(source.name, fin, 'audio/wav'), parameters)
        assert len(docs) == 1
        doc0 = docs[0]
        assert doc0.text.startswith('on bed seven')
