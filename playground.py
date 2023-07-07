import torch
from transformers import AutoTokenizer, LlamaForCausalLM


class August:
    def __init__(self):
        # Load pre-trained model and tokenizer
        self.model_name = 'TheBloke/vicuna-13B-1.1-HF'
        self.model = LlamaForCausalLM.from_pretrained(self.model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)

    def generate_conversation(self, context, prompt):
        # Set the model to evaluation mode
        self.model.eval()

        # Tokenize the context and prompt
        input_text = context + '\n' + prompt
        input_ids = self.tokenizer.encode(input_text, return_tensors='pt')

        # Generate response
        with torch.no_grad():
            output = self.model.generate(input_ids, max_length=100)

        # Decode the response
        response = self.tokenizer.decode(output[0], skip_special_tokens=True)

        # Split the response into a list of strings
        response_list = response.split('\n')

        return response_list


august = August()
# Example usage
context = ""
prompt = "User: write a python app that extracts the second string on a sentence\nAI:"
response = august.generate_conversation(context, prompt)
print(response)
