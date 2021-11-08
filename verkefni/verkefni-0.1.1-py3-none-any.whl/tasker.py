from json import dumps, loads
import pika
import verkefni.common


logger = verkefni.common.get_logger('tasker')


class Tasker:
    def __init__(self, id):
        self.conn = verkefni.common.connect()
        self.chan = self.conn.channel()
        self.tasker_id = id
        self.result_queue = self.chan.queue_declare(
                queue=f'results-{self.tasker_id}',
                durable=True,
                exclusive=True,
                auto_delete=True)
        self.chan.queue_bind(queue=self.result_queue.method.queue,
                             exchange='result',
                             routing_key=f'{self.tasker_id}.*.result')

    def send_task(self, task):
        logger.info(f'Sending task: {task}')
        self.chan.basic_publish(exchange='work',
                                routing_key=task.function,
                                body=dumps(dict(function=task.function,
                                                id=task.id,
                                                input_data=task.input_data)),
                                properties=pika.BasicProperties(
                                    delivery_mode=2,
                                    reply_to=f'{self.tasker_id}.{task.id}'))

    def run(self, on_result_handler):
        def on_result(ch, method, properties, body):
            logger.info(f'Result: {body}')
            result = loads(body.decode())
            on_result_handler(result)
            ch.basic_ack(delivery_tag=method.delivery_tag)

        self.chan.basic_consume(queue=self.result_queue.method.queue,
                                exclusive=True,
                                on_message_callback=on_result)
        logger.info('Waiting for result...')
        self.chan.start_consuming()

    def stop(self):
        self.chan.stop_consuming()
