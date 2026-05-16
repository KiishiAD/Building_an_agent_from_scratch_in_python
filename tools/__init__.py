from .read_file import read_tool, read_file
from .list_directory import list_tool, list_directory

tools = [read_tool, list_tool]

TOOL_MAPPING = {
    "read_tool": read_file,
    "list_tool": list_directory
}