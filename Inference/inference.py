import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

BASE_MODEL_ID = "google/gemma-2-2b-it"
LORA_PATH = "./gemma-empathy-lora"  # folder containing adapter files

def load_model():
    tokenizer = AutoTokenizer.from_pretrained(LORA_PATH)

    base_model = AutoModelForCausalLM.from_pretrained(
        BASE_MODEL_ID,
        torch_dtype=torch.float16,
        device_map="auto",
    )

    model = PeftModel.from_pretrained(base_model, LORA_PATH)
    model.eval()

    return model, tokenizer


def generate_response(model, tokenizer, user_input):
    prompt = (
        "You are an empathetic mental health support assistant.\n"
        "Respond in a single, calm, supportive message.\n\n"
        f"User: {user_input}\n"
        "Assistant:"
    )

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=200,
            temperature=0.7,
            do_sample=True,
            eos_token_id=tokenizer.eos_token_id,
        )

    text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Keep only first assistant response
    if "Assistant:" in text:
        text = text.split("Assistant:", 1)[1].strip()

    return text


if __name__ == "__main__":
    model, tokenizer = load_model()

    while True:
        user_input = input("\nUser: ")
        if user_input.lower() in {"exit", "quit"}:
            break

        response = generate_response(model, tokenizer, user_input)
        print(f"\nAssistant: {response}")
