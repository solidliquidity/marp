import subprocess

def create_settings(theme="default", classes=None):
    classes_str = "\n  - " + "\n  - ".join(classes) if classes else ""
    
    return f"""---
marp: true
theme: {theme}
class:{classes_str}

"""

def create_slide(title, content, position=""):
    slide = f"""---
{'' if not position else f'style: {position}'}

# {title}

{content}


"""
    return slide

class PythonMarp:
    def __init__(self, theme="default", classes=None, output_file="marp_presentation.pdf"):
        self.settings = create_settings(theme, classes)
        self.slides = []
        self.output_file = output_file

    def add_slide(self, title, content, position=""):
        self.slides.append(create_slide(title, content, position))

    def generate_presentation(self):
        marp_content = self.settings + "\n".join(self.slides)

        with open(self.output_file, "wb") as f:
            process = subprocess.run(
                ["marp", "--pdf", "-"],  # Change to "--pptx" or "--html" if needed
                input=marp_content.encode(),
                stdout=f,
                stderr=subprocess.PIPE,
            )

        if process.returncode == 0:
            print(f"Presentation saved as: {self.output_file}")
        else:
            print("Error:", process.stderr.decode())


