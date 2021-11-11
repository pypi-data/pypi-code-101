
import odrive.database
from odrive.enums import *
from odrive.rich_text import RichText
import odrive.enums
import time
from typing import NamedTuple
import re
import struct
import functools

example_config_raw = {
    "version": "0.1",

    "devices": [
        {
            "product": "ODrive Pro v4.4-58V",
            "serial_number": "356E395D3339",
        },
    ],

    "axes": [
        {
            "motors": [
                {
                    "type": "D5065-270KV",
                    "scale": 1.0
                }
            ],
            "encoders": [
                {
                    "type": "amt102",
                    "scale": 1.0
                },
            ],
            "pos_encoder": 0,
            "vel_encoder": 0,
            "commutation_encoder": 0,
            "pos_index": False,
            "pos_index_offset": None
        }
    ],

    # Each entry represents one RS485 bus
    #"connections_rs485": [
    #    # Each entry in a bus represents one port
    #    #[("axis.encoder", 0, 0), ("odrive.rs485", 0, 0)]
    #],
    "ab_connections": [
        ["devices.0.inc_enc.0", "axes.0.encoders.0.ab"],
    ],
    "three_phase_connections": [
        ["devices.0.phases.0", "axes.0.motors.0.phases"],
    ],
    "dc_connections": [

    ],
    "rs485_connections": [

    ],
    "digital_connections": [
        ["devices.0.io.gpio12", "axes.0.encoders.0.z"],
    ],
    "thermistor_connections": [
    ]
}

db = odrive.database.load()

CALIBRATION_STATUS_OK = object()
CALIBRATION_STATUS_NEEDED = object()
CALIBRATION_STATUS_RECOMMENDED = object()
CALIBRATION_STATUS_UNKNOWN = object()

reboot_vars = [
    r'^inc_encoder[0-9]+.config.enabled$',
    r'^amt21_encoder_group0\.config\.enable$',
]

class Ref():
    pass

class GlobalRef(Ref):
    def __eq__(self, other):
        return isinstance(other, GlobalRef)

class DeviceRef(Ref):
    def __init__(self, num: int):
        self.num = num
    def __eq__(self, other):
        return isinstance(other, DeviceRef) and self.num == other.num
    def __hash__(self):
        return hash(self.num)

class IncEncIntfRef(Ref):
    def __init__(self, dev_ref: DeviceRef, num: int):
        self.dev_ref = dev_ref
        self.num = num
    def __eq__(self, other):
        return isinstance(other, IncEncIntfRef) and self.dev_ref == other.dev_ref and self.num == other.num
    def __hash__(self):
        return hash((self.dev_ref, self.num))

class Rs485IntfRef(Ref):
    def __init__(self, dev_ref: DeviceRef, num: int):
        self.dev_ref = dev_ref
        self.num = num
    def __eq__(self, other):
        return isinstance(other, IncEncIntfRef) and self.dev_ref == other.dev_ref and self.num == other.num
    def __hash__(self):
        return hash((self.dev_ref, self.num))

class GpioRef(Ref):
    def __init__(self, dev_ref: DeviceRef, name: str):
        self.dev_ref = dev_ref
        self.name = name
    def __eq__(self, other):
        return isinstance(other, GpioRef) and self.dev_ref == other.dev_ref and self.name == other.name
    def __hash__(self):
        return hash((self.dev_ref, self.name))

class InverterRef(Ref):
    def __init__(self, dev_ref: DeviceRef, num: int):
        self.dev_ref = dev_ref
        self.num = num
    def __eq__(self, other):
        return isinstance(other, InverterRef) and self.dev_ref == other.dev_ref and self.num == other.num

class AxisRef(Ref):
    def __init__(self, num: int):
        self.num = num
    def __eq__(self, other):
        return isinstance(other, AxisRef) and self.num == other.num
    def __hash__(self):
        return hash(self.num)

class EncoderRef(Ref):
    def __init__(self, axis_ref: AxisRef, num: int):
        self.axis_ref = axis_ref
        self.num = num
    def __eq__(self, other):
        return isinstance(other, EncoderRef) and self.axis_ref == other.axis_ref and self.num == other.num
    def __hash__(self):
        return hash((self.axis_ref, self.num))

class MotorRef(Ref):
    def __init__(self, axis_ref: AxisRef, num: int):
        self.axis_ref = axis_ref
        self.num = num
    def __eq__(self, other):
        return isinstance(other, MotorRef) and self.axis_ref == other.axis_ref and self.num == other.num
    def __hash__(self):
        return hash((self.axis_ref, self.num))



class CalibrationTask():
    def __init__(self, name, func, status):
        self.name = name
        self.func = func
        self.status = status

    def run(self):
        self.func()

class IssueType():
    ERROR = object() # error level issues prevent the configuration from being written onto the ODrive(s)
    WARN = object() # warn level issues don't prevent the configuration from being applied but require user attention

class IssueCollection():
    def __init__(self):
        self.issues = []

    def append(self, ref, message, level = IssueType.ERROR):
        """
        Appends an issue to the issue collection.

        `ref` defines which object in the user configuration the issue pertains
        to.
        """
        if isinstance(ref, Ref):
            self.issues.append((ref, message, level))
        elif isinstance(ref, list):
            for r in ref:
                self.issues.append((r, message, level))
        else:
            assert False, type(ref)

    def get(self, ref: Ref):
        """
        Returns all issues pertaining to the specified configuration object.
        """
        for _ref, message, level in self.issues:
            if _ref == ref:
                yield message, level

    def get_for_type(self, ref_type: type):
        """
        Returns all issues pertaining to any object of the specified type.
        """
        for _ref, message, level in self.issues:
            if isinstance(_ref, ref_type):
                yield _ref, message, level



class EncoderConfig():
    @staticmethod
    def from_json(json):
        return EncoderConfig(
            json['type'],
            json.get('addr', 0x54), # TODO: this should only be present on AMT21
            json.get('scale', 1.0),
        )

    def __init__(self, type: str, addr: int = 0x54, scale: float = 1.0):
        self.type = type
        self.addr = addr
        self.scale = scale

class MotorConfig():
    @staticmethod
    def from_json(json):
        return MotorConfig(
            json['type'],
            json.get('scale', 1.0),
            json.get('phase_resistance', None),
            json.get('phase_inductance', None),
            json.get('use_thermistor', False),
        )

    def __init__(self, type: str, scale: float = 1.0, phase_resistance: float = None, phase_inductance: float = None, use_thermistor: bool = False):
        self.type = type
        self.scale = scale
        self.phase_resistance = phase_resistance
        self.phase_inductance = phase_inductance
        self.use_thermistor = use_thermistor

class AxisConfig():
    """
    Represents one axis in a user machine configuration.
    """

    @staticmethod
    def from_json(json: dict) -> 'AxisConfig':
        """
        Loads an :class:`AxisConfig` object from a dictionary (usually loaded from JSON).
        """
        return AxisConfig(
            motors=[MotorConfig.from_json(cfg) for cfg in json.get('motors', [])],
            encoders=[EncoderConfig.from_json(cfg) for cfg in json.get('encoders', [])],
            calib_scan_vel=json.get('calib_scan_vel', None),
            calib_scan_distance=json.get('calib_scan_distance', None),
            calib_scan_range=json.get('calib_scan_range', None),
            calib_torque=json.get('calib_torque', None),
            pos_encoder=json.get('pos_encoder', None),
            vel_encoder=json.get('vel_encoder', None),
            commutation_encoder=json.get('commutation_encoder', None),
            pos_index=json.get('pos_index', False),
            pos_index_offset=json.get('pos_index_offset', None)
        )

    def __init__(self, motors, encoders, calib_scan_vel: float = None, calib_scan_distance: float = None, calib_scan_range: float = None, calib_torque: float = None, pos_encoder: int = None, vel_encoder: int = None, commutation_encoder: int = None, pos_index: bool = False, pos_index_offset = None):
        self.motors = motors
        self.encoders = encoders
        self.calib_scan_vel = calib_scan_vel
        self.calib_scan_distance = calib_scan_distance
        self.calib_scan_range = calib_scan_range
        self.calib_torque = calib_torque
        self.pos_encoder = pos_encoder
        self.vel_encoder = vel_encoder
        self.commutation_encoder = commutation_encoder
        self.pos_index = pos_index # TODO: make use of this
        self.pos_index_offset = pos_index_offset

    def add_motor(self, motor_config: MotorConfig):
        self.motors.append(motor_config)

    def add_encoder(self, encoder_type: str, cpr: int, use_for_pos: bool, use_for_vel: bool, use_for_commutation: bool):
        self.encoders.append(EncoderConfig({'type': encoder_type}))
        if use_for_pos:
            self.pos_encoder = len(self.encoders) - 1
        if use_for_vel:
            self.vel_encoder = len(self.encoders) - 1
        if use_for_commutation:
            self.commutation_encoder = len(self.encoders) - 1

class DeviceConfig():
    """
    Represents the configuration of one ODrive device.
    """

    @staticmethod
    def from_json(json):
        return DeviceConfig(
            product=json['product'],
            serial_number=json.get('serial_number', None),
            shunt_conductances=json.get('shunt_conductances', None)
        )

    def __init__(self, product: str, serial_number: str = None, shunt_conductances = None):
        self.product = product
        self.serial_number = serial_number
        self.shunt_conductances = shunt_conductances if (not shunt_conductances is None) else ([None] * len(db.get_product(self.product)['inverters']))

class MachineConfig():
    """
    Represents the configuration of a machine.

    This includes a list of axes, a list of ODrive devices and information about
    how the axes and devices are connected.
    """

    @staticmethod
    def make_empty():
        data = {
            'version': '0.1',
            'devices': [],
            'axes': [],
        }
        return MachineConfig(data)

    def __init__(self, data):
        if data['version'] != "0.1":
            raise Exception("Unsupported config version " + str(data['version']))

        # Load devices
        self.devices = [DeviceConfig.from_json(device_json) for device_json in data['devices']]

        # Load axes
        self.axes = [AxisConfig.from_json(axis_json) for axis_json in data['axes']]

        # Load connections
        all_refs = {}
        for dev_num, dev in enumerate(self.devices):
            dev_ref = DeviceRef(dev_num)
            dev_data = db.get_product(dev.product)
            all_refs.update({'devices.' + str(dev_num) + '.phases.' + str(i): InverterRef(dev_ref, i) for i, _ in enumerate(dev_data['inverters'])})
            all_refs.update({'devices.' + str(dev_num) + '.inc_enc.' + str(i): IncEncIntfRef(dev_ref, i) for i, _ in enumerate(dev_data['inc_enc'])})
            all_refs.update({'devices.' + str(dev_num) + '.io.' + k: GpioRef(dev_ref, k) for k in dev_data['io'].keys()})
        for axis_num, axis in enumerate(self.axes):
            axis_ref = AxisRef(axis_num)
            all_refs.update({'axes.' + str(axis_num) + '.encoders.' + str(i) + '.ab': EncoderRef(axis_ref, i) for i, _ in enumerate(axis.encoders)}) # TODO: check if this encoder supports A/B
            all_refs.update({'axes.' + str(axis_num) + '.encoders.' + str(i) + '.z': EncoderRef(axis_ref, i) for i, _ in enumerate(axis.encoders)}) # TODO: check if this encoder supports index
            all_refs.update({'axes.' + str(axis_num) + '.motors.' + str(i) + '.phases': MotorRef(axis_ref, i) for i, _ in enumerate(axis.motors)})

        def resolve(name):
            if not name in all_refs:
                raise Exception("Unknown port: \"" + name + "\". Known ports are: " + str(list(all_refs.keys())))
            return all_refs[name]

        self._ab_connections = [[resolve(port) for port in conn] for conn in data.get('ab_connections', [])]
        self._rs485_connections = [[resolve(port) for port in conn] for conn in data.get('rs485_connections', [])]
        self._three_phase_connections = [[resolve(port) for port in conn] for conn in data.get('three_phase_connections', [])]
        self._dc_connections = [[resolve(port) for port in conn] for conn in data.get('dc_connections', [])]
        self._digital_connections = [[resolve(port) for port in conn] for conn in data.get('digital_connections', [])]
        self._thermistor_connections = [[resolve(port) for port in conn] for conn in data.get('thermistor_connections', [])]

    def add_axis(self, axis_config: AxisConfig):
        """
        Adds an axis to the machine config.
        """
        self.axes.append(axis_config)
        return len(self.axes) - 1

    def add_device(self, dev_config: DeviceConfig):
        """
        Adds an ODrive device to the machine config.
        """
        self.devices.append(dev_config)
        return len(self.devices) - 1

    def connect_phases(self, *refs):
        assert all([isinstance(r, InverterRef) or isinstance(r, MotorRef) for r in refs])
        self._three_phase_connections.append(refs)

    def connect_abz(self, enc_ref, inc_enc_intf_ref, z_gpio_ref = None):
        assert isinstance(enc_ref, EncoderRef)
        assert isinstance(inc_enc_intf_ref, IncEncIntfRef)
        assert z_gpio_ref is None or isinstance(z_gpio_ref, GpioRef)
        # TODO: register connection for index signal
        self._ab_connections.append([enc_ref, inc_enc_intf_ref])

    def connect_rs485(self, enc_ref, rs485_intf_ref):
        assert isinstance(enc_ref, EncoderRef)
        assert isinstance(rs485_intf_ref, Rs485IntfRef)
        self._rs485_connections.append([enc_ref, rs485_intf_ref])

    def get_status(self, odrives):
        """
        Returns various information about the machine configuration taking into
        account the list of currently connected ODrives and their state.

        Returns a tuple (odrv_list, output_configs, issues, axis_calib)
        where:

        odrv_list: A list of ODrive objects that need to be configured. Each
            entry corresponds to one device in this configuration object. Some
            entries can be None.
        output_configs: A list of multi-level dictionaries that hold all
            configuration settings for all ODrives, whether they are connected or
            not. The order an length of this list corresponds to `odrv_list`.
        issues: An `IssueCollection` containing all errors and warnings that
            were found.
        needs_reboot: A list of booleans indicating for each device if a reboot
            is required after applying the new configuration.
        axis_calib: A list of lists of CalibrationTask objects representing the
            available calibration tasks for this axis.
            Each list in axis_calib corresponds to an axis in this configuration.
        """

        output_configs = [{'config': {}} for _ in range(len(self.devices))]
        issues = IssueCollection()
        axis_calib = [[] for _ in range(len(self.axes))]
        encoder_ids = [{} for _ in range(len(self.devices))]

        def group_conn_by_type(conn, types, issues, error_text):
            items = [[] for _ in types]
            for port in conn:
                expected_type = False
                for i, t in enumerate(types):
                    if isinstance(port, t):
                        items[i].append(port)
                        expected_type = True
                        break
                if not expected_type:
                    issues.append(port, error_text)
            return tuple(items)

        # Associate devices in the configuration with connected devices
        odrv_list = [None for _ in range(len(self.devices))]
        for dev_num, dev_config in enumerate(self.devices):
            if dev_config.serial_number is None:
                issues.append(DeviceRef(dev_num), 'Not associated with any serial number.')
            elif not dev_config.serial_number in odrives:
                issues.append(DeviceRef(dev_num), 'Not connected.')
            else:
                dev = odrives[dev_config.serial_number]
                product = 'ODrive Pro v{}.{}-{}V'.format(dev.hw_version_major, dev.hw_version_minor, dev.hw_version_variant)
                if dev_config.product != product:
                    issues.append(DeviceRef(dev_num), 'Expected {} but found {}.'.format(dev_config.product, product))
                else:
                    odrv_list[dev_num] = dev

        for k, o in odrives.items():
            if not k in [c.serial_number for c in self.devices]:
                issues.append(GlobalRef(), "Unused ODrive: " + k, IssueType.WARN)

        # Configure RS485 encoders
        for conn in self._rs485_connections:
            rs485_intf_refs, enc_refs = group_conn_by_type(conn, [Rs485IntfRef, EncoderRef], issues, "Cannot be connected to a RS485 bus")

            if len(rs485_intf_refs) > 1:
                issues.append(rs485_intf_refs, "Multiple ODrives are not allowed on the same RS485 bus")
                continue
            if len(rs485_intf_refs) < 1:
                continue # not an error

            rs485_intf_ref = rs485_intf_refs[0]
            odrv_output_config = output_configs[rs485_intf_ref.dev_ref.num]

            for enc_ref in enc_refs:
                encoder_config = self.axes[enc_ref.axis_ref.num].encoders[enc_ref.num]
                enc_data = db.get_encoder(encoder_config.type)

                if encoder_config.type != 'amt21':
                    issues.append(enc_ref, f"Encoder type {encoder_config.type} not supported over RS485.")
                    continue # ignore encoder

                # Each amt21_encoder_group is dedictated to one RS485 port on the ODrive.
                # One port can talk to multiple encoders (needs firmware change!).
                if f'amt21_encoder_group{rs485_intf_ref.num}' in odrv_output_config:
                    amt21_encoder_group_config = odrv_output_config[f'amt21_encoder_group{rs485_intf_ref.num}']
                else:
                    amt21_encoder_group_config = {'config': {'enable': True, 'rs485': rs485_intf_ref.num}}
                    odrv_output_config[f'amt21_encoder_group{rs485_intf_ref.num}'] = amt21_encoder_group_config

                if 'addr0' in amt21_encoder_group_config['config']:
                    issues.append(rs485_intf_ref.dev_ref, rs485_intf_ref.dev_ref.num, f"Current firmware does not support more than AMT21 encoder.")
                    continue # ignore encoder

                amt21_encoder_group_config['config']['addr0'] = encoder_config.addr # use default AMT21 address if unspecified
                encoder_ids[rs485_intf_ref.dev_ref.num][enc_ref] = ENCODER_ID_AMT21_ENCODER0

        # Configure incremental encoders
        for conn in self._ab_connections:
            inc_enc_intf_refs, enc_refs = group_conn_by_type(conn, [IncEncIntfRef, EncoderRef], issues, "Cannot be connected to a A/B signal")

            if len(enc_refs) > 1:
                issues.append(enc_refs, "Multiple incremental encoders cannot share the same A/B signals.")
                continue
            if len(enc_refs) < 1:
                continue # this is not an error

            enc_ref = enc_refs[0]
            enc_data = db.get_encoder(self.axes[enc_ref.axis_ref.num].encoders[enc_ref.num].type)

            for inc_enc_intf_ref in inc_enc_intf_refs:
                output_configs[inc_enc_intf_ref.dev_ref.num]["inc_encoder{}".format(inc_enc_intf_ref.num)] = {
                    'config': {'enabled': True, 'cpr': enc_data['cpr']}
                }
                encoder_ids[inc_enc_intf_ref.dev_ref.num][enc_ref] = [ENCODER_ID_INC_ENCODER0, ENCODER_ID_INC_ENCODER1][inc_enc_intf_ref.num]

        # Configure motors
        for conn in self._three_phase_connections:
            inverter_refs, motor_refs = group_conn_by_type(conn, [InverterRef, MotorRef], issues, "Cannot be connected to a three phase net")

            if len(inverter_refs) > 1:
                issues.append(inverter_refs, "Phase bundling not implemented. Each motor must be connected to at most one inverter.")
            if len(motor_refs) > 1:
                issues.append(motor_refs, "Each inverter must be connected to at most one motor.")
            if len(inverter_refs) != 1 or len(motor_refs) != 1:
                continue

            inverter_ref = inverter_refs[0]
            motor_ref = motor_refs[0]
            
            motor_config = self.axes[motor_ref.axis_ref.num].motors[motor_ref.num]
            motor_data = db.get_motor(motor_config.type)

            axis_output_config = output_configs[inverter_ref.dev_ref.num]['axis{}'.format(inverter_ref.num)] = {'motor': {'config': {}}, 'controller': {'config': {}}, 'config': {}}

            if motor_config.scale != 1.0:
                issues.append(motor_ref, "Support for motor scale other than 1.0 not implemented.")

            if not motor_config.phase_resistance is None:
                axis_output_config['motor']['config']['phase_resistance'] = motor_config.phase_resistance
            else:
                axis_output_config['motor']['config']['phase_resistance'] = motor_data['phase_resistance']

            if not motor_config.phase_inductance is None:
                axis_output_config['motor']['config']['phase_inductance'] = motor_config.phase_inductance
            else:
                axis_output_config['motor']['config']['phase_inductance'] = motor_data['phase_inductance']

            # TODO: take into account user max current
            # Note: we multiply the motor current limit by two since it's given in "continuous max"
            inv_data = db.get_product(self.devices[inverter_ref.dev_ref.num].product)['inverters'][inverter_ref.num]
            axis_output_config['motor']['config']['current_lim'] = min(inv_data['max_current'], 2 * motor_data['max_current'])

            axis_output_config['motor']['config']['pole_pairs'] = motor_data['pole_pairs']
            axis_output_config['motor']['config']['torque_constant'] = motor_data['torque_constant']
            axis_output_config['motor']['config']['pre_calibrated'] = True

            calibrated = (not motor_config.phase_resistance is None) and (not motor_config.phase_inductance is None)
            if not odrv_list[inverter_ref.dev_ref.num] is None:
                calib = functools.partial(_run_motor_calibration, getattr(odrv_list[inverter_ref.dev_ref.num], 'axis{}'.format(inverter_ref.num)), motor_config)
            else:
                calib = None
            axis_calib[motor_ref.axis_ref.num].append(CalibrationTask(
                "Motor Calibration",
                calib,
                CALIBRATION_STATUS_OK if calibrated else CALIBRATION_STATUS_RECOMMENDED
                ))

        # Configure thermistors
        for conn in self._thermistor_connections:
            if motor_coords is None:
                continue # this thermistor input is not connected anywhere
            (axis_num, motor_num) = motor_coords
            axis_config = config['axes'][axis_num]
            motor_config = axis_config['motors'][motor_num]
            motor_data = db.get_motor(motor_config['type'])

            if motor_coords != odrv_config['motors'][temp_in_num]:
                issues.append(motor_ref, f"The motor thermistor must either be disconnected or connected to the thermistor input that corresponds to the same ODrive and axis to which the motor is connected.")
                continue

            axis_output_config = odrv_output_config['axis{}'.format(temp_in_num)]

            odrv_data = db.get_odrive(odrv_config['board_version'])
            temp_in_data = odrv_data['temp_in'][temp_in_num]

            coeffs = odrive.utils.calculate_thermistor_coeffs(3, temp_in_data['r_load'], motor_data['thermistor_r25'], motor_data['thermistor_beta'], 0, motor_data['max_temp'] + 10, temp_in_data['thermistor_bottom'])
            axis_output_config['motor']['motor_thermistor'] = {
                'config': {
                    'poly_coefficient_0': float(coeffs[3]),
                    'poly_coefficient_1': float(coeffs[2]),
                    'poly_coefficient_2': float(coeffs[1]),
                    'poly_coefficient_3': float(coeffs[0]),
                    'temp_limit_lower': motor_data['max_temp'] - 20,
                    'temp_limit_upper': motor_data['max_temp'],
                    'enabled': True # requires reboot (?)
                }
            }
            # TODO: set corresponding GPIO mode to 3 (or probably should be handled by firmware)

        # Configure shunt conductance
        for dev_num, dev_config in enumerate(self.devices):
            for inv_num, shunt_conductance in enumerate(dev_config.shunt_conductances):
                if not shunt_conductance is None:
                    axis_output_config = output_configs[dev_num]['axis{}'.format(inv_num)]
                    axis_output_config['motor']['config']['shunt_conductance'] = shunt_conductance

        # Other configuration
        for dev_num, odrv_config in enumerate(self.devices):
            output_config = output_configs[dev_num]

            # TODO: set vbus voltage trip level based on power supply setting
            # TODO: set dc_max_negative_current based on power supply setting
            output_config['config']['enable_brake_resistor'] = False
            output_config['config']['dc_max_negative_current'] = -1

        # Configure axes
        for axis_num, axis_config in enumerate(self.axes):
            axis_ref = AxisRef(axis_num)

            conns = [conn for motor_num in range(len(axis_config.motors)) for conn in self._three_phase_connections if (MotorRef(axis_ref, motor_num) in conn)]
            inverter_refs = [inv for conn in conns for inv in conn if isinstance(inv, InverterRef)]

            if len(inverter_refs) == 0:
                issues.append(axis_ref, f"Not connected to any inverter.")
                continue
            if len(inverter_refs) > 1:
                issues.append(axis_ref, f"Connected to more than one inverters.")
                continue

            inverter_ref = inverter_refs[0]

            axis_output_config = output_configs[inverter_ref.dev_ref.num]['axis{}'.format(inverter_ref.num)]

            if not axis_config.calib_scan_vel is None:
                axis_output_config['config']['calib_scan_vel'] = axis_config.calib_scan_vel * motor_data['pole_pairs'] * motor_config['scale']
            
            if not axis_config.calib_scan_distance is None:
                axis_output_config['config']['calib_scan_distance'] = axis_config.calib_scan_distance * motor_data['pole_pairs'] * motor_config['scale']
            
            if not axis_config.calib_scan_range is None:
                axis_output_config['config']['calib_scan_range'] = axis_config.calib_scan_range
            
            # TODO: check if larger than current limit
            if not axis_config.calib_torque is None:
                axis_output_config['motor']['config']['calibration_current'] = axis_config.calib_torque / motor_data['torque_constant']

            if axis_config.pos_encoder is None:
                # TODO: use sensorless mode
                issues.append(axis_ref, "No position encoder specified")
            else:
                enc_id = encoder_ids[inverter_ref.dev_ref.num].get(EncoderRef(axis_ref, axis_config.pos_encoder), None)
                if enc_id is None:
                    issues.append(axis_ref, f"Load encoder of this axis must be connected to the same odrive as the motor ({odrv_config['serial_number']})")
                else:
                    axis_output_config['config']['load_encoder'] = enc_id

            if axis_config.commutation_encoder is None:
                # TODO: use sensorless mode
                issues.append(axis_ref, "No commutation encoder specified")
            else:
                enc_id = encoder_ids[inverter_ref.dev_ref.num].get(EncoderRef(axis_ref, axis_config.commutation_encoder), None)
                if enc_id is None:
                    issues.append(axis_ref, f"Commutation encoder of this axis must be connected to the same odrive as the motor ({odrv_config['serial_number']})")
                else:
                    axis_output_config['config']['commutation_encoder'] = enc_id

            if axis_config.vel_encoder is None:
                # TODO: use sensorless mode
                issues.append(axis_ref, "No commutation encoder specified")
            elif axis_config.vel_encoder == axis_config.commutation_encoder:
                axis_output_config['controller']['config']['use_commutation_vel'] = False
            elif axis_config.vel_encoder == axis_config.pos_encoder:
                axis_output_config['controller']['config']['use_commutation_vel'] = True
            else:
                issues.append(axis_ref, "The velocity encoder must be the same as either the position encoder or the commutation encoder.")

            #if enc_id in [ENCODER_ID_INC_ENCODER0, ENCODER_ID_INC_ENCODER1]:
            axis = None if odrv_list[inverter_ref.dev_ref.num] is None else getattr(odrv_list[inverter_ref.dev_ref.num], 'axis{}'.format(inverter_ref.num))
            axis_calib[inverter_ref.num].append(CalibrationTask(
                "Encoder Offset Calibration",
                None if axis is None else functools.partial(_run_encoder_offset_calibration, axis),
                (CALIBRATION_STATUS_OK if ((not axis is None) and axis.commutation_mapper.status == COMPONENT_STATUS_NOMINAL) else
                CALIBRATION_STATUS_NEEDED if ((not axis is None) and axis.commutation_mapper.status == COMPONENT_STATUS_RELATIVE_MODE) else
                CALIBRATION_STATUS_UNKNOWN)
            ))


        def compare(path, obj, config):
            all_equal = True
            reboot_required = False

            for k, v in config.items():
                if isinstance(v, dict):
                    equal, sub_reboot = compare(path + [k], getattr(obj, k), v)
                    reboot_required = reboot_required or sub_reboot
                elif isinstance(v, float):
                    # TODO: this comparison is a bit fragile (shouldn't compare floats like this)
                    equal = struct.unpack("f", struct.pack("f", v))[0]
                else:
                    equal = getattr(obj, k) == v

                all_equal = all_equal and equal
                if not equal:
                    name = '.'.join(path + [k])
                    #print("changed: ", name)
                    if any(re.match(r, name) for r in reboot_vars):
                        reboot_required = True
            return all_equal, reboot_required

        needs_reboot = [False] * len(odrv_list)
        for odrv_num, odrv in enumerate(odrv_list):
            if not odrv is None:
                all_equal, needs_reboot[odrv_num] = compare([], odrv, output_configs[odrv_num])
                if not all_equal:
                    issues.append(DeviceRef(odrv_num), "Configuration needs to be committed to ODrive", IssueType.WARN)
                needs_reboot[odrv_num] = needs_reboot[odrv_num] or odrv.reboot_required
                if needs_reboot[odrv_num]:
                    issues.append(DeviceRef(odrv_num), "Reboot required", IssueType.WARN)

        return odrv_list, output_configs, issues, needs_reboot, axis_calib
#

    def show_status(self, odrives):
        """
        Prints the status of the configuration in a human readable format.
        This includes warnings about any issues with the configuration, calibration
        status and more.
        """

        odrv_list, output_configs, issues, needs_reboot, axis_calib = self.get_status(odrives)

        print(len(issues.issues), 'issues', issues.issues)
        print(output_configs)

        lines = []

        check_sign = "\u2705"
        info_sign = "\U0001F4A1"
        warning_sign = "\u26A0\uFE0F "
        error_sign = "\u274C"
        question_sign = "  " # TODO

        sign = {
            IssueType.WARN: warning_sign,
            IssueType.ERROR: error_sign
        }

        style = {
            IssueType.WARN: RichText.STYLE_YELLOW,
            IssueType.ERROR: RichText.STYLE_RED
        }

        for message, level in issues.get(GlobalRef()):
            lines.append(sign[level] + " " + RichText(message, style[level]))

        for dev_num, dev_config in enumerate(self.devices):
            dev_ref = DeviceRef(dev_num)
            if not dev_config.serial_number is None:
                name = "ODrive with serial number " + str(dev_config.serial_number)
            else:
                name = "ODrive {} (unspecified serial number)".format(dev_num)
            lines.append(name)
            for message, level in issues.get(dev_ref):
                lines.append("  " + sign[level] + " " + RichText(message, style[level]))

        for axis_num in range(len(self.axes)):
            axis_ref = AxisRef(axis_num)
            lines.append("Axis " + str(axis_num))
            for message, level in issues.get(axis_ref):
                lines.append("  " + sign[level] + " " + RichText(message, style[level]))
            for ref, message, level in issues.get_for_type(MotorRef):
                if ref.axis_ref == axis_ref:
                    lines.append("  " + sign[level] + " Motor " + str(ref.num) + ": " + RichText(message, style[level]))
            for ref, message, level in issues.get_for_type(EncoderRef):
                if ref.axis_ref == axis_ref:
                    lines.append("  " + sign[level] + " Encoder " + str(ref.num) + ": " + RichText(message, style[level]))

            for calib in axis_calib[axis_num]:
                if calib.status == CALIBRATION_STATUS_OK:
                    lines.append("  " + check_sign + " " + RichText(str(calib.name) + " ok", RichText.STYLE_GREEN))
                elif calib.status == CALIBRATION_STATUS_RECOMMENDED:
                    lines.append("  " + info_sign + " " + RichText(str(calib.name) + " recommended", RichText.STYLE_DEFAULT))
                elif calib.status == CALIBRATION_STATUS_NEEDED:
                    lines.append("  " + warning_sign + " " + RichText(str(calib.name) + " needed", RichText.STYLE_BOLD))
                elif calib.status == CALIBRATION_STATUS_UNKNOWN:
                    lines.append("  " + question_sign + " " + RichText(str(calib.name) + ": unknown status", RichText.STYLE_GRAY))
                else:
                    assert(False)

        print(RichText("\n").join(lines))


    def apply(self, odrives):
        """
        Commits the configuration to the odrives. A reboot may be needed after
        this.

        If there a are problems with the configuration this function throws an
        exception and does not change anything on any ODrive.
        In this case show_status() can be used to get more detailed error
        information.

        Returns a list of devices that need a reboot before the configuration
        takes effect.
        """

        odrv_list, output_configs, issues, needs_reboot, axis_calib = self.get_status(odrives)

        if any([m for _, m, level in issues.issues if level == IssueType.ERROR]):
            print([m for _, m, level in issues.issues if level == IssueType.ERROR])
            raise Exception("There are problems with this configuration. No changes were applied to the ODrive(s).")

        def _apply(obj, config):
            for k, v in config.items():
                if isinstance(v, dict):
                    _apply(getattr(obj, k), v)
                else:
                    setattr(obj, k, v)

        for odrv_num, odrv in enumerate(odrv_list):
            if not odrv is None:
                if needs_reboot[odrv_num]:
                    odrv.reboot_required = True
                _apply(odrv, output_configs[odrv_num])

        return [odrv_list[num] for num, r in enumerate(needs_reboot) if r]

    def calibrate(self, odrives, include_optional = False):
        """
        Runs the calibration tasks for this machine configuration based on the
        current state of the ODrives. This can include a reboot of one or more
        ODrives.
        """

        odrv_list, output_configs, issues, needs_reboot, axis_calibs = self.get_status(odrives)

        if any(needs_reboot):
            raise Exception("Some devices need to be rebooted for the configuration to take effect.")

        for axis_num, axis_calib in enumerate(axis_calibs):
            for calib in axis_calib:
                if (calib.status == CALIBRATION_STATUS_RECOMMENDED and include_optional) or calib.status == CALIBRATION_STATUS_NEEDED:
                    print("Running {} on axis {}...".format(calib.name, axis_num))
                    calib.run()
        print("Done!")

example_config = MachineConfig(example_config_raw)



def _run_state(axis, state):
    axis.requested_state = state
    while axis.requested_state == state:
        time.sleep(0.1)
    while axis.procedure_result == PROCEDURE_RESULT_BUSY:
        time.sleep(0.1)

    result = axis.procedure_result
    if result != PROCEDURE_RESULT_SUCCESS:
        codes = {v: k for k, v in odrive.enums.__dict__ .items() if k.startswith("PROCEDURE_RESULT_")}
        raise Exception("Device returned {}".format(codes.get(result, "unknown code {}".format(result))))

def _run_motor_calibration(axis, motor_config):
    _run_state(axis, AXIS_STATE_MOTOR_CALIBRATION)
    motor_config['phase_resistance'] = axis.motor.config.phase_resistance
    motor_config['phase_inductance'] = axis.motor.config.phase_inductance

def _run_encoder_offset_calibration(axis):
    _run_state(axis, AXIS_STATE_ENCODER_OFFSET_CALIBRATION)

