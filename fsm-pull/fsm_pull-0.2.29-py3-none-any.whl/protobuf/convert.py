import json

import pydash as py_
from tqdm import tqdm

from fsm_pull.protobuf.records_pb2 import (
    Call,
    Intent,
    Prediction,
    Range,
    Turn,
    Utterance,
)

turn_type_map = {"UNKNOWN": 0, "ACTION": 1, "INPUT": 2, "RESPONSE": 3, "VALIDATION": 4}


def call_dict2proto(call_dict):
    turns = call_dict.get("turns", {})
    conversations = turns.get("conversations", [])
    turns = [turn_dict2proto({**turns, **turn}) for turn in conversations]
    return Call(
        id=call_dict.get("uuid"),
        created_at=call_dict.get("created_at"),
        virtual_number=call_dict.get("virtual_number"),
        audio_url=call_dict.get("audio_url"),
        duration=call_dict.get("duration"),
        turns=turns,
    )


def turn_dict2proto(conversation_dict):
    utterances = utterance_dict2proto(
        conversation_dict.get("debug_metadata", {})
        .get("plute_request", {})
        .get("alternatives")
    )
    prediction = conversation_dict.get("prediction")
    if prediction:
        prediction = json.loads(prediction)
    prediction = prediction_dict2proto(prediction)
    return Turn(
        id=conversation_dict["uuid"],
        created_at=conversation_dict["created_at"],
        type=turn_type_map.get(conversation_dict.get("type"), 0),
        sub_type=conversation_dict.get("sub_type"),
        text=conversation_dict.get("text"),
        utterances=utterances,
        audio_url=conversation_dict.get("audio_url"),
        state=conversation_dict.get("state"),
        asr_context=conversation_dict.get("asr_context"),
        asr_provider=conversation_dict.get("asr_provider"),
        language=conversation_dict.get("language"),
        prediction=prediction,
    )


def utterance_dict2proto(utterances_dict):
    if not isinstance(utterances_dict, list):
        return None
    elif not utterances_dict:
        return None
    elif isinstance(utterances_dict, list) and isinstance(utterances_dict[0], dict):
        utterances_dict = [utterances_dict]
    elif isinstance(utterances_dict, list) and not isinstance(utterances_dict[0], list):
        raise TypeError(
            f"Expected {utterances_dict=} to be List[List[Dict[str, Any]]]."
        )

    utterances = []
    for utterance in utterances_dict:
        alternatives = []
        for alternative in utterance:
            _alternative = Utterance.Alternative(transcript=alternative["transcript"])
            if "confidence" in alternative:
                _alternative.confidence = alternative["confidence"]
            elif "am_score" in alternative and "lm_score" in alternative:
                _alternative.am_score = alternative["am_score"]
                _alternative.lm_score = alternative["lm_score"]
            alternatives.append(_alternative)
        utterances.append(Utterance(alternatives=alternatives))
    return utterances


def prediction_dict2proto(prediction_dict):
    if not prediction_dict:
        return Prediction()
    # handle plute style predictions
    if "graph" in prediction_dict:
        intents = prediction_dict["graph"]["output"][0]
    # or dialogy style predictions
    else:
        intents = prediction_dict["intents"]
    intents_ = []
    for intent in intents:
        slots = []
        for slot in intent["slots"]:
            values = []
            value_holder = {}
            if isinstance(slot["type"], str):
                slot_types = [slot["type"]]
            elif isinstance(slot["type"], list):
                slot_types = slot["type"]
            else:
                slot_types = None
            if slot_types:
                for value in slot.get("values", []):
                    value_ = value.get("value")
                    if isinstance(value_, str):
                        value_holder["string_value"] = value_
                    elif isinstance(value_, int):
                        value_holder["int_value"] = value_
                    elif isinstance(value_, float):
                        value_holder["float_value"] = value_
                    values.append(
                        Intent.Slot.Value(
                            body=value.get("body"),
                            type=value.get("type"),
                            alternative_id=value.get("alternative_id"),
                            range=Range(
                                start=value.get("range", {}).get("start"),
                                end=value.get("range", {}).get("end"),
                            ),
                            **value_holder,
                        )
                    )
            else:
                values = None
            slot_ = Intent.Slot(name=slot["name"], type=slot_types, values=values)
            try:
                slots.append(slot_)
            except ValueError:
                print(slot)
        intents_.append(Intent(name=intent["name"], score=intent["score"], slots=slots))
    return Prediction(intents=intents_)


def make_utterances(maybe_utterances):
    if not maybe_utterances:
        return None
    if isinstance(maybe_utterances, list) and isinstance(maybe_utterances[0], dict):
        return json.dumps([maybe_utterances])
    if isinstance(maybe_utterances, list) and isinstance(maybe_utterances[0], list):
        return json.dumps(maybe_utterances)


def is_plute_style(prediction):
    if isinstance(prediction, str):
        try:
            prediction = json.loads(prediction)
        except json.JSONDecodeError:
            return False
    return "graph" in prediction


def prediction_from_plute(prediction):
    intent = None
    if "intents" in prediction:
        intent = prediction.get("intents")[0]
    elif "name" in prediction and ("slot" in prediction or "slots" in prediction):
        intent = prediction

    if not intent:
        return [], None

    slot_key = "slot" if "slot" in intent else "slots"
    prediction = {
        "name": intent.get("name"),
        "score": intent.get("score"),
        "slots": [],
    }
    entities_from_all_slots = []

    for slot in intent.get(slot_key, []):
        value_key = "value" if "value" in slot else "values"
        entities = [
            {
                "text": entity.get("body") or entity.get("text"),
                "type": entity.get("type") or "transcription",
                "value": entity.get("value"),
                "score": entity.get("score", 0),
            }
            for entity in slot.get(value_key, [])
        ]

        prediction["slots"].append(
            {"name": slot.get("name"), "type": slot.get("type"), "value": entities}
        )

        entities_from_all_slots.append(entities)

    return py_.flatten(entities_from_all_slots), prediction


def prediction_from_dialogy(prediction):
    intent = None
    if "intents" in prediction:
        intent = prediction.get("intents")[0]
    elif "name" in prediction and ("slot" in prediction or "slots" in prediction):
        intent = prediction

    if not intent:
        return [], None

    slot_key = "slot" if "slot" in intent else "slots"
    prediction = {"name": intent.get("name"), "score": intent.get("score"), "slots": []}
    entities_from_all_slots = []

    for slot in intent.get(slot_key, []):
        value_key = "value" if "value" in slot else "values"
        entities = [
            {
                "text": entity.get("body") or entity.get("text"),
                "type": entity.get("type") or "transcription",
                "value": entity.get("value"),
                "score": entity.get("score", 0),
            }
            for entity in slot.get(value_key, [])
        ]

        prediction["slots"].append(
            {"name": slot.get("name"), "type": slot.get("type"), "values": entities}
        )

        entities_from_all_slots.append(entities)

    return py_.flatten(entities_from_all_slots), prediction


def get_prediction(prediction):
    if isinstance(prediction, str):
        prediction = json.loads(prediction)
    if not isinstance(prediction, dict):
        return [], None
    if is_plute_style(prediction):
        return prediction_from_plute(prediction)
    else:
        return prediction_from_dialogy(prediction)


def build_turns_dataframe(calls_dict):
    """
    Builds a dataframe from a list of Call objects.
    """
    calls = []
    flat_turns = []
    for call_dict in tqdm(calls_dict):
        turns = []
        turn = call_dict.get("turns", {})
        for conversation in tqdm(turn.get("conversations", [])):
            if (
                conversation.get("type") == "INPUT"
                and conversation.get("sub_type") == "AUDIO"
            ):
                entities, prediction = get_prediction(conversation.get("prediction"))
            else:
                entities = []
                prediction = None
            turn_ = {
                "id": conversation.get("uuid"),
                "created_at": turn.get("created_at"),
                "type": conversation.get("type"),
                "sub_type": conversation.get("sub_type"),
                "text": conversation.get("text"),
                "utterances": make_utterances(
                    conversation.get("debug_metadata", {})
                    .get("plute_request", {})
                    .get("alternatives")
                ),
                "audio_url": conversation.get("audio_url"),
                "state": conversation.get("state"),
                "asr_context": conversation.get("asr_context"),
                "asr_provider": conversation.get("asr_provider"),
                "language": turn.get("language_code"),
                "prediction": prediction
                if isinstance(prediction, str)
                else json.dumps(prediction, ensure_ascii=False),
                "predicted_entities": entities
                if isinstance(entities, str)
                else json.dumps(entities, ensure_ascii=False),
            }
            flat_turns.append(turn_)
            turns.append(turn_)
        call = {
            "id": call_dict.get("uuid"),
            "created_at": call_dict.get("created_at"),
            "virtual_number": call_dict.get("virtual_number"),
            "audio_url": call_dict.get("call_audio"),
            "duration": call_dict.get("total_call_duration"),
            "flow_version": call_dict.get("flow_version"),
            "turns": turns,
        }
        calls.append(call)
    return calls, flat_turns
