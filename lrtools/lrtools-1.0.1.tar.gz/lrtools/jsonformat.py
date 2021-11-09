from vector_2d import Vector as Vector2d
from .track import *
from .utils import *
import json

json_LineTypeMap = {
	0: LineType.Blue,
	1: LineType.Red,
	2: LineType.Scenery,
}

def get_key(dict: dict, value):
	return list(dict.keys())[list(dict.values()).index(value)]

def convert_ltype_to_trk(ltype: int) -> int:
	try:
		return json_LineTypeMap[ltype]
	except KeyError:
		raise ValueError(f"Invalid line type {ltype}")

def load_json(filename, name="track"):
	track = Track()
	track.Name = name
	with open(filename, encoding="utf-8") as f:
		data = json.load(f)
	track.ver = int(data["version"].replace(".", ""))
	track.StartOffset = Vector2d(data["startPosition"]["x"], data["startPosition"]["y"])
	for line in data["lines"]:
		extra = {}
		if "id" in line:
			extra["ID"] = line["id"]
		if "flipped" in line:
			extra["inv"] = line["flipped"]
		if "multiplier" in line:
			extra["Multiplier"] = line["multiplier"]
		# Extension: 0b01 - left   0b10 - right
		if "leftExtended" in line:
			extra["Extension"] = line["rightExtended"] * 2 + line["leftExtended"]
		track.addLine(
			Line(
				convert_ltype_to_trk(line["type"]),
				Vector2d(line["x1"], line["y1"]),
				Vector2d(line["x2"], line["y2"]),
				**extra
			)
		)
	return track

def save_json(trk: Track, savename: str):
	data = {
		"label": trk.Name,
		"duration": 0,
		"version": str(trk.ver / 10),
		"audio": None,
		"startPosition": {
			"x": 0,
			"y": 0
		},
		"riders": [
			{
				"startPosition": {
					"x": trk.StartOffset.x,
					"y": trk.StartOffset.y
				},
				"startVelocity": {
					"x": 0.4,
					"y": 0
				}
			}
		],
		"layers": [
			{
				"id": 0,
				"name": "Base Layer",
				"visible": True
			}
		],
		"lines": []
	}

	for line in trk.lines:
		line: Line
		l = {
			"id": 0,
			"type": get_key(json_LineTypeMap, line.type),
			"x1": line.point1.x,
			"y1": line.point1.y,
			"x2": line.point2.x,
			"y2": line.point2.y,
		}

		if line.type == LineType.Red:
			l["multiplier"] = line.Multiplier
		
		if line.type in (LineType.Blue, LineType.Red):
			l["id"] = line.ID
			l["flipped"] = line.inv
			l["leftExtended"] = bool(line.Extension & 0b01)
			l["rightExtended"] = bool(line.Extension & 0b10)

		data["lines"].append(l)

	with open(savename, "w") as f:
		json.dump(data, f)