from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from enum import Enum
import json
import os
from pydantic import BaseModel, validate_arguments
from typing import Any, Dict, List, Optional, Tuple, Type
import time
from uuid import uuid4

from impira import Impira as ImpiraAPI, FieldType, InferredFieldType, parse_date

from ..cmd.utils import environ_or_required
from ..schema import schema_to_model
from ..types import (
    BBox,
    combine_bboxes,
    Config as BaseConfig,
    DocData,
    DocSchema,
    NumberLabel,
    TextLabel,
    TimestampLabel,
)
from ..utils import batch
from .tool import Tool


class SchemaField(BaseModel):
    name: str
    path: List[str] = []
    field_type: InferredFieldType


def generate_schema(doc_schema: DocSchema) -> List[SchemaField]:
    fields = []
    for field_name, value in doc_schema.fields.items():
        if isinstance(value, DocSchema):
            fields.append(
                SchemaField(name=field_name, field_type=InferredFieldType.table)
            )
            for sub_field in generate_schema(value):
                sub_field.path.insert(0, field_name)
                fields.append(sub_field)
        elif value == "NumberLabel":
            fields.append(
                SchemaField(name=field_name, field_type=InferredFieldType.number)
            )
        elif value == "TextLabel":
            fields.append(
                SchemaField(name=field_name, field_type=InferredFieldType.text)
            )
        elif value == "TimestampLabel":
            fields.append(
                SchemaField(name=field_name, field_type=InferredFieldType.timestamp)
            )
        else:
            assert False, "Unknown field %s: %s" % (field_name, value)

    return fields


def is_overlapping(left1, width1, left2, width2):
    return left1 + width1 >= left2 and left2 + width2 >= left1


@validate_arguments
def is_bbox_overlapping(bbox1: BBox, bbox2: BBox):
    return (
        bbox1.page == bbox2.page
        and is_overlapping(
            bbox1.left,
            bbox1.width,
            bbox2.left,
            bbox2.width,
        )
        and is_overlapping(bbox1.top, bbox1.height, bbox2.top, bbox2.height)
    )


class ImpiraWord(BaseModel):
    confidence: float
    location: BBox
    processed_word: str
    rotated: bool
    source: str
    uid: str
    word: str


class ImpiraEntity(BaseModel):
    label: str
    location: BBox
    processed: Any
    source_rivlets: List[str]
    uid: str
    word: str


FirstClassEntityLabelToFieldType = {
    "NUMBER": InferredFieldType.number,
    "MONEY": InferredFieldType.number,
    "DATE": InferredFieldType.timestamp,
    "TIME": InferredFieldType.text,
}


class ScalarLabel(BaseModel):
    class L(BaseModel):
        Source: List[ImpiraWord]
        IsPrediction: bool = False
        Value: Optional[Any]

    class C(BaseModel):
        Entities: Optional[List[ImpiraEntity]]

    Label: L
    ModelVersion: int = 0  # TODO This might need to change for "future" labels
    Context: Optional[C]

    def is_prediction(self):
        return self.Label.IsPrediction


class RowLabel(BaseModel):
    class L(BaseModel):
        IsPrediction: bool
        Value: Dict[str, ScalarLabel]

    Label: L

    def is_prediction(self):
        return self.Label.IsPrediction


class TableLabel(BaseModel):
    class L(BaseModel):
        IsPrediction: bool
        Value: List[RowLabel]

    Label: L
    ModelVersion: int = 0  # TODO May be able to exclude

    def is_prediction(self):
        return self.Label.IsPrediction


class EntityMap(BaseModel):
    entities: List[ImpiraEntity]
    entityIndicesByRivletUid: Optional[Dict[str, List[int]]] = None

    # This is mirrored from Impira client code. We may want to move it into the Impira SDK.
    def find_entities(self, rivlets, match_subsets=False, match_supersets=False):
        m = self.ensureEntityIndicesByRivletUid()

        entity_index_counts = defaultdict(lambda: 0)
        for r in rivlets:
            x = m.get(r.uid, [])
            for i in x:
                entity_index_counts[i] += 1

        unique_entity_indices = set()
        for i, c in entity_index_counts.items():
            if (not match_subsets and c < len(rivlets)) or (
                not match_supersets
                and len(self.entities[i].source_rivlets) > len(rivlets)
            ):
                continue

            unique_entity_indices.add(i)

        return [self.entities[i] for i in sorted(unique_entity_indices)]

    def ensureEntityIndicesByRivletUid(self):
        if self.entityIndicesByRivletUid is None:
            m = defaultdict(lambda: [])
            for i, e in enumerate(self.entities):
                for r in e.source_rivlets:
                    m[r].append(i)
            self.entityIndicesByRivletUid = m

        return self.entityIndicesByRivletUid


@validate_arguments
def find_overlapping_words(value, words: List[ImpiraWord]):
    if value.location is None:
        return []

    return [
        word
        for word in words
        if is_bbox_overlapping(word.location, value.location)
        # and all([w in str(value.fmt()) for w in word.word.split()])
    ]


@validate_arguments
def generate_labels(
    record, words: List[ImpiraWord], entity_map: EntityMap
) -> Dict[str, Any]:
    labels = {}
    for field_name, value in dict(record).items():
        field_name = field_name.replace(
            ".", "_"
        )  # Remove after https://hendrix.impira.com/D11392 lands

        if isinstance(value, List):
            rows = [generate_labels(v, words, entity_map) for v in value]
            row_labels = [
                RowLabel(
                    Label=RowLabel.L(
                        Value=row,
                        IsPrediction=any([v.is_prediction() for v in row.values()]),
                    )
                )
                # TODO: For benchmarking, we'll want to reduce the number of labels we provide in a table
                for row in rows
            ]
            labels[field_name] = TableLabel(
                Label=TableLabel.L(
                    Value=row_labels,
                    IsPrediction=any([r.is_prediction() for r in row_labels]),
                )
            )
        elif value is not None:
            w = find_overlapping_words(value, words)
            labels[field_name] = ScalarLabel(
                Label=ScalarLabel.L(Source=w),
                Context=ScalarLabel.C(Entities=entity_map.find_entities(w)),
            )
    return labels


DATA_PROJECTION = "[uid, name: File.name, text: File.text, entities: File.ner.entities]"


def upload_and_retrieve_text(conn, collection_uid, f):
    uids = conn.upload_files(collection_uid, [f])
    assert len(uids) == 1
    for i in range(10):
        while True:
            resp = conn.query(
                "@`file_collections::%s`%s uid='%s' File.IsPreprocessed=true"
                % (collection_uid, DATA_PROJECTION, uids[0]),
                mode="poll",
                timeout=60,
            )

            for d in resp["data"] or []:
                if d["action"] != "insert":
                    continue

                return d["data"]


def find_path(root, *path):
    curr = root
    for p in path:
        curr = [x for x in curr["children"] if x["name"] == p][0]
    return curr


@validate_arguments
def fields_to_doc_schema(fields) -> DocSchema:
    ret = {}
    for f in fields:
        comment = json.loads(f["comment"])
        trainer = (
            InferredFieldType.match_trainer(comment["infer_func"]["trainer_name"])
            if "infer_func" in comment
            else None
        )
        t = None
        if trainer == InferredFieldType.table:
            sub_fields = find_path(f, "Label", "Value", "Label", "Value")["children"]
            t = fields_to_doc_schema(sub_fields)
        else:
            # TODO: To distinguish between more advanced types like checkboxes
            # and signatures, we should look at the trainer directly (not the
            # scalar type).
            scalar_type = find_path(f, "Label", "Value")["fieldType"]
            if scalar_type == FieldType.text:
                t = TextLabel.__name__
            elif scalar_type == FieldType.number:
                t = NumberLabel.__name__
            elif scalar_type == FieldType.timestamp:
                t = TimestampLabel.__name__
            else:
                assert False, "Unknown scalar type: %s" % (scalar_type)
        ret[f["name"]] = t
    return DocSchema(fields=ret)


@validate_arguments
def row_to_record(row, doc_schema: DocSchema) -> Any:
    d = {}
    for field_name, field_type in doc_schema.fields.items():
        value = row[field_name]
        if isinstance(field_type, DocSchema):
            table_rows = [
                row_label["Label"]["Value"] for row_label in value["Label"]["Value"]
            ]
            label = [
                x
                for x in [row_to_record(tr, field_type) for tr in table_rows]
                if x is not None
            ]
            if not label:
                continue
        else:
            impira_label = ScalarLabel.parse_obj(value)
            if impira_label.Label.IsPrediction:
                continue
            location = (
                combine_bboxes(*[x.location for x in impira_label.Label.Source])
                if len(impira_label.Label.Source) > 0
                else None
            )
            scalar = impira_label.Label.Value
            if scalar is not None and field_type == "TimestampLabel":
                scalar = parse_date(scalar)
            label = {"location": location, "value": scalar}
        d[field_name] = label

    if len(d) == 0:
        return None

    M = schema_to_model(doc_schema)
    return M(**d)


@validate_arguments
def row_to_fname(row) -> str:
    fname, ext = row["File"]["name"].rsplit(".", 1)
    return fname + "-" + row["uid"] + "." + ext


class Impira(Tool):
    class Config(BaseConfig):
        api_token: str
        org_name: str
        collection_prefix: str
        base_url: str
        collection: Optional[str]
        skip_upload: bool
        skip_type_inference: bool

    @staticmethod
    def add_arguments(parser):
        parser.add_argument("--api-token", **environ_or_required("IMPIRA_API_TOKEN"))
        parser.add_argument("--org-name", **environ_or_required("IMPIRA_ORG_NAME"))
        parser.add_argument(
            "--collection-prefix",
            **environ_or_required("IMPIRA_COLLECTION_PREFIX", "xbench")
        )
        parser.add_argument(
            "--base-url",
            **environ_or_required("IMPIRA_BASE_URL", "https://app.impira.com")
        )
        parser.add_argument(
            "--collection",
            default=None,
            type=str,
            help="uid of an existing collection",
        )
        parser.add_argument(
            "--skip-upload",
            default=False,
            action="store_true",
            help="Skip uploading files into the collection",
        )
        parser.add_argument(
            "--skip-type-inference",
            default=False,
            action="store_true",
            help="Do not use Impira's type inference to select field types",
        )

    @validate_arguments
    def __init__(self, config: Config):
        self.config = config

    def _conn(self):
        return ImpiraAPI(
            org_name=self.config.org_name,
            api_token=self.config.api_token,
            base_url=self.config.base_url,
        )

    @validate_arguments
    def run(self, doc_schema: DocSchema, entries: List[DocData]):
        log = self._log()

        schema = generate_schema(doc_schema)

        # Remove after https://hendrix.impira.com/D11392 lands
        if schema:
            for f in schema:
                f.name = f.name.replace(".", "_")

        conn = self._conn()

        if self.config.collection is None:
            assert (
                not self.config.skip_upload
            ), "Cannot skip uploading if we're creating a new collection."

            collection_name = "%s-%s" % (
                self.config.collection_prefix,
                uuid4(),
            )

            log.info("Creating collection %s" % (collection_name))
            collection_uid = conn.create_collection(collection_name)

        else:
            collection_uid = self.config.collection

        log.info(
            "You can visit the collection at: %s"
            % (conn.get_app_url("fc", collection_uid))
        )

        if not self.config.skip_upload:
            files = [
                {"path": e.url or str(e.fname), "name": e.fname.name} for e in entries
            ]

            log.info("Uploading %d files", len(files))
            with ThreadPoolExecutor(max_workers=self.config.parallelism) as t:
                file_data = [
                    x
                    for x in t.map(
                        lambda f: upload_and_retrieve_text(conn, collection_uid, f),
                        files,
                    )
                ]
        else:
            uids = {
                r["name"]: r
                for r in conn.query(
                    "@`file_collections::%s`%s" % (collection_uid, DATA_PROJECTION)
                )["data"]
            }
            file_data = [uids[e.fname.name] for e in entries]

        log.info("File uids: %s", [r["uid"] for r in file_data])

        # Now, just trim it down to the labeled entries
        labeled_entries = []
        labeled_files = []
        for i, e in enumerate(entries):
            if e.record is not None:
                labeled_entries.append(e)
                labeled_files.append(file_data[i])

        if len(labeled_entries) == 0:
            logging.warning(
                "No records have labels. Stopping now that uploads have completed."
            )
            return

        labels = []
        for e, fd in zip(labeled_entries, labeled_files):
            entity_map = EntityMap(entities=fd["entities"])
            labels.append(
                generate_labels(
                    e.record,
                    fd["text"]["words"],
                    entity_map,
                )
            )

        schema_resp = conn.query("@file_collections::%s limit:0" % (collection_uid))
        current_fields = set([f["name"] for f in schema_resp["schema"]["children"]])

        log.info("Creating fields")
        new_fields = []
        for f in schema:
            if f.name in current_fields or (
                len(f.path) > 0 and f.path[0] in current_fields
            ):
                continue

            new_fields.append(f)
            field_type = f.field_type

            first_labels = labels[0]
            if (
                f.name in first_labels
                and isinstance(first_labels[f.name], ScalarLabel)
                and not self.config.skip_type_inference
            ):
                entities = first_labels[f.name].Context.Entities
                unique_entity_types = set(
                    [field_type]
                    + [
                        FirstClassEntityLabelToFieldType[e.label]
                        for e in entities
                        if e.label in FirstClassEntityLabelToFieldType
                    ]
                )

                if InferredFieldType.timestamp in unique_entity_types:
                    field_type = InferredFieldType.timestamp
                elif InferredFieldType.number in unique_entity_types:
                    field_type = InferredFieldType.number

                log.debug(
                    "Creating field %s: type=%s, path=%s",
                    f.name,
                    field_type,
                    f.path,
                )

            conn.create_inferred_field(collection_uid, f.name, field_type, path=f.path)

        # Snapshot the model version and its cursor for new fields. Old fields are not going to change
        # their values (unless the labels have changed, which is not something we distinguish).
        mv_query = "@`file_collections::%s`[sum_mv: %s]" % (
            collection_uid,
            " + ".join(
                ["0"]
                + [
                    "COALESCE(min(`%s`.`ModelVersion`), -1)" % (f.name)
                    for f in new_fields
                    if len(f.path) == 0
                ]
            ),
        )
        increment = sum(
            [
                1 if f.field_type != InferredFieldType.table else 2
                for f in new_fields
                if len(f.path) == 0
            ]
        )

        # Unfortunately, polling doesn't work for "min" queries, so we just run a normal query
        log.info("Running model version query %s", mv_query)
        resp = conn.query(mv_query)["data"][0]
        log.info(
            "Current minimum model version %s. Target is %s",
            resp["sum_mv"],
            resp["sum_mv"] + increment,
        )

        target = resp["sum_mv"] + increment

        log.info("Running update on %d files" % len(labeled_files))
        conn.update(
            collection_uid,
            [
                {
                    **{"uid": fd["uid"]},
                    **{
                        field_path: label.dict(exclude_none=True)
                        for field_path, label in ld.items()
                    },
                }
                for (fd, ld) in zip(labeled_files, labels)
            ],
        )
        log.info(
            "Done running update on %d files. Now waiting for models to update!"
            % len(labeled_files)
        )

        while True:
            resp = conn.query(
                mv_query + " [sum_mv] sum_mv >= %d" % (target),
            )
            try:
                resp = resp["data"][0]
                break
            except Exception as e:
                time.sleep(1)
                continue

        log.debug(
            "Current minimum model version %s",
            resp["sum_mv"],
        )
        log.info("Done!")

    @validate_arguments
    def snapshot(self):
        assert self.config.collection is not None
        log = self._log()

        conn = self._conn()
        resp = conn.query("@file_collections::%s" % (self.config.collection))

        inferred_fields = [
            f
            for f in resp["schema"]["children"]
            if "comment" in f
            and json.loads(f["comment"])["field_template"] == "inferred_field_spec"
        ]

        doc_schema = fields_to_doc_schema(inferred_fields)
        records = [
            {
                "url": row["File"]["download_url"],
                "name": row_to_fname(row),
                "record": row_to_record(row, doc_schema),
            }
            for row in resp["data"]
        ]

        return doc_schema, records
