# AI Planet Fullstack Intern Assignment

Live: https://assignment.sudheer.tech

## Demo Video
https://github.com/user-attachments/assets/75e886d5-75c9-449b-8322-c35f2890f800

## To Run the app Locally
### Backend:
#### Open the file and Install dependencies
```bash
cd ./backend
pip install -r requirement.txt
```




#### Run the app
```bash
uvicorn src.main:app --reload
```
<br>

### Frontend:

#### Open the file and Install dependencies
```bash
cd ./Frontend
npm install
```


#### Run the app
```bash
npm run dev
```

##  File Structure Backend

``` 
backend
┣ assignment
┣ src
┃ ┣ api
┃ ┃ ┣ init.py
┃ ┃ ┣ dependencies.py
┃ ┃ ┗ routes.py
┃ ┣ models
┃ ┃ ┣ init.py
┃ ┃ ┣ database.py
┃ ┃ ┗ models.py
┃ ┣ schemas
┃ ┃ ┣ init.py
┃ ┃ ┣ responses.py
┃ ┃ ┗ schema.py
┃ ┗ services
┃   ┣ init.py
┃   ┣ pdf_service.py
┃   ┣ qa_service.py
┃   ┣ s3_service.py
┃   ┣ config.py
┃   ┗ main.py
┣ .env
┣ .gitignore 
┗ requirements.txt
```

##  File Structure Backend

``` 
frontend
 ┣ public
 ┃ ┣ AI Planet Logo.png
 ┃ ┣ AI Planet Logo.svg
 ┃ ┣ gala_add.png
 ┃ ┣ Group.png
 ┃ ┣ logo.png
 ┃ ┗ vite.svg
 ┣ src
 ┃ ┣ assets
 ┃ ┣ components
 ┃ ┃ ┣ MainScreenSe...
 ┃ ┃ ┣ Section1.tsx
 ┃ ┃ ┣ Section2.tsx
 ┃ ┃ ┗ FileUpload.tsx
 ┃ ┣ hooks
 ┃ ┃ ┗ useChatScroll.tsx
 ┃ ┣ Routes
 ┃ ┃ ┗ AppRouter.tsx
 ┃ ┣ Screens
 ┃ ┃ ┗ MainScreen.tsx
 ┃ ┣ utils
 ┃ ┃ ┗ config.ts
 ┃ ┣ App.css
 ┃ ┣ App.tsx
 ┃ ┣ index.css
 ┃ ┗ main.tsx
 ┣ .gitignore
 ┣ eslint.config.js
 ┣ index.html
 ┣ package-lock.json
 ┣ package.json
 ┣ postcss.config.js
 ┣ README.md
 ┣ tailwind.config.js
 ┣ tsconfig.app.json
 ┣ tsconfig.json
 ┣ tsconfig.node.json
 ┗ vite.config.ts
```
