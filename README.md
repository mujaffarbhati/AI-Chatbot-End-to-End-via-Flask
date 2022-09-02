# AI-Chatbot
Chatbot made via NLP  for Question - Answering purposes as of being a 24x7 support assistant of websites. <br>
Bert model from the transformers library is used since its a pretrained model. <br>
The project is made end to end via flask providing both chatbot as well as voicebot depending on the use of the user as well as an additional admin section is added to manage and customize the data on the users need.

# Modules and Library used: 
Transformers - BertQuestionandAnswering and Berttokenizer <br>
Pytorch <br>
Flask <br>
Pickle <br>
Bootstrap is used for frontend development

# How to Use the Chatbot
<li> In order to append the chatbox to your website pull the main.py since it is the model of the project. <br>
<li> Import the model in your backend. (Flask in our case) <br>
<li> Append the Html changes according to the theme of your website along with the dashboard page for managing and customizing the data of the chatbot.<br>
<li> Choose the appropriate bot model from the html file since there are 2 sub usage of the model - Chatbot and Voicebot. <br>
<li> Append the Chosen Html file in your code and select your code of need from the backend.py file where Flask is being used.
<li> In main.py uncomment the pickle creating code while commenting the rest of the code to form the pickle of the model and tokenizer, (1.4GB approx)
<li> The config.json file contains the parameters of the project.
  
# Additional features / Conclusion
<li> The additional features that could be added in the module is allowing the admin to choose the layout of the chatbot from the dashboard itself. 
<li> Database is pre-connected for the users if they want to connect the database to the project.
<li> Roberta model from transformers library could be used to further optimize the model.
<li> Open to suggestions. Feel free to pull the repository for your need.

  
 
 


