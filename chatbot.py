from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class Chatbot:
    def __init__(self, model_name="microsoft/DialoGPT-medium"):
        print("Loading the chatbot model. This may take a few seconds...")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.model.config.pad_token_id = self.tokenizer.eos_token_id 
        self.chat_history_ids = None

    def chat(self):
        print("Chatbot is ready! Type 'exit' to end the conversation.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Chatbot: Goodbye! Have a great day!")
                break

            # Encode the user input and append to the chat history
            new_input_ids = self.tokenizer.encode(user_input + self.tokenizer.eos_token, return_tensors="pt")
            self.chat_history_ids = (
                new_input_ids if self.chat_history_ids is None else torch.cat([self.chat_history_ids, new_input_ids], dim=-1)
            )

            # Generate a response with attention_mask
            attention_mask = torch.ones(self.chat_history_ids.shape, dtype=torch.long)
            response_ids = self.model.generate(
                self.chat_history_ids,
                attention_mask=attention_mask,  # Pass attention_mask
                max_length=1000,
                pad_token_id=self.tokenizer.eos_token_id,
                top_p=0.92,
                top_k=50,
                temperature=0.7,
                do_sample=True,
            )

            # Decode and print the response
            response = self.tokenizer.decode(response_ids[:, self.chat_history_ids.shape[-1]:][0], skip_special_tokens=True)
            print(f"Chatbot: {response}")

            # Update the chat history
            self.chat_history_ids = response_ids


if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.chat()