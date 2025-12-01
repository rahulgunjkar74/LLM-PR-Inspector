from groq import Groq
from config import GROQ_API_KEY, MODEL

client = Groq(api_key=GROQ_API_KEY)

def review_code_patch(filename, patch):
    prompt = f"""
You are an expert GitHub Pull Request reviewer.

Analyze the following patch in the file: **{filename}**

PATCH:
{patch}

Provide the review in the following structured Markdown format:

### 1. Summary
Explain what the patch changes and the intention behind it.

### 2. Potential Bugs
List any possible bugs or logical issues introduced by the patch.

### 3. Code Smells
Identify bad patterns, duplication, unnecessary steps, or poor naming.

### 4. Optimization Suggestions
Recommend performance improvements and cleaner alternatives.

### 5. Security Issues
Mention any potential vulnerabilities or unsafe logic.

### 6. Line-by-Line Review
For each changed line:
- Mark it as **OK**, **Needs Improvement**, or **Risky**
- Provide a short explanation

### 7. Risk Score (0–10)
Provide a numeric risk score and clear explanation:
0 = Completely safe  
10 = Highly risky change likely to break behavior

### 8. Final Decision
Select only one:
- **APPROVE**
- **REQUEST CHANGES**
- **NEEDS DISCUSSION**

### 9. Short Final Comment (1–2 lines)
A small summary view of the PR quality.

Make the output clean, readable, and in proper Markdown format.
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    return response.choices[0].message.content
