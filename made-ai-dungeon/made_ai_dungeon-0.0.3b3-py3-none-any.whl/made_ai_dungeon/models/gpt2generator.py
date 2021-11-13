import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel


class GPTGenerator:
    def __init__(self, model_path: str, max_len: int = 60, max_context_len: int = 1024):
        self.max_len = max_len
        self.max_context_len = max_context_len
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.device = 'cpu'
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_path)
        self.model = GPT2LMHeadModel.from_pretrained(model_path).to(self.device)
        self.model.eval()

    def get_context_tokens(self, input_text):
        context_tokens = self.tokenizer.encode(input_text, add_special_tokens=False, return_tensors="pt").to(
            self.device)
        context_tokens[0] = context_tokens[0][-self.max_context_len:]
        return context_tokens

    @staticmethod
    def prettify_output(text):
        punto = text.rfind('.')
        if punto > 3:
            return text[:punto + 1]
        return text

    def generate_text(self, input_text: str) -> str:
        context_tokens = self.get_context_tokens(input_text)
        generated_tokens = self.model.generate(context_tokens, do_sample=True,
                                               max_length=self.max_len,
                                               top_k=50)
        generated_new_tokens = generated_tokens.cpu().tolist()[0][len(context_tokens[0]):]
        generated_text = self.tokenizer.decode(generated_new_tokens,
                                               clean_up_tokenization_spaces=False,
                                               skip_special_tokens=True)
        generated_text = self.prettify_output(generated_text)
        return generated_text
