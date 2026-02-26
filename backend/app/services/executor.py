import matplotlib.pyplot as plt
import base64
from io import BytesIO
from app.services.data_loader import DataLoader
import pandas as pd

def execute_code(code: str):
    df = DataLoader.get_dataframe()

    local_vars = {
        "df": df,
        "plt": plt
    }

    try:
        print("Generated Code:\n", code)
        if "read_csv" in code or "import pandas" in code:
            return {
        "answer": "Execution Error: Direct file loading is not allowed.",
        "image": None
    }
        # Remove markdown code fences
        if "```" in code:
            code = code.split("```")[1]
            code = code.replace("python", "").strip()
        exec(code, {}, local_vars)

        result = local_vars.get("result", None)

        if isinstance(result, (pd.Series, pd.DataFrame)):
            result = "\n".join([f"{k}: {v}" for k, v in result.items()])

# If result is a tuple (like from plt.hist), ignore it
        if isinstance(result, tuple):
            result = None

# Clean float formatting
        if isinstance(result, float):
            result = round(result, 2)

        image_base64 = None
        if plt.get_fignums():
            buffer = BytesIO()
            plt.savefig(buffer, format="png")
            buffer.seek(0)
            image_base64 = base64.b64encode(buffer.read()).decode("utf-8")
            buffer.close()
            plt.close()
            result = None

        return {
            "answer": str(result) if result else "Done.",
            "image": image_base64
        }

    except Exception as e:
        return {
            "answer": f"Execution Error: {str(e)}",
            "image": None

        }

