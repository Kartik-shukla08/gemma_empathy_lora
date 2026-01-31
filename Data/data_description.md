# Dataset Description

This project uses a combination of two publicly available datasets to fine-tune an empathetic, mental-health–oriented language model. The datasets were selected to complement each other in terms of conversational style and emotional depth.

No raw or processed dataset files are redistributed in this repository. Instead, this document describes the datasets used, their sources, and how they were processed.

---

## 1. Empathetic Dialogues Dataset

**Source**  
https://huggingface.co/datasets/Estwld/empathetic_dialogues_llm

**Original Description**  
The Empathetic Dialogues dataset consists of conversational exchanges grounded in emotional situations. Each conversation is associated with:
- A short situational description
- An emotion label (e.g., anxious, sad, hopeful)
- A multi-turn dialogue between two participants

**Purpose in This Project**  
This dataset was used to teach the model:
- Emotional mirroring
- Context-aware follow-up questioning
- Natural conversational flow
- Sensitivity to a wide range of emotional states

**Processing Applied**
- Extracted user–assistant message pairs from multi-turn conversations
- Prepended emotion context to user messages to preserve emotional grounding
- Filtered and truncated messages to control sequence length
- Randomly sampled ~10,000 dialogue pairs to balance dataset size

---

## 2. CounselChat Dataset

**Source**  
https://huggingface.co/datasets/nbertagnolli/counsel-chat

**Original Description**  
The CounselChat dataset contains real-world mental health questions and answers, where responses are written by licensed or trained mental health professionals.

Each entry includes:
- A user-submitted mental health question
- One or more therapist responses
- Topic categorization and metadata

**Purpose in This Project**  
This dataset was used to teach the model:
- Professional and non-judgmental tone
- Validation-first response structure
- Calm and supportive language
- Avoidance of definitive diagnosis or commands

**Processing Applied**
- Selected question–answer text fields only
- Removed incomplete or null entries
- Preserved multiple answers for identical questions to maintain response diversity
- Truncated long responses to fit model context limits

---

## 3. Dataset Combination Strategy

The final training dataset was created by combining:
- ~2,600 processed CounselChat samples
- ~10,000 sampled Empathetic Dialogues pairs

This combination was intentional:
- CounselChat provides **professional therapeutic tone**
- Empathetic Dialogues provides **natural emotional conversation**

The merged dataset enables the model to learn empathetic behavior that is both emotionally sensitive and professionally framed.

---

## 4. Ethical Considerations

- All datasets are publicly available and used in accordance with their original licenses.
- No personally identifiable information (PII) was introduced.
- No attempt was made to train the model to provide diagnosis, treatment, or crisis intervention.
- Safety and crisis handling are enforced at the application level, not through training data.

---

## 5. Reproducibility

The combined dataset can be deterministically reconstructed by:
1. Downloading the original datasets from the links above
2. Running the preprocessing steps provided in `training/finetune.ipynb`

This approach ensures transparency and reproducibility without redistributing sensitive data.
