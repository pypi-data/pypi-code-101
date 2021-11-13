import asyncio
import typing

from nion.instrumentation import camera_base
from nion.ui import Declarative
from nion.ui import Dialog
from nion.ui import Window
from nion.swift.model import PlugInManager
from nion.utils import Registry
from nionswift_plugin.nion_instrumentation_ui import CameraControlPanel


class ConfigDialog(Dialog.ActionDialog):
    def __init__(self, ui, parent_window: Window.Window):
        super().__init__(ui, parent_window=parent_window)
        self.content.add(ui.create_label_widget("LABEL"))


class CameraPanelDelegate(CameraControlPanel.CameraPanelDelegate):

    camera_panel_delegate_type = "usim_camera_panel_delegate"

    def has_feature(self, feature_flag: str) -> bool:
        return feature_flag in ("configuration", "help")

    def open_help(self, *, api_broker: PlugInManager.APIBroker = None) -> bool:
        print("HELP")
        return True

    def open_configuration(self, *, api_broker: PlugInManager.APIBroker,
                           hardware_source_id: str = None,
                           camera_device: camera_base.CameraDevice = None,
                           camera_settings: camera_base.CameraSettings = None) -> bool:
        api = api_broker.get_api('1')
        parent_window = api.application.document_controllers[0]._document_controller

        if not parent_window.is_dialog_type_open(ConfigDialog):
            ConfigDialog(parent_window.ui, parent_window).show()

        return True

    def get_configuration_ui_handler(self, *, api_broker: PlugInManager.APIBroker = None,
                                     event_loop: asyncio.AbstractEventLoop = None,
                                     hardware_source_id: str = None,
                                     camera_device: camera_base.CameraDevice = None,
                                     camera_settings: camera_base.CameraSettings = None,
                                     **kwargs):
        assert api_broker
        u = typing.cast(Declarative.DeclarativeUI, api_broker.get_ui("~1.0"))

        class Handler:
            ui_view = u.create_row(u.create_label(text="LABEL2"), u.create_push_button(text="Push", on_clicked="cancel_clicked"))

            def cancel_clicked(self, widget):
                print("CLICK")

        return Handler()


def run():
    camera_panel_delegate = CameraPanelDelegate()

    Registry.register_component(camera_panel_delegate, {"camera_panel_delegate"})
