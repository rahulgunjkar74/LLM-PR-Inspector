def format_comment(review: str, filename: str) -> str:
    return f"""
## 🤖 LLM-PR-Inspector — AI Code Review

**File:** `{filename}`

---

{review}

---

### 📝 Note
This review was generated automatically by **LLM-PR-Inspector** using Groq Llama models.
Please verify critical suggestions before merging.
"""
