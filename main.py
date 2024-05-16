import json
import os
import shutil
from textwrap import dedent

from crewai import Agent, Crew, Task
from langchain.agents.agent_toolkits import FileManagementToolkit
from langchain.chat_models import ChatOpenAI
from tasks import TaskPrompts

from tools.browser_tools import BrowserTools
from tools.file_tools import FileTools
from tools.search_tools import SearchTools
from tools.template_tools import TemplateTools

from dotenv import load_dotenv
load_dotenv()


os.environ['SERPER_API_KEY'] = '9bd11608103c6a824b47c816c2158c96ef54125f'
os.environ['OPENAI_API_BASE'] = 'https://api.groq.com/openai/v1'
os.environ['OPENAI_API_KEY'] = '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'

llm = ChatOpenAI(model='llama3-8b-8192', openai_api_key='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') # Loading GPT-3.5
# llm = ChatOpenAI(
#   model='crewai-llama2',
#   base_url='http://localhost:11434/v1'
# )

class LandingPageCrew():
  def __init__(self, idea):
    self.agents_config = json.loads(open("config/agents.json", "r").read())
    self.idea = idea
    self.__create_agents()

  def run(self):
    # expanded_idea = self.__expand_idea()
    
    # components = self.__choose_template(self.idea)
    # self.__update_components(components, self.idea)
    fileContent = self.__make_html_page(self.idea)
    self.__store_page_content(fileContent)

  def __store_page_content(self, content):
    htmlPath = './workdir/index.html'
    cssPath = './workdir/styles.css'
    
    store_page_content = Task(
        description=TaskPrompts.store_page_content().format(
          file_content=content,
          html_path=htmlPath,
          css_path=cssPath
        ),
        agent=self.content_storer_agent
      )
  
    crew = Crew(
      agents=[self.content_storer_agent],
      tasks=[store_page_content],
    
      verbose=False
    )
    
    returnedData = crew.kickoff()
    returnedData = returnedData.replace('\n', '').replace("```", "")
    print('returned data is ', returnedData)
    
    try: 
      jsonData = json.loads(returnedData)
      print('json data is ', jsonData)
      
      if (jsonData):
        print('----------------------------------------')
        print(jsonData[0])
        print('----------------------------------------')
        print(jsonData[1])
        print('----------------------------------------')
        
        with open('workdir/index.html', "w") as f:
          f.write(jsonData[0])
        
        with open('workdir/styles.css', "w") as f:
          f.write(jsonData[1].replace('<style>', '').replace('</style>', ''))
    except:
      print('Error while extracting json')    


  def __make_html_page(self, idea): 
    make_html_page = Task(
        description=TaskPrompts.make_html_page().format(
          expanded_idea=idea,
        ),
        agent=self.html_developer
      )
    
    crew = Crew(
      agents=[self.html_developer],
      tasks=[make_html_page],
      verbose=True
    )
    fileOutput = crew.kickoff()
    print('fileOutputFor the make html task is ', fileOutput);
    return fileOutput;
  

  def __expand_idea(self):
    expand_idea_task = Task(
      description=TaskPrompts.expand().format(idea=self.idea),
      agent=self.idea_analyst
    )
    refine_idea_task = Task(
      description=TaskPrompts.refine_idea(),
      agent=self.communications_strategist
    )
    crew = Crew(
      agents=[self.idea_analyst, self.communications_strategist],
      tasks=[expand_idea_task, refine_idea_task],
      verbose=True
    )
    expanded_idea = crew.kickoff()
    return expanded_idea

  def __choose_template(self, expanded_idea):
    choose_template_task = Task(
        description=TaskPrompts.choose_template().format(
          idea=self.idea
        ),
        agent=self.html_developer
    )
    update_page = Task(
      description=TaskPrompts.update_page().format(
        idea=self.idea
      ),
      agent=self.html_developer
    )
    crew = Crew(
      agents=[self.html_developer],
      tasks=[choose_template_task, update_page],
      verbose=True
    )
    components = crew.kickoff()
    return components

  def __update_components(self, components, expanded_idea):
    print('Debug log: the components are as follows', components)
    components = components.replace("\n", "").replace(" ",
                                                      "").replace("```", "")

    components = json.loads(str(components))
    for component in components:
      file_content = open(
        f"./workdir/{component.split('./')[-1]}",
        "r"
      ).read()
      create_content = Task(
        description=TaskPrompts.component_content().format(
          expanded_idea=expanded_idea,
          file_content=file_content,
          component=component
        ),
        agent=self.content_editor_agent
      )
      update_component = Task(
        description=TaskPrompts.update_component().format(
          component=component,
          file_content=file_content
        ),
        agent=self.html_developer
      )
      qa_component = Task(
        description=TaskPrompts.qa_component().format(
          component=component
        ),
        agent=self.html_developer
      )
      crew = Crew(
        agents=[self.content_editor_agent, self.html_developer],
        tasks=[create_content, update_component, qa_component],
        verbose=True
      )
      crew.kickoff()

  def __create_agents(self):
    # idea_analyst_config = self.agents_config["senior_idea_analyst"]
    # strategist_config = self.agents_config["senior_strategist"]
    developer_config = self.agents_config["senior_html_developer"]
    editor_config = self.agents_config["senior_content_editor"]
    storer_config = self.agents_config["senior_content_storer"]

    toolkit = FileManagementToolkit(
      root_dir='workdir',
      selected_tools=["read_file", "list_directory"]
    )

    self.html_developer = Agent(
      **developer_config,
      verbose=True,
      llm=llm,
      tools=[
          # SearchTools.search_internet,
          # BrowserTools.scrape_and_summarize_website,
          # TemplateTools.learn_landing_page_options,
          # TemplateTools.copy_landing_page_template_to_project_folder,
          FileTools.write_file
      ] + toolkit.get_tools()
    )

    self.content_editor_agent = Agent(
      **editor_config,
      llm=llm,
      tools=[
          # SearchTools.search_internet,
          # BrowserTools.scrape_and_summarize_website,
      ]
    )
    
    self.content_storer_agent = Agent(
          **storer_config,
          verbose=True,
          llm=llm,
          tools=[
              # SearchTools.search_internet,
              # BrowserTools.scrape_and_summarize_website,
              # TemplateTools.learn_landing_page_options,
              # TemplateTools.copy_landing_page_template_to_project_folder,
              # FileTools.write_file_local
          ]
        )
    

if __name__ == "__main__":
  print("Welcome to Idea Generator")
  print(dedent("""
  ! YOU MUST FORK THIS BEFORE USING IT !
  """))

  print(dedent("""
      Disclaimer: This will use gpt-4 unless you changed it 
      not to, and by doing so it will cost you money (~2-9 USD).
      The full run might take around ~10-45m. Enjoy your time back.\n\n
    """
  ))
  idea = input("# Describe what is your idea:\n\n")
  
  if not os.path.exists("./workdir"):
    os.mkdir("./workdir")

  if len(os.listdir("./templates")) == 0:
    print(
      dedent("""
      !!! NO TEMPLATES FOUND !!!
      ! YOU MUST FORK THIS BEFORE USING IT !
      
      Templates are not included as they are Tailwind templates. 
      Place Tailwind individual template folders in `./templates`, 
      if you have a license you can download them at
      https://tailwindui.com/templates, their references are at
      `config/templates.json`.
      
      This was not tested this with other templates, 
      prompts in `tasks.py` might require some changes 
      for that to work.
      
      !!! STOPPING EXECUTION !!!
      """)
    )
    exit()

  crew = LandingPageCrew(idea)
  crew.run()
  zip_file = "workdir"
  shutil.make_archive(zip_file, 'zip', 'workdir')
  # shutil.rmtree('workdir')
  print("\n\n")
  print("==========================================")
  print("DONE!")
  print(f"You can download the project at ./{zip_file}.zip")
  print("==========================================")
