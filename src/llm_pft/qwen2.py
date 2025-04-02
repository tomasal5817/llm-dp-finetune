from transformers import Qwen2Config

from .language_model import LanguageModel


class Qwen2(LanguageModel):
    """ A custom convenience wrapper around huggingface gpt-2 utils """

    def get_config(self):
        return Qwen2Config()