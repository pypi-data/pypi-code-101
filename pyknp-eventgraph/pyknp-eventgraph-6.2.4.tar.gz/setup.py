# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyknp_eventgraph']

package_data = \
{'': ['*']}

install_requires = \
['graphviz>=0.16,<1.0.0', 'pyknp>=0.5.0,<1.0.0']

entry_points = \
{'console_scripts': ['evg = pyknp_eventgraph.cli:evg',
                     'evgviz = pyknp_eventgraph.cli:evgviz']}

setup_kwargs = {
    'name': 'pyknp-eventgraph',
    'version': '6.2.4',
    'description': 'A development platform for high-level NLP applications in Japanese',
    'long_description': "# pyknp-eventgraph\n\n**EventGraph** is a development platform for high-level NLP applications in Japanese.\nThe core concept of EventGraph is event, a language information unit that is closely related to predicate-argument structure but more application-oriented.\nEvents are linked to each other based on their syntactic and semantic relations.\n\n## Requirements\n\n- Python 3.6 or later\n- pyknp\n- graphviz\n\n## Installation\n\nTo install pyknp-eventgraph, use `pip`.\n\n```\n$ pip install pyknp-eventgraph\n```\n\n## Quick Tour\n\n### Step 1: Create an EventGraph\n\nAn EventGraph is built on language analysis given in a KNP format.\n\n```python\n# Add imports.\nfrom pyknp import KNP\nfrom pyknp_eventgraph import EventGraph\n\n# Parse a document.\ndocument = ['彼女は海外勤務が長いので、英語がうまいに違いない。', '私はそう確信していた。']\nknp = KNP()\nanalysis = [knp.parse(sentence) for sentence in document]\n\n# Create an EventGraph.\nevg = EventGraph.build(analysis)\nprint(evg)  # <EventGraph, #sentences: 2, #events: 3, #relations: 1>\n```\n\n### Step 2: Extract Information\n\nUsers can obtain various information about language analysis via a simple interface.\n\n#### Step 2.1: Sentence\n\n```python\n# Extract sentences.\nsentences = evg.sentences\nprint(sentences)\n# [\n#   <Sentence, sid: 1, ssid: 0, surf: 彼女は海外勤務が長いので、英語がうまいに違いない。>,\n#   <Sentence, sid: 2, ssid: 1, surf: 私はそう確信していた。>\n# ]\n\n# Convert a sentence into various forms.\nsentence = evg.sentences[0]\nprint(sentence.surf)   # 彼女は海外勤務が長いので、英語がうまいに違いない。\nprint(sentence.mrphs)  # 彼女 は 海外 勤務 が 長い ので 、 英語 が うまい に 違いない 。\nprint(sentence.reps)   # 彼女/かのじょ は/は 海外/かいがい 勤務/きんむ が/が 長い/ながい ので/ので 、/、 英語/えいご が/が 上手い/うまい に/に 違い無い/ちがいない 。/。\n```\n\n#### Step 2.2: Event\n\n```python\n# Extract events.\nevents = evg.events\nprint(events)\n# [\n#   <Event, evid: 0, surf: 海外勤務が長いので、>,\n#   <Event, evid: 1, surf: 彼女は英語がうまいに違いない。>,\n#   <Event, evid: 2, surf: 私はそう確信していた。>\n# ]\n\n# Convert an event into various forms.\nevent = evg.events[0]\nprint(event.surf)              # 海外勤務が長いので、\nprint(event.mrphs)             # 海外 勤務 が 長い ので 、\nprint(event.normalized_mrphs)  # 海外 勤務 が 長い\nprint(event.reps)              # 海外/かいがい 勤務/きんむ が/が 長い/ながい ので/ので 、/、\nprint(event.normalized_reps)   # 海外/かいがい 勤務/きんむ が/が 長い/ながい\nprint(event.content_rep_list)  # ['海外/かいがい', '勤務/きんむ', '長い/ながい']\n\n# Extract an event's PAS.\npas = event.pas\nprint(pas)            # <PAS, predicate: 長い/ながい, arguments: {ガ: 勤務/きんむ}>\nprint(pas.predicate)  # <Predicate, type: 形, surf: 長い>\nprint(pas.arguments)  # defaultdict(<class 'list'>, {'ガ': [<Argument, case: ガ, surf: 勤務が>]})\n\n# Extract an event's features.\nfeatures = event.features\nprint(features)  # <Features, modality: None, tense: 非過去, negation: False, state: 状態述語, complement: False>\n```\n\n#### Step 2.3: Event-to-event Relation\n\n```python\n# Extract event-to-event relations.\nrelations = evg.relations\nprint(relations)  # [<Relation, label: 原因・理由, modifier_evid: 0, head_evid: 1>]\n\n# Take a closer look at an event-to-event relation\nrelation = relations[0]\nprint(relation.label)     # 原因・理由\nprint(relation.surf)      # ので\nprint(relation.modifier)  # <Event, evid: 0, surf: 海外勤務が長いので、>\nprint(relation.head)      # <Event, evid: 1, surf: 彼女は英語がうまいに違いない。>\n```\n\n### Step 3: Seve/Load an EventGraph\n\nUsers can save and load an EventGraph by serializing it as a JSON object.\n\n```python\n# Save an EventGraph as a JSON file.\nevg.save('evg.json')\n\n# Load an EventGraph from a JSON file.\nwith open('evg.json') as f:\n    evg = EventGraph.load(f)\n```\n\n### Step 4: Visualize an EventGraph\n\nUsers can visualize an EventGraph using [graphviz](https://graphviz.org/).\n\n```python\nfrom pyknp_eventgraph import make_image\nmake_image(evg, 'evg.svg')  # Currently, only supports 'svg'.\n```\n\n## Advanced Usage\n\n### Merging modifiers\n\nBy merging a modifier event to the modifiee, users can construct a larger information unit.\n\n```python\nfrom pyknp import KNP\nfrom pyknp_eventgraph import EventGraph\n\ndocument = ['もっととろみが持続する作り方をして欲しい。']\nknp = KNP()\nanalysis = [knp.parse(sentence) for sentence in document]\n\nevg = EventGraph.build(analysis)\nprint(evg)  # <EventGraph, #sentences: 1, #events: 2, #relations: 1>\n\n# Investigate the relation.\nrelation = evg.relations[0]\nprint(relation)           # <Relation, label: 連体修飾, modifier_evid: 0, head_evid: 1>\nprint(relation.modifier)  # <Event, evid: 0, surf: もっととろみが持続する>\nprint(relation.head)      # <Event, evid: 1, surf: 作り方をして欲しい。>\n\n# To merge modifier events, enable `include_modifiers`.\nprint(relation.head.surf)                           # 作り方をして欲しい。\nprint(relation.head.surf_(include_modifiers=True))  # もっととろみが持続する作り方をして欲しい。\n\n# Other formats also support `include_modifiers`.\nprint(relation.head.mrphs_(include_modifiers=True))  # もっと とろみ が 持続 する 作り 方 を して 欲しい 。\nprint(relation.head.normalized_mrphs_(include_modifiers=True))  # もっと とろみ が 持続 する 作り 方 を して 欲しい\n```\n\n### Binary serialization\n\nWhen an EventGraph is serialized in a JSON format, it will lose some functionality, including access to KNP objects and modifier merging.\nTo keep full functionality, use Python's pickle utility for serialization.\n\n```python\n# Save an EventGraph using Python's pickle utility.\nevg.save('evg.pkl', binary=True)\n\n# Load an EventGraph using Python's pickle utility.\nwith open('evg.pkl', 'rb') as f:\n    evg_ = EventGraph.load(f, binary=True)\n```\n\n## CLI\n\n### EventGraph Construction\n\n```\n$ echo '彼女は海外勤務が長いので、英語がうまいに違いない。' | jumanpp | knp -tab | evg -o example-eventgraph.json\n```\n\n### EventGraph Visualization\n\n```\n$ evgviz example-eventgraph.json example-eventgraph.svg\n```\n\n## Documents\n\n[https://pyknp-eventgraph.readthedocs.io/en/latest/](https://pyknp-eventgraph.readthedocs.io/en/latest/)\n\n## Authors\n\n- Kurohashi-Kawahara Lab, Kyoto University.\n- contact@nlp.ist.i.kyoto-u.ac.jp\n",
    'author': 'Hirokazu Kiyomaru',
    'author_email': 'h.kiyomaru@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ku-nlp/pyknp-eventgraph',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
