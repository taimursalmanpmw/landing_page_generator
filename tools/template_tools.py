import json
import shutil
from pathlib import Path

from langchain.tools import tool


class TemplateTools():

  @tool("learn_landing_page_options")
  def learn_landing_page_options(input):
    """Learn the templates at your disposal"""
    templates = json.load(open("config/templates.json"))
    print("-----------------------------------------------------------\nthe templates are\n", json.dumps(templates, indent=2), "\n----------------------------------------------------\n")
    return json.dumps(templates, indent=2)

  @tool("copy_landing_page_template_to_project_folder")
  def copy_landing_page_template_to_project_folder(landing_page_template):
    """Copy a landing page template to your project 
    folder so you can start modifying it, it expects 
    a landing page template folder as input"""
    source_path = Path(f"templates/{landing_page_template}")
    destination_path = Path(f"workdir/{landing_page_template}")
    destination_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source_path, destination_path)
    return f"Template copied to {landing_page_template} and ready to be modified, main files should be under ./{landing_page_template}/src/components, you should focus on those."

