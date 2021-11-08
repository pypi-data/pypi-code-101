from cube_plugin_async_w_kafka.Networkplane.Network_Plane import Network_Plane
from cube_plugin_async_w_kafka.Networkplane.Exceptions import ConnectionError, InterfaceAttachFailed, NetworkPlaneFailure
from confluent_kafka import Producer

import queue
import logging

from multiprocessing import Process, Queue



"""
This network plane is assynchronious non transactional, it can send records with different TOPICS/KEYS while ensuring no duplication of messages and order delivery even during network failure
"""
class A_Network_Plane(Network_Plane):


    def __init__(self,network_plane_spec,to_be_connected_interfaces_spec):
        Network_Plane.__init__(self,network_plane_spec,to_be_connected_interfaces_spec)



    def start(self, timeout=10):
        """
        Starts the Network plane

        :param timeout:

            because of network jitters and communication quality:
                if timeout >= 0, NP will wait for that time (maximum) to discover topics and if it fails it will raise a NetworkPlaneFailure
                if timeout < 0, NP will wait indefinitely to discover all topics, it will start when discovery occurs

        :return:
        :raises: NetworkPlaneFailure
        """

        if not self._run_status.is_set():

            self._producer_config=self.get_producer_config(self._network_plane_spec)

            try:

                #wait to start for timeout, otherwise raise exception
                if timeout >= 0:

                    self.discover_topics(timeout)

                    self._run_status.set()
                    self._send_status.set()

                    self._burst_queue = Queue(self._network_plane_spec["buffering"]["burst-buffer-max-records"])
                    self._P_Live_Sync = Process(target=self._sync, args=(self._producer_config, self._burst_queue,self._address, self._send_status,self._task))
                    self._P_Live_Sync.start()

                    logging.getLogger(self._address).info("network plane is started")


                # wait to start when connection resumed, accept to receive messages, delivery will be done later
                else:

                    self._burst_queue = Queue(self._network_plane_spec["buffering"]["burst-buffer-max-records"])
                    self._P_Live_Sync = Process(target=self._sync, args=(self._producer_config, self._burst_queue,self._address, self._send_status,self._task))
                    self._P_Live_Sync.start()

                    logging.getLogger(self._address).warning(
                        "network plane will start automatically when connection with kafka cluster is up: "+self._producer_config['bootstrap.servers'])

                    #the system will block at this step until connection is established (topic are discovered)
                    self.discover_topics(-1)

                    self._run_status.set()
                    self._send_status.set()


            except ConnectionError as e:

                self._run_status.clear()
                self._send_status.clear()

                logging.getLogger(self._address).critical(
                        "network plane cannot start, no records will be accepted to be sent")

                raise NetworkPlaneFailure("network plane cannot start, no records will be accepted to be sent")



            except Exception as e:

                self._run_status.clear()
                self._send_status.clear()

                logging.getLogger(self._address).critical("unknown error, details: "+str(e))

                raise NetworkPlaneFailure("network plane cannot start, no records will be accepted to be sent")


        else:

            logging.getLogger(self._address).warning("network plane is already started or in starting process")


    def stop(self, timeout=None):
        """
        Stops the Network Plane
        :param timeout: time to wait to stop the sync thread
        :return:
        """

        if self._run_status.is_set():

            self._run_status.clear()

            if timeout is None:

                if not self._task.set("STOP", instructions={"timeout": None}):
                    pass


            else:
                if not self._task.set("STOP",instructions={"timeout": timeout}):
                    pass

            self._P_Live_Sync.join()

            self._send_status.clear()

            self._burst_queue.close()
            self._burst_queue.join_thread()

            logging.getLogger(self._address).info("network plane is closed with "+str(self._burst_queue.qsize())+" records in the queue")

            del self._P_Live_Sync

        else:
            logging.getLogger(self._address).warning("network plane is already closed or in closing process")


    def get_NetPort(self, interface_address):

        if interface_address in self._interfaces_status.keys():

            if self._interfaces_status[interface_address]["registered"] == True:

                self._interfaces_status[interface_address]["attached"] = True

                logging.getLogger(self._address).info(
                    "Attach succeeded: Interface " + str(interface_address) + " is attached to network plane " + str(
                        self._address))
                return self._burst_queue

            else:

                logging.getLogger(self._address).error(
                    "Attach Failed: Interface " + str(interface_address) + " is not registered, need to register first")
                raise InterfaceAttachFailed(
                    "Attach Failed: Interface " + str(interface_address) + " is not registered, need to register first")

        else:

            logging.getLogger(self._address).error(
                "Attach Failed: Interface " + str(interface_address) + " is not recognized by the network plane " + str(
                    self._address))
            raise InterfaceAttachFailed(
                "Attach Failed: Interface " + str(interface_address) + " is not recognized by the network plane " + str(
                    self._address))





    def _sync(self, __config, __burst_queue, __address, __send_status,__task):

        __producer = Producer(**__config, logger=logging.getLogger(__address))

        while True:

            # check if there is a task to do (update, close, ...)
            if not __task.to_do():

                try:

                    # wait for timeout, if no records after timeout: check for updates, otherwise: send that record and check next round
                    msg=__burst_queue.get(timeout=1000)

                    __producer.produce(topic=msg['topic'], key=msg['key'], value=msg['msg'], callback=self._on_delivery_callback)
                    __producer.poll(0)

                except queue.Empty:
                    pass

                #local queue is full : need to send messages in cache before start fetching new messages
                except BufferError as e:

                    __producer.poll(0)
                    __send_status.clear()
                    __timeout = 1

                    remaining_msg=__producer.flush(0)
                    b_percentage_msg_capacity=round((remaining_msg/__config['queue.buffering.max.messages'])*100,2)
                    b_kbytes_capacity=__config['queue.buffering.max.kbytes']

                    logging.getLogger(self._address).critical(
                        "Buffer bottleneck: " + str(
                        b_percentage_msg_capacity) + "% of its maximum record number ("+str(__config['queue.buffering.max.messages'])+"), maximum configured buffer size "+str(b_kbytes_capacity)+" kb)" + ", burst buffer contains: " + str(
                        __burst_queue.qsize()) + " records")

                    new_remaining_msg=remaining_msg

                    #loop until we start flushing
                    while new_remaining_msg >= remaining_msg:
                        new_remaining_msg=__producer.flush(__timeout)

                    __send_status.set()

                    b_percentage_msg_capacity = round(
                        (new_remaining_msg / __config['queue.buffering.max.messages']) * 100, 2)

                    logging.getLogger(self._address).critical(
                        "Buffer freed, network plane buffer capacity is " + str(
                            b_percentage_msg_capacity) + "% of its maximum record number, maximum configured buffer size is "+str(b_kbytes_capacity)+" kb" + ", burst buffer contains: " + str(
                            __burst_queue.qsize()) + " records")

                    #continue flashing the remaining records
                    __producer.flush()

                    #__producer.produce(topic=msg['topic'], key=msg['key'], value=msg['msg'], callback=self.on_delivery_callback)
                    #__producer.poll(0)

                except Exception as e:

                    __producer.poll(0)
                    __send_status.clear()

                    logging.getLogger(self._address).critical("Unknown delivery error: "+str(e))

            else:

                print("updating")

                task=__task.get_task()
                task_name=task["name"]
                task_instructions=task["instructions"]

                if task_name=="STOP":

                    logging.getLogger(self._address).warning("Interrupted for stopping task")
                    timeout=task_instructions["timeout"]

                    if timeout is not None:

                        if __producer.flush(timeout)==0:
                            __send_status.clear()
                            __task.success()

                            break
                        else:
                            __task.fail()

                    #wait until we flush all data
                    else:

                        __producer.flush()
                        __send_status.clear()
                        __task.success()

                elif task_name=="UPDATE_PRODUCER":

                    logging.getLogger(self._address).warning("Interrupted for producer update task")

                    #check the sending status prior to flush
                    if __send_status.is_set():

                        #flush remaining data
                        __producer.flush()

                        __saved_config=__config.copy()
                        for key, value in task_instructions.items():
                            __config[key]=value

                        try:

                            __producer = Producer(**__config, logger=logging.getLogger(__address))

                            __task.success()

                            del __saved_config

                            logging.getLogger(self._address).info(
                                        "Updates applied successfully, network plane updated with new instructions: " + str(
                                            task_instructions))

                                #config restore
                        except Exception as e:

                            logging.getLogger(self._address).error(
                                    "Updates application failed: producer encountered an error with the following configuration: "+str(__config)+", details: "+str(e))

                            __bad_config=__config
                            __config=__saved_config

                            __producer = Producer(**__config, logger=logging.getLogger(__address))

                            __task.fail()

                            logging.getLogger(self._address).info(
                                        "Undo updates: producer resumed successfully to last configuration: "+str(__config))

                            del __bad_config

                        #there is errors in sending, cannot update because cannot flush and create a new producer
                    else:

                            __task.fail()
                            logging.getLogger(self._address).error("Updates rejected: network plane is not working properly, need to establish a normal situation before proceeding with updates")

                else:

                    if task_name=="NONE":
                        __task.fail()
                        logging.getLogger(self._address).warning("Interruption ignored: no task mentioned")
                    else:
                        __task.fail()
                        logging.getLogger(self._address).warning("Interruption ignored: task "+task_name+" not identified")













