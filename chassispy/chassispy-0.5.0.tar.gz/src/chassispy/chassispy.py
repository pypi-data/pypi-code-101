#!/usr/bin/env python3
# coding=UTF-8


import sys
import os
import asyncio
import can
import time
import threading
import ctypes
import struct
# import can_msgs
# import rospy

from datetime import datetime
from can import Message
from socket import MsgFlag
from typing import ByteString, Set, Type
from can import bus, interface

from datetime import date
from sqlite3.dbapi2 import Date

import chassispy.UGVConfigMsg as ChassisBaseMsg

# 当前操作系统的类型
# posix： Linux
# nt: Windows
# java: Java虚拟机

os_is_nt = os.name == 'nt'
# Linux跟Mac都属于 posix 标准
# posix: 类Unix 操作系统的可移植API
os_is_posix = os.name == 'posix'


class CanMsgsGet:
    def __init__(self, capacity=1024 * 4):
        self.size = 0
        self.rear = 0
        self.front = 0
        self.array = capacity

    def ArrayGet(self):
        bus = can.interface.Bus(bustype='socketcan',
                                channel='can0',
                                bitrate=500000)
        print('can connect is ok')

        msg = bus.recv(0.1)
        if msg is None:
            print('time occerred,no message')
        else:
            can.Message = msg
            self.AllMsgsGet()

    def CanMsgsProcess(self, msg):
        """
        Process can data according to ID
        """

        msg = msg
        if (msg.arbitration_id == ChassisBaseMsg.CanID.SYSTEM_STATE_ID
            ):
            vehicle_state = int(msg.data[0])
            ChassisBaseMsg.SetVehicleState(vehicle_state)
            control_mode = msg.data[1]
            ChassisBaseMsg.SetControlMode(control_mode)
            battery_voltage = float((msg.data[2] & 0xff) << 8
                                    | msg.data[3]) / 10
            ChassisBaseMsg.SetBatteryVoltage(battery_voltage)
            error_code = msg.data[5]
            ChassisBaseMsg.SetErrorCode(error_code)
            count_num = msg.data[7]

            # print(
            #     'vehicle_state:%s control_mode:%s battery_voltage:%s error_code:%s  count_num:%s'
            #     % (vehicle_state, control_mode, battery_voltage, error_code,
            #        count_num))
        elif (msg.arbitration_id ==
              ChassisBaseMsg.CanID.MOTION_STATE_ID):
            linear_velocity_get = ctypes.c_int16((msg.data[0] & 0xff) << 8
                                    | msg.data[1])
                                
            linear_velocity=float(linear_velocity_get.value/1000) 
            # print(int(linear_velocity))                   
            ChassisBaseMsg.SetLinearVelocity(linear_velocity)
            angular_velocity_get = ctypes.c_int16((msg.data[2] & 0xff) << 8
                                     | msg.data[3]) 
            angular_velocity=float(angular_velocity_get.value/1000)
            ChassisBaseMsg.SetAngularVelocity(angular_velocity)
            lateral_velocity_get = ctypes.c_int16((msg.data[4] & 0xff) << 8
                                     | msg.data[5])
            lateral_velocity=float(lateral_velocity_get.value/1000)
            ChassisBaseMsg.SetLateralVelocity(lateral_velocity)
            steering_angle_get = ctypes.c_int16((msg.data[6] & 0xff) << 8
                                   | msg.data[7])
            steering_angle=float(steering_angle_get.value/1000)                       
            ChassisBaseMsg.SetSteeringAngle(steering_angle)
            # print(msg)
            
            # print(msg)
            # print(
            #     'linear_velocity:%s angular_velocity:%s lateral_velocity:%s steering_angle:%s '
            #     % (linear_velocity, angular_velocity, lateral_velocity,
            #        steering_angle))

        elif (msg.arbitration_id ==
              ChassisBaseMsg.CanID.ACTUATOR1_HS_STATE_ID):
            rpm1 = int((msg.data[0] & 0xff) << 8 | msg.data[1])
            ChassisBaseMsg.SetRpm1(rpm1)
            current1 = float((msg.data[2] & 0xff) << 8
                             | msg.data[3]) * 0.1
            ChassisBaseMsg.SetCurrent1(current1)
            pulse_count1 = int((msg.data[4] & 0xff) << 24
                               | (msg.data[5] & 0xff) << 16
                               | (msg.data[6] & 0xff) << 8
                               | msg.data[7])
            ChassisBaseMsg.SetPulseCount1(pulse_count1)
            # print('rpm1:%s current1:%s pulse_count1:%s ' %
            #       (rpm1, current1, pulse_count1))

        elif (msg.arbitration_id ==
              ChassisBaseMsg.CanID.ACTUATOR2_HS_STATE_ID):
            rpm2 = int((msg.data[0] & 0xff) << 8 | msg.data[1])
            ChassisBaseMsg.SetRpm2(rpm2)
            current2 = float((msg.data[2] & 0xff) << 8
                             | msg.data[3]) * 0.1
            ChassisBaseMsg.SetCurrent2(current2)
            pulse_count2 = int((msg.data[4] & 0xff) << 24
                               | (msg.data[5] & 0xff) << 16
                               | (msg.data[6] & 0xff) << 8
                               | msg.data[7])
            ChassisBaseMsg.SetPulseCount2(pulse_count2)
            # print('rpm2:%s current2:%s pulse_count2:%s ' %
            #       (rpm2, current2, pulse_count2))

        elif (msg.arbitration_id ==
              ChassisBaseMsg.CanID.ACTUATOR3_HS_STATE_ID):
            rpm3 = int((msg.data[0] & 0xff) << 8 | msg.data[1])
            ChassisBaseMsg.SetRpm3(rpm3)
            current3 = float((msg.data[2] & 0xff) << 8
                             | msg.data[3]) * 0.1
            ChassisBaseMsg.SetCurrent3(current3)
            pulse_count3 = int((msg.data[4] & 0xff) << 24
                               | (msg.data[5] & 0xff) << 16
                               | (msg.data[6] & 0xff) << 8
                               | msg.data[7])
            ChassisBaseMsg.SetPulseCount3(pulse_count3)
            # print('rpm3:%s current3:%s pulse_count3:%s ' %
            #       (rpm3, current3, pulse_count3))

        elif (msg.arbitration_id ==
              ChassisBaseMsg.CanID.ACTUATOR4_HS_STATE_ID):
            rpm4 = int((msg.data[0] & 0xff) << 8 | msg.data[1])
            ChassisBaseMsg.SetRpm4(rpm4)
            current4 = float((msg.data[2] & 0xff) << 8
                             | msg.data[3]) * 0.1
            ChassisBaseMsg.SetCurrent4(current4)
            pulse_count4 = int((msg.data[4] & 0xff) << 24
                               | (msg.data[5] & 0xff) << 16
                               | (msg.data[6] & 0xff) << 8
                               | msg.data[7])
            ChassisBaseMsg.SetPulseCount4(pulse_count4)

            # print('rpm4:%s current4:%s pulse_count4:%s ' %
            #       (rpm4, current4, pulse_count4))

        elif (msg.arbitration_id ==
              ChassisBaseMsg.CanID.ACTUATOR1_LS_STATE_ID):
            driver1_voltage = float((msg.data[0] & 0xff) << 8
                                    | msg.data[1]) * 0.1
            ChassisBaseMsg.SetDriver1Voltage(driver1_voltage)
            driver1_temp = int((msg.data[2] & 0xff) << 8
                               | msg.data[3])
            ChassisBaseMsg.SetDriver1Temp(driver1_temp)
            motor1_temp = msg.data[4]
            ChassisBaseMsg.SetMotor1Temp(motor1_temp)
            driver1_state = msg.data[5]
            ChassisBaseMsg.SetDriver1State(driver1_state)
            # print(
            #     'driver_voltage1:%s driver_temp1:%s motor_temp%s driver_state1:%s '
            #     % (driver1_voltage, driver1_temp, motor1_temp, driver1_state))

        elif (msg.arbitration_id ==
              ChassisBaseMsg.CanID.ACTUATOR2_LS_STATE_ID):
            driver2_voltage = float((msg.data[0] & 0xff) << 8
                                    | msg.data[1]) * 0.1
            ChassisBaseMsg.SetDriver2Voltage(driver2_voltage)
            driver2_temp = int((msg.data[2] & 0xff) << 8
                               | msg.data[3])
            ChassisBaseMsg.SetDriver2Temp(driver2_temp)
            motor2_temp = msg.data[4]
            ChassisBaseMsg.SetMotor2Temp(motor2_temp)
            driver2_state = msg.data[5]
            ChassisBaseMsg.SetDriver2State(driver2_state)
            # print(
            #     'driver_voltage2:%s driver_temp2:%s  motor_temp2:%s driver_state2:%s '
            #     % (driver2_voltage, driver2_temp, motor2_temp, driver2_state))
        elif (msg.arbitration_id ==
              ChassisBaseMsg.CanID.ACTUATOR3_LS_STATE_ID):
            driver3_voltage = float((msg.data[0] & 0xff) << 8
                                    | msg.data[1]) * 0.1
            ChassisBaseMsg.SetDriver3Voltage(driver3_voltage)
            driver3_temp = int((msg.data[2] & 0xff) << 8
                               | msg.data[3])
            ChassisBaseMsg.SetDriver3Temp(driver3_temp)
            motor3_temp = msg.data[4]
            ChassisBaseMsg.SetMotor3Temp(motor3_temp)
            driver3_state = msg.data[5]
            ChassisBaseMsg.SetDriver3State(driver3_state)
            # print(
            #     'driver_voltage3:%s driver_temp3:%s  motor_temp3:%s driver_state3:%s '
            #     % (driver3_voltage, driver3_temp, motor3_temp, driver3_state))
        elif (msg.arbitration_id ==
              ChassisBaseMsg.CanID.ACTUATOR4_LS_STATE_ID):
            driver4_voltage = float((msg.data[0] & 0xff) << 8
                                    | msg.data[1]) * 0.1
            ChassisBaseMsg.SetDriver4Voltage(driver4_voltage)
            driver4_temp = int((msg.data[2] & 0xff) << 8
                               | msg.data[3])
            ChassisBaseMsg.SetDriver4Temp(driver4_temp)
            motor4_temp = msg.data[4]
            ChassisBaseMsg.SetMotor4Temp(motor4_temp)
            driver4_state = msg.data[5]
            ChassisBaseMsg.SetDriver4State(driver4_state)
            # print(
            #     'driver_voltage4:%s driver_temp4:%s  motor_temp:%s driver_state4:%s '
            #     % (driver4_voltage, driver4_temp, motor4_temp, driver4_state))

        elif (msg.arbitration_id == ChassisBaseMsg.CanID.LIGHT_STATE_ID
              ):
            light_cmd_ctrl = (msg.data[0])
            ChassisBaseMsg.SetLightCmdCtrl(light_cmd_ctrl)
            front_mode = (msg.data[1])
            ChassisBaseMsg.SetFrontMode(front_mode)
            front_custom = (msg.data[2])
            ChassisBaseMsg.SetFrontCustom(front_custom)
            rear_mode = (msg.data[3])
            ChassisBaseMsg.SetRearMode(rear_mode)
            rear_custom = (msg.data[4])
            ChassisBaseMsg.SetRearCustom(rear_custom)

            # print(
            #     'enable_cmd_ctrl:%s front_mode:%s  front_custom:%s rear_mode:%s  rear_custom:%s'
            #     % (light_cmd_ctrl, front_mode, front_custom, rear_mode,
            #        rear_custom))
        elif (msg.arbitration_id ==
              ChassisBaseMsg.CanID.VERSION_RESPONSE_ID):
            control_hardware_version = int((msg.data[0] & 0xff) << 8
                                           | msg.data[1])
            ChassisBaseMsg.SetControlHardwareVersion(control_hardware_version)
            actuaror_hardware_version = int((msg.data[2] & 0xff) << 8
                                            | msg.data[3])
            ChassisBaseMsg.SetActuarorHardwareVersion(
                actuaror_hardware_version)
            control_software_version = int((msg.data[4] & 0xff) << 8
                                           | msg.data[5])
            ChassisBaseMsg.SetControlSoftwareVersion(control_software_version)
            actuaror_software_version = int((msg.data[6] & 0xff) << 8
                                            | msg.data[7])
            ChassisBaseMsg.SetActuarorSoftwareVersion(
                actuaror_software_version)
            # print(
            #     'control_hardware_version: %s actuaror_hardware_version: %s' %
            #     (control_hardware_version, actuaror_hardware_version))
            # print('control_software_version:%s actuaror_software_version:%s ' %
            #       (control_software_version, actuaror_software_version))

        elif (msg.arbitration_id == ChassisBaseMsg.CanID.ODOMETRY_ID):
            left_wheel_get = ctypes.c_int((msg.data[0] & 0xff) << 24
                             | (msg.data[1] & 0xff) << 16
                             | (msg.data[2] & 0xff) << 8
                             | msg.data[3])
            left_wheel=left_wheel_get.value
            ChassisBaseMsg.SetLeftWheel(left_wheel)
            right_wheel_get = ctypes.c_int((msg.data[4] & 0xff) << 24
                              | (msg.data[5] & 0xff) << 16
                              | (msg.data[6] & 0xff) << 8
                              | msg.data[7])
            # print('left_wheel: %s right_wheel: %s ' %
            #       (left_wheel, right_wheel))
            right_wheel=right_wheel_get.value
            ChassisBaseMsg.SetRightWheel(right_wheel)
            # print(msg)
        elif (msg.arbitration_id == ChassisBaseMsg.CanID.RC_STATE_ID):
            sws = msg.data[0]
            ChassisBaseMsg.SetSws(sws)
            stick_right_v = msg.data[1]
            ChassisBaseMsg.SetStickRightV(stick_right_v)
            stick_right_h = msg.data[2]
            ChassisBaseMsg.SetStickRightH(stick_right_h)
            stick_left_v = msg.data[3]
            ChassisBaseMsg.SetStickLeftV(stick_left_v)
            stick_left_h = msg.data[4]
            ChassisBaseMsg.SetStickLeftH(stick_left_h)
            var_a = msg.data[5]
            ChassisBaseMsg.SetVarA(var_a)




class DeviceCan:
    """
    
    """
    def __init__(self, bustype='', channel='', bitrate=0):
        self.bustype = str(bustype)
        self.channel = str(channel)
        self.bitrate = int(bitrate)
        ChassisBaseMsg._init()
        self.canport = can.interface.Bus(bustype=self.bustype,
                                         channel=self.channel,
                                         bitrate=self.bitrate)

        # with self.canport as server:
        with can.interface.Bus(bustype=self.bustype,
                               channel=self.channel,
                               bitrate=self.bitrate) as client:
            # stop_event = threading.Event()
            t_receive = threading.Thread(target=self.EnableAsynsCan)
            t_receive.start()
            # self.EnableAsynsCan(client)

            try:
                while (ChassisBaseMsg.GetLen() < 53):
                    self.msg = Message(
                        arbitration_id=ChassisBaseMsg.CanID.VERSION_REQUEST_ID,
                        data=[0x01],
                        is_extended_id=False)
                    self.CanSend(self.msg)
                    time.sleep(0.1)

            except (KeyboardInterrupt, SystemExit):
                pass
            # stop_event.set()
            time.sleep(0.5)

    async def CanReceive(self, bus, stop_event):
        """The loop for receiving."""
        print("Start receiving messages")
        SlectMsg = CanMsgsGet()
        while not stop_event.is_set():

            self.rx_msg = await bus.recv(0.002)
            if self.rx_msg is not None:
                SlectMsg.CanMsgsProcess(self.rx_msg)
                print("rx: {}".format(self.rx_msg))

        await bus.recv()
        print("Stopped receiving messages")
        if stop_event.is_set() == False:
            stop_event.set()

    def CanGet(self):
        self.canport = can.ThreadSafeBus(interface=self.bustype,
                                         channel=self.channel,
                                         bitrate=self.bitrate)

        msg = self.canport.recv(0.002)
        print(msg)
        return msg

    def EnableAsynsCan(self):

        LOOP = asyncio.new_event_loop()
        asyncio.set_event_loop(LOOP)
        # Run until main coroutine finishes
        LOOP.run_until_complete(self.AsynsCan())

    def print_message(self, msg):
        SlectMsg = CanMsgsGet()
        SlectMsg.CanMsgsProcess(msg)

    async def AsynsCan(self):
        bus = can.Bus(interface=self.bustype,
                      channel=self.channel,
                      bitrate=self.bitrate)

        reader = can.BufferedReader()
        logger = can.Logger('logfile.asc')
        listeners = [
            self.print_message,
            reader,  # AsyncBufferedReader() listener
            logger  # Regular Listener object
        ]
        loop = asyncio.get_event_loop()
        notifier = can.Notifier(bus, listeners, loop=loop)
        while 1:
            msg = reader.get_message()
            await asyncio.sleep(0.2)

        notifier.stop()

    def CanDataUpdate(self):
        msg = self.CanGet()
        SlectMsg = CanMsgsGet()
        if msg is None:
            print('time occerred,no message')
        else:

            SlectMsg.CanMsgsProcess(msg)

    def CanSend(self, msg):

        self.canport = can.ThreadSafeBus(interface=self.bustype,
                                         channel=self.channel,
                                         bitrate=self.bitrate)
        with self.canport as bus:
            try:
                bus.send(msg)
            except can.CanError:
                print("Message NOT sent")


class UGVCan:
    def __init__(self, bustype=None, channel=None, bitrate=None):
        can_device_kwargs = {}
        if bitrate is None:
            can_device_kwargs['bitrate'] = 500000
        else:
            can_device_kwargs['bitrate'] = bitrate

        if bustype is None:
            can_device_kwargs['bustype'] = "socketcan"
        else:
            can_device_kwargs['bustype'] = bustype

        if channel is None:
            can_device_kwargs['channel'] = "can0"
        else:
            default_channel = channel
            can_device_kwargs['channel'] = default_channel

        self.candevice = DeviceCan(**can_device_kwargs)

    def Get(self):
        return self.candevice.CanGet()

    def Send(self, msg):
        self.candevice.CanSend(msg)


class UGV:
    """
        EnableCanCtrl()
        SendVersionRequest()
        SendErrorClearByte()
        EnableLightCtrl()
        DisableLightCtrl()
        LightFrontMode()
        SendSpeedAngular()
        SendSpeed()
        SendAngular()

        GetLightMode()        
        GetSysVersion()
        GetLeftWheel()
        GetRightWheel()
        GetLinerVelocity()
        GetAngularVelocity()
        GetErrorCode()
    
    """
    def __init__(self, *device_args, **device_kwargs):
        self.device = None
        can_device_init_fn = UGVCan.__init__
        args_names = can_device_init_fn.__code__.co_varnames[:
                                                             can_device_init_fn
                                                             .__code__.
                                                             co_argcount]
        args_dict = dict(zip(args_names, device_args))
        args_dict.update(device_kwargs)

        self.device = UGVCan(**args_dict)

    ChassisBaseMsg._init()

    def SendMsg(self, msg):
        self.device.Send(msg)

    def GetMsg(self):
        return self.device.Get()

    def SendVersionRequest(self):
        """
        Version Information Request
        """
        self.msg = Message(
            arbitration_id=ChassisBaseMsg.CanID.VERSION_REQUEST_ID,
            data=[0x01],
            is_extended_id=False)
        self.SendMsg(self.msg)

    def EnableCanCtrl(self):
        """
        控制底盘处于Can控制模式，需将遥控SWB拨到最上方
        Control the chassis in Can control mode, you need to dial the remote control SWB to the top
        """
        self.msg = Message(
            arbitration_id=ChassisBaseMsg.CanID.CTRL_MODE_CONFIG_ID,
            data=[0x01],
            is_extended_id=False)
        self.SendMsg(self.msg)

    def SendErrorClearByte(self, clear_byte):
        """
        clear the chassis motro error 

        clear_byte:0-4
            0 clear all 
            1 only clear motro1
            2 only clear motro2
            3 only clear motro3
            4 only clear motro4
        """
        if clear_byte > 4 | clear_byte < 0:
            clear_byte = 0
        else:
            pass
        self.msg = can.Message(
            arbitration_id=ChassisBaseMsg.CanID.STATE_RESET_CONFIG_ID,
            data=[clear_byte],
            is_extended_id=False)
        self.SendMsg(self.msg)

    def EnableLightCtrl(self):
        """
        Enable light control
        """
        get_data = ChassisBaseMsg.GetLightCmdCtrl()
        if (get_data != None):
            set_data = ((get_data) | 1)
            ChassisBaseMsg.SetLightCmdCtrl(set_data)

            self.msg = Message(
                arbitration_id=ChassisBaseMsg.CanID.LIGHT_COMMAND_ID,
                data=[
                    ChassisBaseMsg.GetLightCmdCtrl(),
                    ChassisBaseMsg.GetFrontMode(),
                    ChassisBaseMsg.GetFrontCustom()
                ],
                is_extended_id=False)

            self.SendMsg(self.msg)

    def DisableLightCtrl(self):
        """
         Disable light control
        """
        data = ChassisBaseMsg.GetLightCmdCtrl()
        data = data & 0xfe
        ChassisBaseMsg.SetLightCmdCtrl(data)
        self.msg = Message(
            arbitration_id=ChassisBaseMsg.CanID.LIGHT_COMMAND_ID,
            data=[
                ChassisBaseMsg.GetLightCmdCtrl(),
                ChassisBaseMsg.GetFrontMode(),
                ChassisBaseMsg.GetFrontCustom(),
            ],
            is_extended_id=False)
        self.SendMsg(self.msg)

    def LightFrontMode(self, mode, bright):
        """
        mode:0 Often shut
        mode:1 Normally open
        mode:2 Breathing lamp
        mode:3 Custom
        bright:        0-100       Note：Must be in mode 3
        """
        if bright != None:
            if mode == 0x03:
                ChassisBaseMsg.SetFrontCustom(bright)
            else:
                print("please in mode 3")

        self.msg = Message(
            arbitration_id=ChassisBaseMsg.CanID.LIGHT_COMMAND_ID,
            data=[
                ChassisBaseMsg.GetLightCmdCtrl(),
                ChassisBaseMsg.GetFrontMode(),
                ChassisBaseMsg.GetFrontCustom()
            ],
            is_extended_id=False)
        self.SendMsg(self.msg)

    def SendSpeedAngular(self, speed, angular):
        """
        send speed and angular data to chassis
        speed :-3~3 m/s
        angular:-2.523~2.523  rad/s
        """
        if (((speed * 1000) > 3000) | ((speed * 1000) < -3000) |
            (speed == None)):
            speed = 0
            print('Speed must be between -3 and 3m/s ')
        if (((angular * 1000) > 2523) | ((angular * 1000) < -2523) |
            (angular == None)):
            angular = 0
            print('Angular must be between -2.523 and 2.523 rad/s ')

        msg = Message(arbitration_id=ChassisBaseMsg.CanID.MOTION_COMMAND_ID,
                      data=[(int(speed * 1000)) >> 8 & 0xff,
                            (int(speed * 1000)) & 0xff,
                            (int(angular * 1000)) >> 8 & 0xff,
                            (int(angular * 1000) )& 0xff],
                      is_extended_id=False)
        self.SendMsg(msg)
        

    def SendSpeed(self, speed):
        """
        send speed  data to chassis
        speed :-3000~3000 mm/s
    
        """
        ChassisBaseMsg.SetLinearVelocity(speed)

        msg = Message(arbitration_id=ChassisBaseMsg.CanID.MOTION_COMMAND_ID,
                      data=[
                          (int(speed * 1000) >> 8) & 0xff,
                          int(speed * 1000) & 0xff,
                      ],
                      is_extended_id=False)
        self.SendMsg(msg)

    def SendAngular(self, angular):
        """
        send  angular data to chassis
        speed :-3000~3000 mm/s
        """
        ChassisBaseMsg.SetLinearVelocity(angular)

        msg = Message(arbitration_id=ChassisBaseMsg.CanID.MOTION_COMMAND_ID,
                      data=[
                          0, 0, (int(angular * 1000) >> 8) & 0xff,
                          int(angular * 1000) & 0xff
                      ],
                      is_extended_id=False)
        self.SendMsg(msg)

    # def  MotionCommand(self,msg):
    #     if (msg.id == 0X111):
    #         can.Message.arbitration_id=0X111
    #         msg = can.Message(arbitration_id=0x421, data=[0x01], is_extended_id=False)

    #         SendOne(msg)
    #     else:print("command_id is err")

    # def  BrakingCommand(self,msg):
    #     if (msg.id == 0X131):
    #         can.Message.arbitration_id=msg.id
    #         can.Message.data=msg.data
    #         SendOne(can.Message)
    #     else:print("command_id is err")

    # def  MotionCommand(self,msg):
    #     if (msg.id == 0X141):
    #         can.Message.arbitration_id=msg.id
    #         can.Message.data=msg.data
    #         SendOne(can.Message)
    #     else:print("command_id is err")

    def GetLightMode(self):
        return (ChassisBaseMsg.GetLightCmdCtrl(),
                ChassisBaseMsg.GetFrontMode(), ChassisBaseMsg.GetFrontCustom())

    def GetSysVersion(self):
        self.SendVersionRequest()
        return (ChassisBaseMsg.GetControlHardwareVersion(),
                ChassisBaseMsg.GetActuarorHardwareVersion(),
                ChassisBaseMsg.GetControlSoftwareVersion(),
                ChassisBaseMsg.GetActuarorSoftwareVersion())

    def GetLeftWheel(self):
        return ChassisBaseMsg.GetLeftWheel()

    def GetRightWheel(self):
        return ChassisBaseMsg.GetRightWheel()

    def GetLinerVelocity(self):
        return ChassisBaseMsg.GetLinearVelocity()

    def GetAngularVelocity(self):
        return ChassisBaseMsg.GetAngularVelocity()

    def GetErrorCode(self):
        return ChassisBaseMsg.GetErrorCode()


# if __name__ == "__main__":
#     # ScoutMiniCan(channel='can0')
#     # def __init__(self,channel=None, bustype=None, bitrate=None):
#     #     can_device_kwargs={}
#     #     if channel is None:
#     #         can_device_kwargs['bitrate'] =500000

#     #     if bustype is None:
#     #         can_device_kwargs['bustype']="socketcan"

#     #     if channel is None:
#     #         can_device_kwargs['channel']="can0"

#     #     self.candevice=DeviceCan(**can_device_kwargs)
#     # bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=500000)
#     #  config_msg.global_var()

#     # ChassisBaseMsg._init()

#     # ChassisBaseMsg.SetValue('name',1000)
#     MINI=ScoutMini(bustype='socketcan',channel='can0',bitrate=500000)
#     # scoutcan=DeviceCan(channel='can0',bustype='socketcan',bitrate=500000)
#     # scoutsend=DeviceCan.CanSend
#     a=CanMsgsGet()
#     b=CanMsgsSend()

#     num=500
#     while(num):
#         num-=1

#         MINI.GetMsg()
#         # a.ArrayGet()

#     while(1):
#         # a.ArrayGet()
#         MINI.GetMsg()

#         MINI.EnableCanCtrl()
#         MINI.EnableLightCtrl()
#         MINI.SendSpeedAngular(1,1)
