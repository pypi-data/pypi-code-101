from json import loads, dumps
import verkefni.common


logger = verkefni.common.get_logger('worker')


def run(queue_name, work_fns):
    logger.info('Starting worker...')
    logger.info(f'Supported work functions: {list(work_fns.keys())}')
    with verkefni.common.connect() as conn:
        chan = conn.channel()
        chan.basic_qos(prefetch_count=2)
        work_q = verkefni.common.declare_work_queue(chan,
                                                    queue_name,
                                                    list(work_fns.keys()))

        def on_work(ch, method, properties, body):
            logger.info(f'on_work received: {body}, {properties}')
            work = loads(body.decode())
            try:
                if work['command'] == 'SHUTDOWN':
                    ch.basic_ack(delivery_tag=method.delivery_tag)
                    ch.stop_consuming()
                    return
            except KeyError:
                # not a command
                pass

            def progress(so_far, target):
                logger.info(
                        f'Progress({properties.reply_to}: {so_far}/{target}')
                ch.basic_publish(exchange='result',
                                 routing_key=properties.reply_to + '.progress',
                                 body=dumps(dict(so_far=so_far,
                                                 id=work['id'],
                                                 target=target)))
                pass

            result = dict(id=work['id'])
            result['output_data'] = work_fns[work['function']](
                    work['input_data'], progress)
            result = dumps(result)
            logger.info(f'Sending result: {result} to {properties.reply_to}')
            ch.basic_publish(exchange='result',
                             routing_key=properties.reply_to + '.result',
                             body=result)
            ch.basic_ack(delivery_tag=method.delivery_tag)

        logger.info('Subscribing to work todo...')
        chan.basic_consume(queue=work_q.method.queue,
                           on_message_callback=on_work)
        logger.info('Waiting for work...')
        chan.start_consuming()
