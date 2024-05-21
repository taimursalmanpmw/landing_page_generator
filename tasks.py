from textwrap import dedent


class TaskPrompts():
  
  #region Non-code tasks
  def expand():
    return dedent("""
      THIS IS A GREAT IDEA! Analyze and expand it 
      by conducting a comprehensive research.
  
      Final answer MUST be a comprehensive idea report 
      detailing why this is a great idea, the value 
      proposition, unique selling points, why people should 
      care about it and distinguishing features. 
  
       IDEA: 
      ----------
      {idea}
    """)

  def refine_idea():
    return dedent("""
      Expand idea report with a Why, How, and What 
      messaging strategy using the Golden Circle 
      Communication technique, based on the idea report.
      
      Your final answer MUST be the updated complete 
      comprehensive idea report with WHY, HOW, WHAT, 
      a core message, key features and supporting arguments.
      
      YOU MUST RETURN THE COMPLETE IDEA REPORT AND 
      THE DETAILS, You'll get a $100 tip if you do your best work!
    """)

  #endregion
  
  def choose_template():
    return dedent("""
      Learn the templates options choose and copy 
      the one that suits the idea below the best, 
      YOU MUST COPY, and then YOU MUST read the index.html and any .css files 
      in the directory you just copied, to decide what 
      component files should be updated to make the 
      landing page about the idea below.
      
      - YOU MUST READ THE DIRECTORY BEFORE CHOOSING THE FILES.      
      - YOU MUST NOT UPDATE any Pricing components.
      - YOU MUST UPDATE ONLY the 4 most important components.
      
      Your final answer MUST be ONLY a JSON array of 
      components full file paths that need to be updated.

      IDEA 
      ----------
      {idea}
    """)
    
    

  def update_page():
    return dedent("""
      READ the ./[chosen_template]/index.html
      to learn its content and then write an updated 
      version to the filesystem that removes any 
      section related components that are not in our 
      list from the returns. Keep the imports.
      
      Final answer MUST BE ONLY a valid json list with 
      the full path of each of the components we will be 
      using, the same way you got them.

      RULES
      -----
      - NEVER ADD A FINAL DOT to the file content.
      - NEVER WRITE \\n (newlines as string) on the file, just the code.
      - NEVER USE COMPONENTS THAT ARE NOT IMPORTED.
      - ALL COMPONENTS USED SHOULD BE IMPORTED, don't make up components.
      - Save the file as with `.html` extension.
      - Return the same valid JSON list of the components your got.

      You'll get a $100 tip if you follow all the rules!

      Also update any necessary text to reflect this landing page
      is about the idea below.
      
      IDEA 
      ----------
      {idea}
    """)
  
  def update_page_content():
    return dedent("""
      A engineer will update the {component} (code below),
      return a list of good options of texts to replace 
      EACH INDIVIDUAL existing text on the component, 
      the suggestion MUST be based on the idea bellow, 
      and also MUST be similar in length with the original 
      text, we need to replace ALL TEXT.
      
      NEVER USE Apostrophes for contraction! You'll get a $100 
      tip if you do your best work!

      IDEA 
      -----
      {expanded_idea}
  
      COMPONENT CONTENT
      -----
      {file_content}
    """)

  def component_content():
    return dedent("""
      A engineer will update the {component} (code below),
      return a list of good options of texts to replace 
      EACH INDIVIDUAL existing text on the component, 
      the suggestion MUST be based on the idea bellow, 
      and also MUST be similar in length with the original 
      text, we need to replace ALL TEXT.
      
      NEVER USE Apostrophes for contraction! You'll get a $100 
      tip if you do your best work!

      IDEA 
      -----
      {expanded_idea}
  
      COMPONENT CONTENT
      -----
      {file_content}
    """)

  def update_component():
    return dedent("""
      YOU MUST USE the tool to write an updated 
      version of the component to the file 
      system in the following path: {component} 
      replacing the text content with the suggestions 
      provided.
      
      You only modify the text content, you don't add 
      or remove any components.
      
      You first write the file then your final answer 
      MUST be the updated component content.

      RULES
      -----
      - Remove all the links, this should be single page landing page.
      - Don't make up images, videos, gifs, icons, logos, etc.
      - keep the same style and tailwind classes.
      - MUST HAVE `'use client'` at the be beginning of the code.
      - href in buttons, links, NavLinks, and navigations should be `#`.
      - NEVER WRITE \\n (newlines as string) on the file, just the code.
      - NEVER FORGET TO CLOSE THE FINAL BRACKET (}}) in the file.
      - Keep the same component imports and don't use new components.
      - NEVER USE COMPONENTS THAT ARE NOT IMPORTED.
      - ALL COMPONENTS USED SHOULD BE IMPORTED, don't make up components.
      - Save the file as with `.jsx` extension.

      If you follow the rules I'll give you a $100 tip!!! 
      MY LIFE DEPEND ON YOU FOLLOWING IT!
  
      CONTENT TO BE UPDATED
      -----
      {file_content}
    """)

  def qa_component():
    return dedent("""
      Check the React component code to make sure 
      it's valid and abide by the rules bellow, 
      if it doesn't then write the correct version to 
      the file system using the write file tool into 
      the following path: {component}.
    
      Your final answer should be a confirmation that 
      the component is valid and abides by the rules and if
      you had to write an updated version to the file system.

      RULES
      -----
      - NEVER USE Apostrophes for contraction!
      - ALL COMPONENTS USED SHOULD BE IMPORTED.
      - MUST HAVE `'use client'` at the be beginning of the code.
      - href in buttons, links, NavLinks, and navigations should be `#`.
      - NEVER WRITE \\n (newlines as string) on the file, just the code.
      - NEVER FORGET TO CLOSE THE FINAL BRACKET (}}) in the file.
      - NEVER USE COMPONENTS THAT ARE NOT IMPORTED.
      - ALL COMPONENTS USED SHOULD BE IMPORTED, don't make up components.
      - Always use `export function` for the component class.

      You'll get a $100 tip if you follow all the rules!
    """)

  def make_html_page(): 
    return dedent("""
        Given an idea, write an HTML page with CSS styles and Javascript, if needed, in a modern fashion for the middle aged consumer. 
        You must make sure the html, css and js content are kept separate instead of using inline styling or inline <script> tags
        You must ensure that the styles for the page are NOT in the <header> of the HTML. Instead the styles are separate from the html 
        You must ensure that there is no extra text in the final answer excluding the HTML content, CSS styles, and Javascript
        
        Rules:
        ----------------
        You MUST WRITE return your HTML and CSS content in a SINGLE STRING.
        NEVER USE Apostrophes for contraction! 
        You MUST NOT have any text in your final answer other than your css and html content!
        Your HTML content must be preceded by an '<!--index.html-->' comment, your CSS content must be preceded by a '<!--styles.css-->' comment, and your javascript content must be preceeded by a '<!--index.js-->' comment ALWAYS
        At the end of ALL of your Javascript code, you MUST add a '<!--code end-->' comment.
        
        If the IDEA requires you to have an FAQs section, you must use the <button> HTML component.
        If the IDEA requires you to use a complex structure like an accordion or a carousel, make sure to add appropriate Javascript as needed.
        
    
        If your component has any buttons, you must give it the .button class EVERY TIME.
        ----------------
        
        You'll get a $100 tip if you follow the rules!
        MY LIFE DEPENDS ON YOU FOLLOWING IT!
        
        These keywords must never be translated and transformed:
        - Action:
        - Thought:
        - Action Input:
          because they are part of the thinking process instead of the output.

        IDEA 
        -----
        {expanded_idea}
                  """)
    
  def store_page_content():
    return dedent("""
          Given an output from the HTML engineer, you must extract the html content and the css content, and separate them. 
          The HTML content will be preceded by a comment containing 'index.html', and the CSS content will be preceded by a comment containing 'styles.css'. Use this to separate the HTML and CSS
          You must ensure that the html content is surrounded by the <html> tags, and the css content should be surrounded by the <style> tags. 
          You must ensure that there are no trailing \\n or \\r characters in the output
          You must ensure the output is correctly formatted to be a json array
                            
          Rules:
          ------
          DO NOT use ellipses to summarize any form of content
          You must ensure that the final answer is ONLY a json array of two elements, the first being the HTML content and the second being the css content.
          ------
          
          MY LIFE DEPENDS ON YOU FOLLOWING IT!
          I will give you a $1000 tip if you follow the rules! and a promotion!
          
          Your final answer MUST ONLY BE a json array of two elements, the first being the HTML content and the second being the css content.
          It must have NO OTHER TEXT, not even any text describing the final answer.
          
          THE CONTENT
          ------
          {file_content}
          ------
          """)
    # your HTML content in the ./workdir folder, in a file named index.html, and you must store your css content in the same folder, named styles.css
    
  def choose_template_designer():
    return dedent("""
      Learn the templates options which can be found in the ./templates folder by reading the templates in the folder. Choose the one that suits the idea below the best. You can learn more about the templates in the config/templates.json folder 
  
      - YOU MUST READ THE DIRECTORY BEFORE CHOOSING THE FILES.      
      - YOU MUST CHOOSE ONLY ONE TEMPLATE out of all the templates
      - YOU MUST NOT QUIT UNTIL YOU HAVE DECIDED ON A TEMPLATE
      - YOU MUST FOLLOW THE PROVDED FORMAT
      
      You will get a $1000 tip if you do your best job! My life depends on you! You MUST follow this or I will fire you!
      
      PROVIDED FORMAT:
      ---------------------
      Your final answer MUST be the folder of the template you have chosen. The folder of the template MUST be preceded by <!-- template -->. Your final answer will begin with your reasoning for choosing your template and why you didn't choose other options.
      --------------------

      An example of your output would be as follows:
      [your reasoning for choosing a template]
      <!-- template -->
      [the folder of your chosen template]


      IDEA 
      ----------
      {idea}
    """)
    