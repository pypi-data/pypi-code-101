from verkefni.task import Task


class SumOfSquares:
    def __init__(self, send_task, input_values):
        self.send_task = send_task
        self.input_values = input_values
        self.squares = dict()
        self.result = None

    def start(self):
        for i, v in enumerate(self.input_values):
            task_id = f'sos-0-{i}'
            self.send_task(Task(id=task_id, function='arithmetic.square',
                                input_data=v))

    def on_result(self, result):
        match result['id'].split('-'):
            case ['sos', '0', i]:
                self.squares[int(i)] = result['output_data']
                if len(self.squares) == len(self.input_values):
                    self.send_task(
                            Task(id='sos-1-0',
                                 function='arithmetic.sum',
                                 input_data=[self.squares[n] for n
                                             in range(len(self.squares))]))
            case ['sos', '1', '0']:
                self.result = result['output_data']

    def is_complete(self):
        return self.result is not None


class WordCount:
    def __init__(self, send_task, text):
        self.send_task = send_task
        self.text = text
        self.wc_by_line = dict()
        self.sorted_lines = dict()
        self.pending_tasks = set()

    def is_complete(self):
        return not self.pending_tasks

    def start(self):
        for i, line in enumerate(self.text.split('\n')):
            task_id = f'wc-{i}'
            self.send_task(Task(id=task_id, function='lexical.wordcount',
                                input_data=line))
            self.pending_tasks.add(task_id)
            task_id = f's-{i}'
            self.send_task(Task(id=task_id, function='lexical.sort',
                                input_data=line))
            self.pending_tasks.add(task_id)

    def on_result(self, result):
        if result['id'] in self.pending_tasks:
            match result['id'].split('-'):
                case ['wc', i]:
                    self.wc_by_line[int(i)] = result['output_data']
                case ['s', i]:
                    self.sorted_lines[int(i)] = result['output_data']
            self.pending_tasks.remove(result['id'])
