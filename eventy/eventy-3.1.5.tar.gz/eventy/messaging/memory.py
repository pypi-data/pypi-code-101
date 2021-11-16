from typing import Iterable, Optional, Union

from eventy.messaging.errors import MessagingError
from eventy.messaging.store import RecordStore, Cursor
from eventy.record import Record

__all__ = [
    'MemoryStore',
]


class _ReadTopic:
    def __init__(
        self,
        topic: str,
    ) -> None:
        self.topic = topic
        self.records: list[Record] = []
        self.read_offset = 0
        self.acked_offset = 0

    def add(
        self,
        records: Union[Record, Iterable[Record]],
    ) -> None:
        if not isinstance(records, Iterable):
            records = [records]
        self.records.extend(records)

    def read(
        self,
        max_count: int = 1,
    ) -> list[Record]:
        read_records = self.records[self.read_offset:self.read_offset + max_count]
        self.read_offset += len(read_records)
        return read_records

    def ack(self, count: int = None) -> None:
        if count is None:
            self.acked_offset = self.read_offset
        else:
            if (self.acked_offset + count) > self.read_offset:
                raise MessagingError('Cannot ack more than read.')
            self.acked_offset += count

    def reset(self):
        self.read_offset = self.acked_offset

    def clear(self) -> None:
        self.records = []
        self.read_offset = 0
        self.acked_offset = 0


class _WriteTopic:
    def __init__(
        self,
        topic: str,
    ) -> None:
        self.topic = topic
        self.records: list[Record] = []
        self.committed_offset = 0

    def write_committed(
        self,
        record: Record,
    ) -> None:
        self.records.insert(self.committed_offset, record)
        self.committed_offset += 1

    def write_uncommitted(
        self,
        record: Record,
    ) -> None:
        self.records.append(record)

    def commit(self, count: int = None) -> None:
        if count is None:
            self.committed_offset = len(self.records)
        else:
            if (self.committed_offset + count) > len(self.records):
                raise MessagingError("Cannot commit more than written.")
            self.committed_offset += count

    def reset(self) -> None:
        self.records = self.records[:self.committed_offset]

    def clear(self) -> None:
        self.records = []
        self.committed_offset = 0


class _Transaction:
    def __init__(self):
        self.reads: dict[str, int] = {}
        self.writes: dict[str, int] = {}

    def add_read(self, topic: str, count: int = 1) -> None:
        if topic not in self.reads:
            self.reads[topic] = 0
        self.reads[topic] += count

    def add_write(self, topic: str, count: int = 1) -> None:
        if topic not in self.writes:
            self.writes[topic] = 0
        self.writes[topic] += count


class MemoryStore(RecordStore):
    """
    In-memory record store, essentially for testing and debug purposes
    """

    def __init__(self) -> None:
        """
        Initialize an empty store
        """
        super().__init__()

        self.read_topics: dict[str, _ReadTopic] = {}
        self.write_topics: dict[str, _WriteTopic] = {}
        self.transaction: Optional[_Transaction] = None

    def register_topic(self, topic: str, cursor: Cursor = Cursor.ACKNOWLEDGED) -> None:
        if cursor != Cursor.ACKNOWLEDGED:
            raise MessagingError(f"Only ACKNOWLEDGED cursors are supported.")
        self.read_topics[topic] = _ReadTopic(topic)

    def read(
        self,
        max_count: int = 1,
        timeout_ms: Optional[int] = None,
        auto_ack: bool = False
    ) -> list[Record]:
        if auto_ack:
            raise MessagingError(f"Auto-ack is not supported.")
        records: list[Record] = []
        for topic, topic_read in self.read_topics.items():
            reads = topic_read.read(max_count - len(records))
            records.extend(reads)
        return records

    def ack(self, timeout_ms=None) -> None:
        for topic, topic_read in self.read_topics.items():
            if self.transaction:
                self.transaction.add_read(topic, topic_read.read_offset - topic_read.acked_offset)
            else:
                topic_read.ack()

    def write(self, record: Record, topic: str, timeout_ms=None) -> None:
        if topic not in self.write_topics:
            self.write_topics[topic] = _WriteTopic(topic)
        write_topic = self.write_topics[topic]
        if self.transaction:
            self.transaction.add_write(topic)
            write_topic.write_uncommitted(record)
        else:
            write_topic.write_committed(record)

    def write_now(self, record: Record, topic: str, timeout_ms=None) -> None:
        if topic not in self.write_topics:
            self.write_topics[topic] = _WriteTopic(topic)
        write_topic = self.write_topics[topic]
        write_topic.write_committed(record)

    def start_transaction(self) -> None:
        if self.transaction:
            raise MessagingError(f"Already in a transaction.")
        self.transaction = _Transaction()

    def commit(self, timeout_ms: Optional[int] = None) -> None:
        if not self.transaction:
            raise MessagingError(f"Not in a transaction.")
        for topic, read_count in self.transaction.reads.items():
            self.read_topics[topic].ack(read_count)
        for topic, write_count in self.transaction.writes.items():
            self.write_topics[topic].commit(write_count)
        self.transaction = None

    def abort(self, timeout_ms: Optional[int] = None) -> None:
        if not self.transaction:
            raise MessagingError(f"Not in a transaction.")
        for topic, read_count in self.transaction.reads.items():
            self.read_topics[topic].reset()
        for topic, write_count in self.transaction.writes.items():
            self.write_topics[topic].reset()
        self.transaction = None

    def add_record(self, records: Union[Record, Iterable[Record]], topic: str) -> None:
        """
        Add one or multiple records to be read.

        :param records: record(s) to be added
        :param topic: topic the record(s) should be added to
        """
        if topic not in self.read_topics:
            raise MessagingError(f"Topic {topic} not registered.")
        self.read_topics[topic].add(records)

    def get_committed_records(self, topic: str = None) -> list[Record]:
        """
        Get records written and committed to the store.

        :param topic: Optionally specify a topic to get records for
        :return: List of Records
        """
        if topic:
            topics = [topic]
        else:
            topics = list(self.write_topics.keys())
        records: list[Record] = []
        for topic in topics:
            if topic in self.write_topics:
                records.extend(self.write_topics[topic].records[:self.write_topics[topic].committed_offset])
        return records

    def get_acked_records(self, topic: str = None) -> list[Record]:
        """
        Get records written and acked to the store.

        :param topic: Optionally specify a topic to get records for
        :return: List of Records
        """
        if topic:
            topics = [topic]
        else:
            topics = list(self.read_topics.keys())
        records: list[Record] = []
        for topic in topics:
            if topic in self.read_topics:
                records.extend(self.read_topics[topic].records[:self.read_topics[topic].acked_offset])
        return records

    def clear(self) -> None:
        """
        Completely clear the store (remove all data).
        """
        for write_topic in self.write_topics.values():
            write_topic.clear()
        for read_topic in self.read_topics.values():
            read_topic.clear()
        self.transaction = None

    def reset(self) -> None:
        """
        Reset the store to the last committed state.
        """
        for write_topic in self.write_topics.values():
            write_topic.reset()
        for read_topic in self.read_topics.values():
            read_topic.reset()
        self.transaction = None
