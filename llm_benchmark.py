import logging
from ocr_utils import capture_screen, ocr_image
from sympy_utils import solve_expression
from gemini_solver import ask_gemini
from openai_solver import ask_openai

class LLMBenchmark:
    def __init__(self, overlay, use_gemini=True, use_openai=True):
        self.overlay = overlay
        self.use_gemini = use_gemini
        self.use_openai = use_openai

    def capture_and_evaluate(self, region=None):
        img = capture_screen(region)
        text = ocr_image(img)
        results = {}

        if self.use_gemini:
            try:
                results["Gemini"] = ask_gemini(text)
            except Exception as e:
                results["Gemini"] = f"Error: {e}"

        if self.use_openai:
            try:
                results["OpenAI"] = ask_openai(text)
            except Exception as e:
                results["OpenAI"] = f"Error: {e}"

        math_solution = solve_expression(text)
        if math_solution:
            results["SymPy"] = math_solution

        self.overlay.update_text_signal.emit(str(results))
        return results
