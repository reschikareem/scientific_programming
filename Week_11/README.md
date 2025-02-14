**This Week: Workshop in class on the Development of an AI-supported Augmented Analytics Web Application (Part I)**

**The task is to build your own AI-supported web application.**

**Note that the provided example data (car data) can be replaced by your own (properly prepared) data.**

**The material is available in the folder 'workshop material' in Week_11!**

**Recommended project folder structure:**

```bash
project/
│
├── .devcontainer/
│    └── devcontainer.json       → Configuration file for setting up the Dev Container
│
├── app.py                       → The main app file
├── Procfile                     → Configuration file for deployment (e.g. on Koyeb)
├── data/
│   ├── autoscout24_data.csv      → .csv file with car data
│   └── credentials.json          → JSON file storing the OpenAI API key
│
├── static/
│   ├── css/
|   |   ├── styles.css            → File to define styles (CSS) in HTML pages
│   ├── logo.svg                  → Logos etc. to include into the HTML pages
│   └── graphic.png               → Generated plots (saved here)
│   
├── templates/
│    ├── index.html                → Main HTML page
│    ├── data.html                 → Data describtion page
│    └── questions.html            → Example questions page
│
└── requirements.txt               → File to specify the Python libraries
```