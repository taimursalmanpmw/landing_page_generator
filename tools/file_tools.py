from langchain.tools import tool
from crewai_tools.tools import WebsiteSearchTool, SerperDevTool, FileReadTool

class FileTools():

  @tool("write_file")
  def write_file(data):
    """Useful to write a file to a given path with a given content. 
       The input to this tool should be a pipe (|) separated text 
       of length two, representing the full path of the file and the content to be written"""
    try:
      path, content = data.split("|")
      path = path.replace("\n", "").replace(" ", "").replace("`", "")
      if not path.startswith("./workdir"):
        path = f"./workdir/{path}"
      with open(path, "w") as f:
        f.write(content)
      return f"File written to {path}."
    except Exception:
      return "Error with the input format for the tool."
    
  @tool("read_file")
  def read_file(data):
    """
    Used to read the contents of a file. The input to this tool should be the full path to the file
    """
    if (data):
      return FileReadTool(file_path=data,	description='A tool to read the job description example file.')
    return 'Error with input formatting for the tool'

  @tool("write_file_local")
  def write_file_local(data):
    """Useful to write a file to a given path with a given content. 
       The input to this tool should be a pipe (|) separated text 
       of length two, representing the path of the file and the content to be written"""

    print('data is ', data)
    path, content = data.split("|")
    print('the path is', path, 'and the contnet is ', content)
    path = path.replace("\n", "").replace(" ", "").replace("`", "")
    
    with open(path, "w") as f:
      f.write(content)
    return f"File written to {path}."





#       including the /workdir/template, and the React 
#        Component code content you want to write to it.
#        For example, `./Keynote/src/components/Hero.jsx|REACT_COMPONENT_CODE_PLACEHOLDER`.
#        Replace REACT_COMPONENT_CODE_PLACEHOLDER with the actual 
#        code you want to write to the file.