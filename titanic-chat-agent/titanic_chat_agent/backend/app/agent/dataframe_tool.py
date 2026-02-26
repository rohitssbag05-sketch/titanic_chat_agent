import matplotlib.pyplot as plt
import base64
from io import BytesIO
from app.services.data_loader import DataLoader

def execute_code(code: str):
    df = DataLoader.get_dataframe()
    local_vars = {"df": df, "plt": plt}

    try:
        exec(code, {}, local_vars)

        result = local_vars.get("result", None)

        image_base64 = None
        if plt.get_fignums():
            buffer = BytesIO()
            plt.savefig(buffer, format="png")
            buffer.seek(0)
            image_base64 = base64.b64encode(buffer.read()).decode("utf-8")
            buffer.close()
            plt.close()

        return {
            "answer": str(result) if result else "Done.",
            "image": image_base64
        }

    except Exception as e:
        return {
            "answer": f"Execution Error: {str(e)}",
            "image": None
        }