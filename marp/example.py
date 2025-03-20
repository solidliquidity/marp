from marp.marp import PythonMarp

# Example usage
marp_presentation = PythonMarp(theme="night", classes=["invert", "lead"])
marp_presentation.add_slide("SolidLiquidity", "TL;DR")
marp_presentation.add_slide("Conclusion", "- Thank you for your time\n- Questions?")

marp_presentation.generate_presentation()
