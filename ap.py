import gradio as gr
import os
def upload_file(file):
    if file:
        name = os.path.basename(file.name)
        upload_dir = "files"  # Specify the directory where uploaded files will be stored
        file_location = f"{upload_dir}/{name}"
        # Do something with the file location (e.g., process, analyze, or save it)
        with open(file_location, "wb") as f:
            f.write(file.read())
        return "File uploaded successfully!"
    else:
        return "No file uploaded."

iface = gr.Interface(
    fn=upload_file,
    inputs="file",
    outputs="text",
    title="Video Editing & Manipulation Tool using AI",
    description="Upload a file and get its location.",
    allow_flagging=False,
    live=True,
    file_upload_dir=r"C:\Users\gaura\Desktop\Vool2024\Vool\files"
)

if __name__ == "__main__":
    iface.launch(share=True)
