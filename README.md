# Gemma-2B Empathy LoRA Adapter

This repository documents the fine-tuning of an **empathetic conversational language model** using **LoRA (Low-Rank Adaptation)** on top of the `google/gemma-2-2b-it` base model.

The objective is to improve **emotional awareness, validation, and supportive response style** for mental-health–related conversations while remaining computationally efficient and ethically responsible.

**LoRA adapter on Hugging Face:**
https://huggingface.co/KARTIK008/gemma-2b-empathy-lora

---

## 🧠 Project Overview

Large Language Models can be strong at reasoning yet weak at emotional sensitivity in conversations involving stress, anxiety, or distress. This project focuses on **behavioral fine-tuning**, not knowledge acquisition.

**Goals**
- Improve empathetic tone and emotional validation
- Preserve base model intelligence and reasoning
- Avoid authoritative or diagnostic language
- Keep the model lightweight and reusable

This is achieved with **parameter-efficient fine-tuning** rather than full model training.

---

## 🧩 Base Model

- **Model:** `google/gemma-2-2b-it`
- **Type:** Instruction-tuned LLM
- **Why Gemma-2B:**
  - Strong conversational baseline
  - Small enough for modest GPU resources
  - Well supported by the Hugging Face ecosystem

The base model weights are **not redistributed** in this repository.

---

## 🔧 Fine-Tuning Method (LoRA)

This project uses **LoRA via the PEFT framework**:
- Freezes all base model parameters
- Injects trainable low-rank matrices into attention layers
- Updates only ~0.12% of total parameters

**Benefits**
- Efficient training on a single GPU
- Reduced overfitting risk
- Preservation of base model capabilities

---

## 📊 Datasets Used

Two public datasets were combined to balance conversational realism and professional tone.

### 1) Empathetic Dialogues
- Source: https://huggingface.co/datasets/Estwld/empathetic_dialogues_llm
- Contribution:
  - Emotional grounding
  - Natural multi-turn dialogue
  - Emotion-aware responses

### 2) CounselChat
- Source: https://huggingface.co/datasets/nbertagnolli/counsel-chat
- Contribution:
  - Therapist-style responses
  - Validation-first language
  - Calm and non-judgmental tone

Approximately **12,000 processed dialogue pairs** were used in total.

No dataset files are redistributed. Details are documented in `Data/data_description.md`.

---

## ⚙️ Training Summary

- Fine-tuning type: Supervised Fine-Tuning (SFT)
- Method: PEFT / LoRA
- Epochs: 2
- Learning rate: 2e-4
- Effective batch size: 16 (via gradient accumulation)
- Optimizer: AdamW
- Quantization: 4-bit loading
- Hardware: Single Tesla T4-class GPU

Training converged stably with a final loss of approximately **2.14**, indicating effective behavioral adaptation without overfitting.

---

## 🧪 Inference

Example script: `Inference/inference.py`

Run locally:

```bash
python inference.py
```

The script:
- Loads the base model
- Attaches the LoRA adapter from Hugging Face
- Enforces a single, empathetic assistant response per input

---

## 🧠 Intended Use

This model is intended for:
- Empathetic conversational agents
- Mental-health support tools (non-clinical)
- Reflection, validation, and emotional support
- Research and educational purposes

## 🚫 Not Intended For

This model must not be used for:
- Medical or psychological diagnosis
- Crisis or suicide intervention
- Emergency decision-making
- Replacing licensed mental health professionals

Safety checks, moderation, and escalation logic must be implemented at the application level.

---

## ⚠️ Limitations & Safety

- The model does not have real emotional understanding
- It may generate verbose or repetitive responses
- It may fail in high-risk or crisis scenarios
- It should not be relied upon for authoritative guidance

Responsible deployment is the responsibility of the user.

---

## 📁 Repository Structure

```
.
├── finetuning/
│   └── gemmaemp.ipynb          # Training notebook
├── Inference/
│   └── inference.py            # Inference script
├── Data/
│   └── data_description.md     # Dataset documentation
├── Notes/
│   └── design_decisions.md     # Design rationale
└── README.md
```

---

## 📜 License & Credits

- LoRA adapter and code: MIT License
- Base model and datasets: original licenses apply

**Credits**
- Google for the Gemma model
- Hugging Face for the PEFT ecosystem
- Dataset contributors for Empathetic Dialogues and CounselChat