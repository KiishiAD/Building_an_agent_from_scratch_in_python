import os

list_tool = {"type": "function",
             "function":{
                 "name": "list_tool",
                 "description": "Lists the content of a directory or returns the contents of the present working directory if no path is provided.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "file_path": {
                                "type": "string",
                                "description": "The path to the directory to be listed. If not provided, the present working directory will be listed."
                            }
                        },
                        "required": []
                    }
             }}



def list_directory(file_path: str = None):
    """"Lists the content of a directory or returns the contents of the 
    present working directory if no path is provided."""

    if not file_path:
        file_path = os.getcwd()

    if os.path.isdir(file_path):
        try:
            return os.listdir(file_path)
        except Exception as e:
            return f"Error listing directory: {e}"

