# Design Decisions and Rationale



## 1. Model Selection

**Chosen Model:** Gemma-2-2B-IT

**Rationale:**
- Instruction-tuned for conversational tasks
- Small enough to fine-tune on limited GPU resources
- Strong baseline language and reasoning capabilities
- Well-supported within the Hugging Face ecosystem

The instruction-tuned variant was selected to align with dialogue-based fine-tuning objectives.

---

## 2. Fine-Tuning Strategy

### Parameter-Efficient Fine-Tuning (PEFT) with LoRA

Instead of full fine-tuning, LoRA (Low-Rank Adaptation) was used via the PEFT framework.

**Reasons:**
- Full fine-tuning of a 2B+ parameter model is computationally expensive
- LoRA allows behavioral adaptation with minimal trainable parameters
- Reduces risk of overfitting
- Preserves base model knowledge

Approximately 0.12% of total model parameters were trainable during fine-tuning.

---

## 3. Target Behavior

The goal of fine-tuning was **behavioral adaptation**, not knowledge acquisition.

Specifically, the model was optimized to:
- Acknowledge user emotions before offering suggestions
- Use non-judgmental and supportive language
- Avoid authoritative or diagnostic statements
- Encourage reflection rather than instruction

---

## 4. Dataset Composition

Two datasets were intentionally combined to balance strengths:

- **Empathetic Dialogues:** emotional grounding and conversational realism
- **CounselChat:** professional mental health response structure

This combination reduces the risk of:
- Overly casual responses
- Overly clinical or rigid phrasing

---

## 5. Training Configuration Choices

Key training decisions included:
- Small per-device batch size to fit GPU memory
- Gradient accumulation to simulate larger effective batch size
- Relatively high learning rate suitable for LoRA
- Limited number of epochs (2) to avoid overfitting

Loss behavior was monitored to ensure stable convergence.

---

## 6. Evaluation Strategy

Evaluation focused primarily on:
- Training loss trends (stability and convergence)
- Qualitative inspection of generated responses
- Behavioral changes in tone and empathy

Formal automated metrics were intentionally deprioritized due to the subjective nature of empathy.

---

## 7. Safety and Scope Limitations

This model is not intended to:
- Provide medical or psychological diagnosis
- Replace professional mental health support
- Handle crisis or self-harm situations autonomously

Crisis detection and escalation are designed to be handled at the application level.

---

## 8. Deployment Considerations

The model is distributed as a LoRA adapter:
- Enables lightweight sharing
- Allows future re-training or merging
- Keeps base model intact

For environments such as WebLLM / WebGPU, the adapter must be merged into the base model before compilation.

---

## 9. Future Improvements

Potential future extensions include:
- Additional domain-specific data
- Incremental LoRA fine-tuning
- Structured response evaluation
- Hybrid client–server safety architectures
