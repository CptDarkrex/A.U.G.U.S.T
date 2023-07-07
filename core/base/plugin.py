from transformers import AutoModelForCausalLM, AutoTokenizer


class Chatbot:
    def __init__(self, model_name):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

    def generate_response(self, input):
        input_ids = self.tokenizer.encode(input, return_tensors='pt')
        output_ids = self.model.generate(input_ids)
        output = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)
        return output
