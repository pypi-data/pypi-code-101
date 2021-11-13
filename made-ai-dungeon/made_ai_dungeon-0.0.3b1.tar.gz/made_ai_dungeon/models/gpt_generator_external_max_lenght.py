import torch
import time
from transformers import GPT2Tokenizer, GPT2LMHeadModel, AutoTokenizer
from typing import Any, Tuple

MODEL_CLASSES = {
    "gpt2": (GPT2LMHeadModel, GPT2Tokenizer),
}
model_class, tokenizer_class = MODEL_CLASSES["gpt2"]

class GPTGenerator:
    def __init__(self, model_path: str, seq_len=20):
        self.seq_len = seq_len
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.device = 'cpu'
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = model_class.from_pretrained(model_path).to(self.device)
        self.model.eval()
    
    def get_context_tokens(self, input_text, context, max_context_len=1024):
        all_text = input_text + "/n" + context 
        context_tokens = self.tokenizer.encode(all_text, add_special_tokens=False, return_tensors="pt")
        if len(context_tokens[0]) > max_context_len:
            context_tokens[0] = context_tokens[0][-max_context_len:]
        return context_tokens

    @staticmethod
    def prettify_output(text):
        punto = text.rfind('.')
        return text[:punto + 1]
    
    def generate_text(self, input_text: str, context: Any, max_len: int) -> Tuple[str, Any]:
        if not isinstance(context, str):
            raise NotImplementedError("Only strings plz")
        context_tokens = self.get_context_tokens(input_text, context)
        generated_tokens = self.model.generate(context_tokens, do_sample=True,
                                               max_length=max_len,
                                               top_k=50)
        generated_new_tokens = generated_tokens.tolist()[0][len(context_tokens[0]):]
        generated_text = self.tokenizer.decode(generated_new_tokens,
                                               clean_up_tokenization_spaces=False,
                                               skip_special_tokens=True)
        generated_text = self.prettify_output(generated_text)
        return generated_text, input_text + "\n" + context + "\n"  + generated_text
