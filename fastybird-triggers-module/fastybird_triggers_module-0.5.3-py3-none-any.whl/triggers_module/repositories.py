#!/usr/bin/python3

#     Copyright 2021. FastyBird s.r.o.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

# pylint: disable=too-many-lines

"""
Triggers module repositories
"""

# Library dependencies
import json
import uuid
from typing import List, Dict, Optional, Union
from exchange_plugin.dispatcher import EventDispatcher
from exchange_plugin.events.event import IEvent
from kink import inject
import modules_metadata.exceptions as metadata_exceptions
from modules_metadata.loader import load_schema
from modules_metadata.routing import RoutingKey
from modules_metadata.validator import validate
from modules_metadata.triggers_module import TriggerConditionOperator
from modules_metadata.types import ModuleOrigin
from pony.orm import core as orm

# Library libs
from triggers_module.events import ModelEntityCreatedEvent, ModelEntityUpdatedEvent, ModelEntityDeletedEvent
from triggers_module.exceptions import HandleExchangeDataException
from triggers_module.models import (
    TriggerEntity,
    AutomaticTriggerEntity,
    ManualTriggerEntity,
    TriggerControlEntity,
    ActionEntity,
    DevicePropertyActionEntity,
    ChannelPropertyActionEntity,
    ConditionEntity,
    DevicePropertyConditionEntity,
    ChannelPropertyConditionEntity,
    TimeConditionEntity,
    DateConditionEntity,
)
from triggers_module.items import (
    AutomaticTriggerItem,
    ManualTriggerItem,
    TriggerControlItem,
    DevicePropertyConditionItem,
    ChannelPropertyConditionItem,
    TimeConditionItem,
    DateConditionItem,
    DevicePropertyActionItem,
    ChannelPropertyActionItem,
)


@inject
class TriggersRepository:
    """
    Triggers repository

    @package        FastyBird:TriggersModule!
    @module         repositories

    @author         Adam Kadlec <adam.kadlec@fastybird.com>
    """
    __items: Optional[Dict[str, Union[AutomaticTriggerItem, ManualTriggerItem]]] = None

    __iterator_index = 0

    __event_dispatcher: EventDispatcher

    # -----------------------------------------------------------------------------

    def __init__(
        self,
        event_dispatcher: EventDispatcher,
    ) -> None:
        self.__event_dispatcher = event_dispatcher

        self.__event_dispatcher.add_listener(
            event_id=ModelEntityCreatedEvent.EVENT_NAME,
            listener=self.__entity_created,
        )

        self.__event_dispatcher.add_listener(
            event_id=ModelEntityUpdatedEvent.EVENT_NAME,
            listener=self.__entity_updated,
        )

        self.__event_dispatcher.add_listener(
            event_id=ModelEntityDeletedEvent.EVENT_NAME,
            listener=self.__entity_deleted,
        )

    # -----------------------------------------------------------------------------

    def get_by_id(self, trigger_id: uuid.UUID) -> Union[AutomaticTriggerItem, ManualTriggerItem, None]:
        """Find trigger in cache by provided identifier"""
        if self.__items is None:
            self.initialize()

        if trigger_id.__str__() in self.__items:
            return self.__items[trigger_id.__str__()]

        return None

    # -----------------------------------------------------------------------------

    def clear(self) -> None:
        """Clear items cache"""
        self.__items = None

    # -----------------------------------------------------------------------------

    @orm.db_session
    def create_from_exchange(self, routing_key: RoutingKey, data: Dict) -> bool:
        """Process received trigger message from exchange when entity was created"""
        if routing_key != RoutingKey.TRIGGERS_ENTITY_CREATED:
            return False

        if self.__items is None:
            self.initialize()

            return True

        data: Dict = validate_exchange_data(ModuleOrigin(ModuleOrigin.TRIGGERS_MODULE), routing_key, data)

        entity: Optional[TriggerEntity] = TriggerEntity.get(trigger_id=uuid.UUID(data.get("id"), version=4))

        if entity is not None:
            self.__items[entity.trigger_id.__str__()] = self.__create_item(entity)

            return True

        return False

    # -----------------------------------------------------------------------------

    @orm.db_session
    def update_from_exchange(self, routing_key: RoutingKey, data: Dict) -> bool:
        """Process received trigger message from exchange when entity was updated"""
        if routing_key != RoutingKey.TRIGGERS_ENTITY_UPDATED:
            return False

        if self.__items is None:
            self.initialize()

            return True

        validated_data: Dict = validate_exchange_data(ModuleOrigin(ModuleOrigin.TRIGGERS_MODULE), routing_key, data)

        if validated_data.get("id") not in self.__items:
            entity: Optional[TriggerEntity] = TriggerEntity.get(
                trigger_id=uuid.UUID(validated_data.get("id"), version=4),
            )

            if entity is not None:
                self.__items[entity.trigger_id.__str__()] = self.__create_item(entity)

                return True

            return False

        item = self.__update_item(
            self.get_by_id(uuid.UUID(validated_data.get("id"), version=4)),
            validated_data,
        )

        if item is not None:
            self.__items[validated_data.get("id")] = item

            return True

        return False

    # -----------------------------------------------------------------------------

    @orm.db_session
    def delete_from_exchange(self, routing_key: RoutingKey, data: Dict) -> bool:
        """Process received trigger message from exchange when entity was updated"""
        if routing_key != RoutingKey.TRIGGERS_ENTITY_DELETED:
            return False

        if data.get("id") in self.__items:
            del self.__items[data.get("id")]

            return True

        return False

    # -----------------------------------------------------------------------------

    @orm.db_session
    def initialize(self) -> None:
        """Initialize repository by fetching entities from database"""
        items: Dict[str, Union[AutomaticTriggerItem, ManualTriggerItem]] = {}

        for trigger in TriggerEntity.select():
            if self.__items is None or trigger.trigger_id.__str__() not in self.__items:
                item = self.__create_item(trigger)

            else:
                item = self.__update_item(self.get_by_id(trigger.trigger_id), trigger.to_dict())

            if item is not None:
                items[trigger.trigger_id.__str__()] = item

        self.__items = items

    # -----------------------------------------------------------------------------

    def __entity_created(self, event: IEvent) -> None:
        if (
            not isinstance(event, ModelEntityCreatedEvent)
            or not isinstance(event.entity, (ManualTriggerEntity, AutomaticTriggerEntity))
        ):
            return

        self.initialize()

    # -----------------------------------------------------------------------------

    def __entity_updated(self, event: IEvent) -> None:
        if (
            not isinstance(event, ModelEntityUpdatedEvent)
            or not isinstance(event.entity, (ManualTriggerEntity, AutomaticTriggerEntity))
        ):
            return

        self.initialize()

    # -----------------------------------------------------------------------------

    def __entity_deleted(self, event: IEvent) -> None:
        if (
            not isinstance(event, ModelEntityDeletedEvent)
            or not isinstance(event.entity, (ManualTriggerEntity, AutomaticTriggerEntity))
        ):
            return

        self.initialize()

    # -----------------------------------------------------------------------------

    @staticmethod
    def __create_item(entity: TriggerEntity) -> Union[AutomaticTriggerItem, ManualTriggerItem, None]:
        if isinstance(entity, AutomaticTriggerEntity):
            return AutomaticTriggerItem(
                trigger_id=entity.trigger_id,
                name=entity.name,
                comment=entity.comment,
                enabled=entity.enabled,
            )

        if isinstance(entity, ManualTriggerEntity):
            return ManualTriggerItem(
                trigger_id=entity.trigger_id,
                name=entity.name,
                comment=entity.comment,
                enabled=entity.enabled,
            )

        return None

    # -----------------------------------------------------------------------------

    @staticmethod
    def __update_item(
        item: Union[AutomaticTriggerItem, ManualTriggerItem],
        data: Dict,
    ) -> Union[AutomaticTriggerItem, ManualTriggerItem, None]:
        if isinstance(item, AutomaticTriggerItem):
            return AutomaticTriggerItem(
                trigger_id=item.trigger_id,
                name=data.get("name", item.name),
                comment=data.get("comment", item.comment),
                enabled=bool(data.get("enabled", item.enabled)),
            )

        if isinstance(item, ManualTriggerItem):
            return ManualTriggerItem(
                trigger_id=item.trigger_id,
                name=data.get("name", item.name),
                comment=data.get("comment", item.comment),
                enabled=bool(data.get("enabled", item.enabled)),
            )

        return None

    # -----------------------------------------------------------------------------

    def __iter__(self) -> "TriggersRepository":
        # Reset index for nex iteration
        self.__iterator_index = 0

        return self

    # -----------------------------------------------------------------------------

    def __len__(self):
        if self.__items is None:
            self.initialize()

        return len(self.__items.values())

    # -----------------------------------------------------------------------------

    def __next__(self) -> Union[AutomaticTriggerItem, ManualTriggerItem]:
        if self.__items is None:
            self.initialize()

        if self.__iterator_index < len(self.__items.values()):
            items: List[Union[AutomaticTriggerItem, ManualTriggerItem]] = list(self.__items.values())

            result: Union[AutomaticTriggerItem, ManualTriggerItem] = items[self.__iterator_index]

            self.__iterator_index += 1

            return result

        # Reset index for nex iteration
        self.__iterator_index = 0

        # End of iteration
        raise StopIteration


@inject
class ActionsRepository:
    """
    Triggers actions repository

    @package        FastyBird:TriggersModule!
    @module         repositories

    @author         Adam Kadlec <adam.kadlec@fastybird.com>
    """
    __items: Optional[Dict[str, Union[DevicePropertyActionItem, ChannelPropertyActionItem]]] = None

    __iterator_index = 0

    __event_dispatcher: EventDispatcher

    # -----------------------------------------------------------------------------

    def __init__(
        self,
        event_dispatcher: EventDispatcher,
    ) -> None:
        self.__event_dispatcher = event_dispatcher

        self.__event_dispatcher.add_listener(
            event_id=ModelEntityCreatedEvent.EVENT_NAME,
            listener=self.__entity_created,
        )

        self.__event_dispatcher.add_listener(
            event_id=ModelEntityUpdatedEvent.EVENT_NAME,
            listener=self.__entity_updated,
        )

        self.__event_dispatcher.add_listener(
            event_id=ModelEntityDeletedEvent.EVENT_NAME,
            listener=self.__entity_deleted,
        )

    # -----------------------------------------------------------------------------

    def get_by_id(self, action_id: uuid.UUID) -> Union[DevicePropertyActionItem, ChannelPropertyActionItem, None]:
        """Find action in cache by provided identifier"""
        if self.__items is None:
            self.initialize()

        if action_id.__str__() in self.__items:
            return self.__items[action_id.__str__()]

        return None

    # -----------------------------------------------------------------------------

    def get_by_property_identifier(
            self,
            property_id: uuid.UUID,
    ) -> Union[DevicePropertyActionItem, ChannelPropertyActionItem, None]:
        """Find action in cache by provided property identifier"""
        if self.__items is None:
            self.initialize()

        for action in self.__items.values():
            if isinstance(action, DevicePropertyActionItem) and action.device_property.__eq__(property_id):
                return action

            if isinstance(action, ChannelPropertyActionItem) and action.channel_property.__eq__(property_id):
                return action

        return None

    # -----------------------------------------------------------------------------

    def get_all_by_property_identifier(
            self,
            property_id: uuid.UUID,
    ) -> List[Union[DevicePropertyActionItem, ChannelPropertyActionItem]]:
        """Find actions in cache by provided property identifier"""
        if self.__items is None:
            self.initialize()

        actions: List[Union[DevicePropertyActionItem, ChannelPropertyActionItem]] = []

        for action in self.__items.values():
            if isinstance(action, DevicePropertyActionItem) and action.device_property.__eq__(property_id):
                actions.append(action)

            if isinstance(action, ChannelPropertyActionItem) and action.channel_property.__eq__(property_id):
                actions.append(action)

        return actions

    # -----------------------------------------------------------------------------

    def get_all_for_trigger(
        self,
        trigger_id: uuid.UUID,
    ) -> List[Union[DevicePropertyActionItem, ChannelPropertyActionItem]]:
        """Find all actions in cache for provided trigger identifier"""
        if self.__items is None:
            self.initialize()

        actions: List[Union[DevicePropertyActionItem, ChannelPropertyActionItem]] = []

        for action in self.__items.values():
            if action.trigger_id.__eq__(trigger_id):
                actions.append(action)

        return actions

    # -----------------------------------------------------------------------------

    def clear(self) -> None:
        """Clear items cache"""
        self.__items = None

    # -----------------------------------------------------------------------------

    @orm.db_session
    def create_from_exchange(self, routing_key: RoutingKey, data: Dict) -> bool:
        """Process received action message from exchange when entity was created"""
        if routing_key != RoutingKey.TRIGGERS_ACTIONS_ENTITY_CREATED:
            return False

        if self.__items is None:
            self.initialize()

            return True

        data: Dict = validate_exchange_data(ModuleOrigin(ModuleOrigin.TRIGGERS_MODULE), routing_key, data)

        entity: Optional[ActionEntity] = ActionEntity.get(action_id=uuid.UUID(data.get("id"), version=4))

        if entity is not None:
            self.__items[entity.action_id.__str__()] = self.__create_item(entity)

            return True

        return False

    # -----------------------------------------------------------------------------

    @orm.db_session
    def update_from_exchange(self, routing_key: RoutingKey, data: Dict) -> bool:
        """Process received action message from exchange when entity was updated"""
        if routing_key != RoutingKey.TRIGGERS_ACTIONS_ENTITY_UPDATED:
            return False

        if self.__items is None:
            self.initialize()

            return True

        validated_data: Dict = validate_exchange_data(ModuleOrigin(ModuleOrigin.TRIGGERS_MODULE), routing_key, data)

        if validated_data.get("id") not in self.__items:
            entity: Optional[ActionEntity] = ActionEntity.get(action_id=uuid.UUID(validated_data.get("id"), version=4))

            if entity is not None:
                self.__items[entity.action_id.__str__()] = self.__create_item(entity)

                return True

            return False

        item = self.__update_item(
            self.get_by_id(uuid.UUID(validated_data.get("id"), version=4)),
            validated_data,
        )

        if item is not None:
            self.__items[validated_data.get("id")] = item

            return True

        return False

    # -----------------------------------------------------------------------------

    @orm.db_session
    def delete_from_exchange(self, routing_key: RoutingKey, data: Dict) -> bool:
        """Process received action message from exchange when entity was updated"""
        if routing_key != RoutingKey.TRIGGERS_ACTIONS_ENTITY_DELETED:
            return False

        if data.get("id") in self.__items:
            del self.__items[data.get("id")]

            return True

        return False

    # -----------------------------------------------------------------------------

    @orm.db_session
    def initialize(self) -> None:
        """Initialize repository by fetching entities from database"""
        items: Dict[str, Union[DevicePropertyActionItem, ChannelPropertyActionItem]] = {}

        for action in ActionEntity.select():
            if self.__items is None or action.action_id.__str__() not in self.__items:
                item = self.__create_item(action)

            else:
                item = self.__update_item(self.get_by_id(action.action_id), action.to_dict())

            if item is not None:
                items[action.action_id.__str__()] = item

        self.__items = items

    # -----------------------------------------------------------------------------

    def __entity_created(self, event: IEvent) -> None:
        if (
            not isinstance(event, ModelEntityCreatedEvent)
            or not isinstance(event.entity, (DevicePropertyActionEntity, ChannelPropertyActionEntity))
        ):
            return

        self.initialize()

    # -----------------------------------------------------------------------------

    def __entity_updated(self, event: IEvent) -> None:
        if (
            not isinstance(event, ModelEntityUpdatedEvent)
            or not isinstance(event.entity, (DevicePropertyActionEntity, ChannelPropertyActionEntity))
        ):
            return

        self.initialize()

    # -----------------------------------------------------------------------------

    def __entity_deleted(self, event: IEvent) -> None:
        if (
            not isinstance(event, ModelEntityDeletedEvent)
            or not isinstance(event.entity, (DevicePropertyActionEntity, ChannelPropertyActionEntity))
        ):
            return

        self.initialize()

    # -----------------------------------------------------------------------------

    @staticmethod
    def __create_item(entity: ActionEntity) -> Union[DevicePropertyActionItem, ChannelPropertyActionItem, None]:
        if isinstance(entity, DevicePropertyActionEntity):
            return DevicePropertyActionItem(
                action_id=entity.action_id,
                trigger_id=entity.trigger.trigger_id,
                enabled=entity.enabled,
                value=entity.value,
                device_property=entity.device_property,
                device=entity.device,
            )

        if isinstance(entity, ChannelPropertyActionEntity):
            return ChannelPropertyActionItem(
                action_id=entity.action_id,
                trigger_id=entity.trigger.trigger_id,
                enabled=entity.enabled,
                value=entity.value,
                channel_property=entity.channel_property,
                channel=entity.channel,
                device=entity.device,
            )

        return None

    # -----------------------------------------------------------------------------

    @staticmethod
    def __update_item(
        item: Union[DevicePropertyActionItem, ChannelPropertyActionItem],
        data: Dict,
    ) -> Union[DevicePropertyActionItem, ChannelPropertyActionItem, None]:
        if isinstance(item, DevicePropertyActionItem):
            return DevicePropertyActionItem(
                action_id=item.action_id,
                trigger_id=item.trigger_id,
                enabled=data.get("enabled", item.enabled),
                value=data.get("value", item.value),
                device_property=item.device_property,
                device=item.device,
            )

        if isinstance(item, ChannelPropertyActionItem):
            return ChannelPropertyActionItem(
                action_id=item.action_id,
                trigger_id=item.trigger_id,
                enabled=data.get("enabled", item.enabled),
                value=data.get("value", item.value),
                channel_property=item.channel_property,
                channel=item.channel,
                device=item.device,
            )

        return None

    # -----------------------------------------------------------------------------

    def __iter__(self) -> "ActionsRepository":
        # Reset index for nex iteration
        self.__iterator_index = 0

        return self

    # -----------------------------------------------------------------------------

    def __len__(self):
        if self.__items is None:
            self.initialize()

        return len(self.__items.values())

    # -----------------------------------------------------------------------------

    def __next__(self) -> Union[DevicePropertyActionItem, ChannelPropertyActionItem]:
        if self.__items is None:
            self.initialize()

        if self.__iterator_index < len(self.__items.values()):
            items: List[Union[DevicePropertyActionItem, ChannelPropertyActionItem]] = list(self.__items.values())

            result: Union[DevicePropertyActionItem, ChannelPropertyActionItem] = items[self.__iterator_index]

            self.__iterator_index += 1

            return result

        # Reset index for nex iteration
        self.__iterator_index = 0

        # End of iteration
        raise StopIteration


@inject
class ConditionsRepository:
    """
    Triggers conditions repository

    @package        FastyBird:TriggersModule!
    @module         repositories

    @author         Adam Kadlec <adam.kadlec@fastybird.com>
    """
    __items: Optional[
        Dict[
            str,
            Union[DevicePropertyConditionItem, ChannelPropertyConditionItem, TimeConditionItem, DateConditionItem]
        ]
    ] = None

    __iterator_index = 0

    __event_dispatcher: EventDispatcher

    # -----------------------------------------------------------------------------

    def __init__(
        self,
        event_dispatcher: EventDispatcher,
    ) -> None:
        self.__event_dispatcher = event_dispatcher

        self.__event_dispatcher.add_listener(
            event_id=ModelEntityCreatedEvent.EVENT_NAME,
            listener=self.__entity_created,
        )

        self.__event_dispatcher.add_listener(
            event_id=ModelEntityUpdatedEvent.EVENT_NAME,
            listener=self.__entity_updated,
        )

        self.__event_dispatcher.add_listener(
            event_id=ModelEntityDeletedEvent.EVENT_NAME,
            listener=self.__entity_deleted,
        )

    # -----------------------------------------------------------------------------

    def get_by_id(
        self,
        condition_id: uuid.UUID,
    ) -> Union[DevicePropertyConditionItem, ChannelPropertyConditionItem, TimeConditionItem, DateConditionItem, None]:
        """Find condition in cache by provided identifier"""
        if self.__items is None:
            self.initialize()

        if condition_id.__str__() in self.__items:
            return self.__items[condition_id.__str__()]

        return None

    # -----------------------------------------------------------------------------

    def get_by_property_identifier(
        self,
        property_id: uuid.UUID,
    ) -> Union[DevicePropertyConditionItem, ChannelPropertyConditionItem, TimeConditionItem, DateConditionItem, None]:
        """Find condition in cache by provided property identifier"""
        if self.__items is None:
            self.initialize()

        for condition in self.__items.values():
            if isinstance(condition, DevicePropertyConditionItem) and condition.device_property.__eq__(property_id):
                return condition

            if isinstance(condition, ChannelPropertyConditionItem) and condition.channel_property.__eq__(property_id):
                return condition

        return None

    # -----------------------------------------------------------------------------

    def get_all_by_property_identifier(
        self,
        property_id: uuid.UUID,
    ) -> List[Union[DevicePropertyConditionItem, ChannelPropertyConditionItem, TimeConditionItem, DateConditionItem]]:
        """Find conditions in cache by provided property identifier"""
        if self.__items is None:
            self.initialize()

        conditions: List[Union[DevicePropertyConditionItem, ChannelPropertyConditionItem]] = []

        for condition in self.__items.values():
            if isinstance(condition, DevicePropertyConditionItem) and condition.device_property.__eq__(property_id):
                conditions.append(condition)

            if isinstance(condition, ChannelPropertyConditionItem) and condition.channel_property.__eq__(property_id):
                conditions.append(condition)

        return conditions

    # -----------------------------------------------------------------------------

    def get_all_for_trigger(
            self,
            trigger_id: uuid.UUID,
    ) -> List[Union[DevicePropertyConditionItem, ChannelPropertyConditionItem, TimeConditionItem, DateConditionItem]]:
        """Find all conditions in cache for provided trigger identifier"""
        if self.__items is None:
            self.initialize()

        conditions: List[
            Union[DevicePropertyConditionItem, ChannelPropertyConditionItem, TimeConditionItem, DateConditionItem]
        ] = []

        for condition in self.__items.values():
            if condition.trigger_id.__eq__(trigger_id):
                conditions.append(condition)

        return conditions

    # -----------------------------------------------------------------------------

    def clear(self) -> None:
        """Clear items cache"""
        self.__items = None

    # -----------------------------------------------------------------------------

    @orm.db_session
    def create_from_exchange(self, routing_key: RoutingKey, data: Dict) -> bool:
        """Process received condition message from exchange when entity was created"""
        if routing_key != RoutingKey.TRIGGERS_CONDITIONS_ENTITY_CREATED:
            return False

        if self.__items is None:
            self.initialize()

            return True

        data: Dict = validate_exchange_data(ModuleOrigin(ModuleOrigin.TRIGGERS_MODULE), routing_key, data)

        entity: Optional[ConditionEntity] = ConditionEntity.get(condition_id=uuid.UUID(data.get("id"), version=4))

        if entity is not None:
            self.__items[entity.condition_id.__str__()] = self.__create_item(entity)

            return True

        return False

    # -----------------------------------------------------------------------------

    @orm.db_session
    def update_from_exchange(self, routing_key: RoutingKey, data: Dict) -> bool:
        """Process received condition message from exchange when entity was updated"""
        if routing_key != RoutingKey.TRIGGERS_CONDITIONS_ENTITY_UPDATED:
            return False

        if self.__items is None:
            self.initialize()

            return True

        validated_data: Dict = validate_exchange_data(ModuleOrigin(ModuleOrigin.TRIGGERS_MODULE), routing_key, data)

        if validated_data.get("id") not in self.__items:
            entity: Optional[ConditionEntity] = ConditionEntity.get(
                condition_id=uuid.UUID(validated_data.get("id"), version=4)
            )

            if entity is not None:
                self.__items[entity.condition_id.__str__()] = self.__create_item(entity)

                return True

            return False

        item = self.__update_item(
            self.get_by_id(uuid.UUID(validated_data.get("id"), version=4)),
            validated_data,
        )

        if item is not None:
            self.__items[validated_data.get("id")] = item

            return True

        return False

    # -----------------------------------------------------------------------------

    @orm.db_session
    def delete_from_exchange(self, routing_key: RoutingKey, data: Dict) -> bool:
        """Process received condition message from exchange when entity was updated"""
        if routing_key != RoutingKey.TRIGGERS_CONDITIONS_ENTITY_DELETED:
            return False

        if data.get("id") in self.__items:
            del self.__items[data.get("id")]

            return True

        return False

    # -----------------------------------------------------------------------------

    @orm.db_session
    def initialize(self) -> None:
        """Initialize conditions repository by fetching entities from database"""
        items: Dict[
            str,
            Union[DevicePropertyConditionItem, ChannelPropertyConditionItem, TimeConditionItem, DateConditionItem],
        ] = {}

        for condition in ConditionEntity.select():
            if self.__items is None or condition.condition_id.__str__() not in self.__items:
                item = self.__create_item(condition)

            else:
                item = self.__update_item(self.get_by_id(condition.condition_id), condition.to_dict())

            if item is not None:
                items[condition.condition_id.__str__()] = item

        self.__items = items

    # -----------------------------------------------------------------------------

    def __entity_created(self, event: IEvent) -> None:
        if (
            not isinstance(event, ModelEntityCreatedEvent)
            or not isinstance(event.entity, (
                DevicePropertyConditionEntity,
                ChannelPropertyConditionEntity,
                DateConditionEntity,
                TimeConditionEntity,
            ))
        ):
            return

        self.initialize()

    # -----------------------------------------------------------------------------

    def __entity_updated(self, event: IEvent) -> None:
        if (
            not isinstance(event, ModelEntityUpdatedEvent)
            or not isinstance(event.entity, (
                DevicePropertyConditionEntity,
                ChannelPropertyConditionEntity,
                DateConditionEntity,
                TimeConditionEntity,
            ))
        ):
            return

        self.initialize()

    # -----------------------------------------------------------------------------

    def __entity_deleted(self, event: IEvent) -> None:
        if (
            not isinstance(event, ModelEntityDeletedEvent)
            or not isinstance(event.entity, (
                DevicePropertyConditionEntity,
                ChannelPropertyConditionEntity,
                DateConditionEntity,
                TimeConditionEntity,
            ))
        ):
            return

        self.initialize()

    # -----------------------------------------------------------------------------

    @staticmethod
    def __create_item(
        entity: ConditionEntity,
    ) -> Union[DevicePropertyConditionItem, ChannelPropertyConditionItem, TimeConditionItem, DateConditionItem, None]:
        if isinstance(entity, DevicePropertyConditionEntity):
            return DevicePropertyConditionItem(
                condition_id=entity.condition_id,
                trigger_id=entity.trigger.trigger_id,
                enabled=entity.enabled,
                operator=entity.operator_formatted,
                operand=entity.operand,
                device_property=entity.device_property,
                device=entity.device,
            )

        if isinstance(entity, ChannelPropertyConditionEntity):
            return ChannelPropertyConditionItem(
                condition_id=entity.condition_id,
                trigger_id=entity.trigger.trigger_id,
                enabled=entity.enabled,
                operator=entity.operator_formatted,
                operand=entity.operand,
                channel_property=entity.channel_property,
                channel=entity.channel,
                device=entity.device,
            )

        if isinstance(entity, TimeConditionEntity):
            return TimeConditionItem(
                condition_id=entity.condition_id,
                trigger_id=entity.trigger.trigger_id,
                enabled=entity.enabled,
                time=entity.time,
                days=entity.days,
            )

        if isinstance(entity, DateConditionEntity):
            return DateConditionItem(
                condition_id=entity.condition_id,
                trigger_id=entity.trigger.trigger_id,
                enabled=entity.enabled,
                date=entity.date,
            )

        return None

    # -----------------------------------------------------------------------------

    @staticmethod
    def __update_item(
        item: Union[DevicePropertyConditionItem, ChannelPropertyConditionItem, TimeConditionItem, DateConditionItem],
        data: Dict,
    ) -> Union[DevicePropertyConditionItem, ChannelPropertyConditionItem, TimeConditionItem, DateConditionItem, None]:
        if isinstance(item, DevicePropertyConditionItem):
            return DevicePropertyConditionItem(
                condition_id=item.condition_id,
                trigger_id=item.trigger_id,
                enabled=data.get("enabled", item.enabled),
                operator=TriggerConditionOperator(data.get("operator", item.operator.value)),
                operand=data.get("operand", item.operand),
                device_property=item.device_property,
                device=item.device,
            )

        if isinstance(item, ChannelPropertyConditionItem):
            return ChannelPropertyConditionItem(
                condition_id=item.condition_id,
                trigger_id=item.trigger_id,
                enabled=data.get("enabled", item.enabled),
                operator=TriggerConditionOperator(data.get("operator", item.operator.value)),
                operand=data.get("operand", item.operand),
                channel_property=item.channel_property,
                channel=item.channel,
                device=item.device,
            )

        if isinstance(item, TimeConditionItem):
            return TimeConditionItem(
                condition_id=item.condition_id,
                trigger_id=item.trigger_id,
                enabled=data.get("enabled", item.enabled),
                time=data.get("time", item.time),
                days=data.get("days", item.days),
            )

        if isinstance(item, DateConditionItem):
            return DateConditionItem(
                condition_id=item.condition_id,
                trigger_id=item.trigger_id,
                enabled=data.get("enabled", item.enabled),
                date=data.get("time", item.date),
            )

        return None

    # -----------------------------------------------------------------------------

    def __iter__(self) -> "ConditionsRepository":
        # Reset index for nex iteration
        self.__iterator_index = 0

        return self

    # -----------------------------------------------------------------------------

    def __len__(self):
        if self.__items is None:
            self.initialize()

        return len(self.__items.values())

    # -----------------------------------------------------------------------------

    def __next__(
        self,
    ) -> Union[DevicePropertyConditionItem, ChannelPropertyConditionItem, TimeConditionItem, DateConditionItem]:
        if self.__items is None:
            self.initialize()

        if self.__iterator_index < len(self.__items.values()):
            items: List[
                Union[
                    DevicePropertyConditionItem,
                    ChannelPropertyConditionItem,
                    TimeConditionItem,
                    DateConditionItem,
                ]
            ] = list(self.__items.values())

            result: Union[
                DevicePropertyConditionItem,
                ChannelPropertyConditionItem,
                TimeConditionItem,
                DateConditionItem,
            ] = items[self.__iterator_index]

            self.__iterator_index += 1

            return result

        # Reset index for nex iteration
        self.__iterator_index = 0

        # End of iteration
        raise StopIteration


@inject
class TriggersControlsRepository:
    """
    Triggers controls repository

    @package        FastyBird:DevicesModule!
    @module         repositories

    @author         Adam Kadlec <adam.kadlec@fastybird.com>
    """
    _items: Optional[Dict[str, TriggerControlItem]] = None

    __iterator_index = 0

    __event_dispatcher: EventDispatcher

    # -----------------------------------------------------------------------------

    def __init__(
        self,
        event_dispatcher: EventDispatcher,
    ) -> None:
        self.__event_dispatcher = event_dispatcher

        self.__event_dispatcher.add_listener(
            event_id=ModelEntityCreatedEvent.EVENT_NAME,
            listener=self.__entity_created,
        )

        self.__event_dispatcher.add_listener(
            event_id=ModelEntityUpdatedEvent.EVENT_NAME,
            listener=self.__entity_updated,
        )

        self.__event_dispatcher.add_listener(
            event_id=ModelEntityDeletedEvent.EVENT_NAME,
            listener=self.__entity_deleted,
        )

    # -----------------------------------------------------------------------------

    def get_by_id(
        self,
        control_id: uuid.UUID,
    ) -> Optional[TriggerControlItem]:
        """Find control in cache by provided identifier"""
        if self._items is None:
            self.initialize()

        if control_id.__str__() in self._items:
            return self._items[control_id.__str__()]

        return None

    # -----------------------------------------------------------------------------

    def clear(self) -> None:
        """Clear items cache"""
        self._items = None

    # -----------------------------------------------------------------------------

    @orm.db_session
    def create_from_exchange(self, routing_key: RoutingKey, data: Dict) -> bool:
        """Process received device control message from exchange when entity was created"""
        if routing_key != RoutingKey.TRIGGERS_CONTROL_ENTITY_CREATED:
            return False

        if self._items is None:
            self.initialize()

            return True

        data: Dict = validate_exchange_data(ModuleOrigin(ModuleOrigin.TRIGGERS_MODULE), routing_key, data)

        entity: Optional[TriggerControlEntity] = TriggerControlEntity.get(
            control_id=uuid.UUID(data.get("id"), version=4),
        )

        if entity is not None:
            self._items[entity.control_id.__str__()] = self._create_item(entity)

            return True

        return False

    # -----------------------------------------------------------------------------

    @orm.db_session
    def update_from_exchange(self, routing_key: RoutingKey, data: Dict) -> bool:
        """Process received device control message from exchange when entity was updated"""
        if routing_key != RoutingKey.TRIGGERS_CONTROL_ENTITY_UPDATED:
            return False

        if self._items is None:
            self.initialize()

            return True

        validated_data: Dict = validate_exchange_data(ModuleOrigin(ModuleOrigin.TRIGGERS_MODULE), routing_key, data)

        if validated_data.get("id") not in self._items:
            entity: Optional[TriggerControlEntity] = TriggerControlEntity.get(
                control_id=uuid.UUID(validated_data.get("id"), version=4)
            )

            if entity is not None:
                self._items[entity.control_id.__str__()] = self._create_item(entity)

                return True

            return False

        item = self._update_item(self.get_by_id(uuid.UUID(validated_data.get("id"), version=4)))

        if item is not None:
            self._items[validated_data.get("id")] = item

            return True

        return False

    # -----------------------------------------------------------------------------

    @orm.db_session
    def delete_from_exchange(self, routing_key: RoutingKey, data: Dict) -> bool:
        """Process received device control message from exchange when entity was updated"""
        if routing_key != RoutingKey.TRIGGERS_CONTROL_ENTITY_DELETED:
            return False

        if data.get("id") in self._items:
            del self._items[data.get("id")]

            return True

        return False

    # -----------------------------------------------------------------------------

    @orm.db_session
    def initialize(self) -> None:
        """Initialize triggers controls repository by fetching entities from database"""
        items: Dict[str, TriggerControlItem] = {}

        for entity in TriggerControlEntity.select():
            if self._items is None or entity.control_id.__str__() not in self._items:
                item = self._create_item(entity)

            else:
                item = self._update_item(self.get_by_id(entity.control_id))

            if item is not None:
                items[entity.control_id.__str__()] = item

        self._items = items

    # -----------------------------------------------------------------------------

    def __entity_created(self, event: IEvent) -> None:
        if not isinstance(event, ModelEntityCreatedEvent) or not isinstance(event.entity, TriggerControlEntity):
            return

        self.initialize()

    # -----------------------------------------------------------------------------

    def __entity_updated(self, event: IEvent) -> None:
        if not isinstance(event, ModelEntityUpdatedEvent) or not isinstance(event.entity, TriggerControlEntity):
            return

        self.initialize()

    # -----------------------------------------------------------------------------

    def __entity_deleted(self, event: IEvent) -> None:
        if not isinstance(event, ModelEntityDeletedEvent) or not isinstance(event.entity, TriggerControlEntity):
            return

        self.initialize()

    # -----------------------------------------------------------------------------

    @staticmethod
    def _create_item(entity: TriggerControlEntity) -> Optional[TriggerControlItem]:
        if isinstance(entity, TriggerControlEntity):
            return TriggerControlItem(
                control_id=entity.control_id,
                control_name=entity.name,
                trigger_id=entity.trigger.trigger_id,
            )

        return None

    # -----------------------------------------------------------------------------

    @staticmethod
    def _update_item(item: TriggerControlItem) -> Optional[TriggerControlItem]:
        if isinstance(item, TriggerControlItem):
            return TriggerControlItem(
                control_id=item.control_id,
                control_name=item.name,
                trigger_id=item.trigger_id,
            )

        return None

    # -----------------------------------------------------------------------------

    def __iter__(self) -> "TriggersControlsRepository":
        # Reset index for nex iteration
        self.__iterator_index = 0

        return self

    # -----------------------------------------------------------------------------

    def __len__(self):
        if self._items is None:
            self.initialize()

        return len(self._items.values())

    # -----------------------------------------------------------------------------

    def __next__(self) -> TriggerControlItem:
        if self._items is None:
            self.initialize()

        if self.__iterator_index < len(self._items.values()):
            items: List[TriggerControlItem] = list(self._items.values())

            result: TriggerControlItem = items[self.__iterator_index]

            self.__iterator_index += 1

            return result

        # Reset index for nex iteration
        self.__iterator_index = 0

        # End of iteration
        raise StopIteration


def validate_exchange_data(origin: ModuleOrigin, routing_key: RoutingKey, data: Dict) -> Dict:
    """
    Validate received RPC message against defined schema
    """
    try:
        schema: str = load_schema(origin, routing_key)

    except metadata_exceptions.FileNotFoundException as ex:
        raise HandleExchangeDataException("Provided data could not be validated") from ex

    except metadata_exceptions.InvalidArgumentException as ex:
        raise HandleExchangeDataException("Provided data could not be validated") from ex

    try:
        return validate(json.dumps(data), schema)

    except metadata_exceptions.MalformedInputException as ex:
        raise HandleExchangeDataException("Provided data are not in valid json format") from ex

    except metadata_exceptions.LogicException as ex:
        raise HandleExchangeDataException("Provided data could not be validated") from ex

    except metadata_exceptions.InvalidDataException as ex:
        raise HandleExchangeDataException("Provided data are not valid") from ex
