from typing import Dict

import logging

import openai


level = logging.INFO
logging.basicConfig(level=level)
logger = logging.getLogger(__name__)


def set_api_key(key) -> None:
    '''set OpenAI API key'''
    openai.api_key = key


class GPT3Generator:
    def __init__(self,
                 input_text: str = 'Input',
                 output_text: str = 'Output') -> None:
        '''Wrapper for simplifying priming
        see https://beta.openai.com/docs/api-reference for documentation
        '''
        self.input_text = input_text
        self.output_text = output_text
        self.instructions: str = ''
        self.examples: Dict[str, str] = {}
        self.full_prompt: str = ''

    def set_instructions(self, instructions: str) -> None:
        '''Set instructions for language generation (followed by examples)

        Parameters:
        -----------
        instructions (str): priming instructions
        '''
        if self.instructions != '':
            logger.warning('Previous instructions overwritten.')
        self.instructions = instructions + '\n\n'

    def add_example(self, input: str, output: str) -> None:
        '''Add an example to the primed prompt

        Parameters:
        -----------
        input (str): input text in example

        output (str): output text in example
        '''
        if input in self.examples:
            logger.warning(f'Example already exists. This will create duplicate examples in the prompt.')
        else:
            self.examples[input] = output

    def remove_example(self, input: str) -> None:
        '''Removes an example'''
        try:
            del self.examples[input]
        except KeyError:
            logger.warning(f'Example {input} not found in existing examples.')

    def get_prompt(self) -> str:
        '''Returns the prompt used for language generation'''
        expanded_examples = '\n\n'.join([f'{self.input_text}: {k}\n{self.output_text}: {v}' for k, v in self.examples.items()])
        return f'{self.instructions}{expanded_examples}'

    def get_gpt3_response(self, starting_text: str, **kwargs) -> openai.openai_response:
        '''Call OpenAI API to get the prompt'''
        if self.examples:
            starting_text = f'\n\n{self.input_text}: {starting_text}\n'
        self.full_prompt = self.get_prompt() + starting_text

        try:
            if self.examples and 'stop' not in kwargs:
                return openai.Completion.create(prompt=self.full_prompt, stop=f'{self.input_text}:', **kwargs)
            else:
                return openai.Completion.create(prompt=self.full_prompt, **kwargs)
        except openai.error.AuthenticationError:
            raise Exception('Unable to authenticate: use set_api_key() to set OpenAI key.')

    def generate(self, prompt: str, **kwargs) -> Dict[str, str]:
        '''Get generated text'''
        gpt3_response = self.get_gpt3_response(prompt, **kwargs)
        generated_text = gpt3_response['choices'][0]['text'].strip()
        return {
            'generated_text': generated_text,
            'full_prompt': self.full_prompt
        }
