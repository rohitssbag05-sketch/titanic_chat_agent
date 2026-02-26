from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from app.config import settings
from app.services.data_loader import DataLoader

llm = ChatOllama(model=settings.MODEL_NAME, temperature=0)

def generate_code(question: str):

    df = DataLoader.get_dataframe()
    columns = list(df.columns)

    prompt = ChatPromptTemplate.from_template("""
You are a data analyst.

A pandas dataframe named 'df' is already loaded.

The dataframe columns are:
{columns}

IMPORTANT:
- Column names are case-sensitive.
- You MUST use exact column names from the list above.
- DO NOT load any CSV.
- DO NOT import pandas.
- DO NOT redefine df.
- Only use the provided dataframe 'df'.
                                              
If plotting:
- Use plt.figure(figsize=(8,5))
- Add plt.title()
- Add plt.xlabel()
- Add plt.ylabel()
- Add plt.grid(True)

Rules:
- Assign final answer to variable: result
- If plotting, use matplotlib via 'plt'
- Return ONLY valid Python code
- No explanation
- No markdown
- No comments
If the question asks for a numeric or text answer:
    Assign a clear human-readable sentence to variable `result`.
    Example:
    result = f"The average ticket fare on the Titanic was {{df['Fare'].mean():.2f}}."
                                              
Question:
{question}
""")

    chain = prompt | llm

    response = chain.invoke({
        "question": question,
        "columns": columns
    })

    return response.content.strip()