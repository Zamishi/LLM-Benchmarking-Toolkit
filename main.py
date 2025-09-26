from PyQt5 import QtWidgets
from overlay import OverlayWindow
from llm_benchmark import LLMBenchmark

def main():
    app = QtWidgets.QApplication([])
    overlay = OverlayWindow(title="LLM Benchmarking Interface")
    benchmark = LLMBenchmark(overlay, use_gemini=True, use_openai=True)
    overlay.show()
    app.exec_()

if __name__ == "__main__":
    main()
