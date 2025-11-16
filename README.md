# Flask Todo App - Setup Instructions
A simple task board, or a kanban board with drag and drop feature and team summary. Tech stack used is Flask and Tailwind CSS
## Prerequisites
- Python 3.8+
- Windows, macOS, or Linux

## Installation & Setup

### 1. Install Python Dependencies
```powershell
pip install -r requirements.txt
```

### 2. Download Tailwind CSS Standalone CLI

For **Windows (x64)**:
```powershell
Invoke-WebRequest -Uri "https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-windows-x64.exe" -OutFile "tailwindcss.exe"
```

For **macOS (arm64)**:
```bash
curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-macos-arm64
chmod +x tailwindcss-macos-arm64
mv tailwindcss-macos-arm64 tailwindcss
```

For other platforms, visit: https://github.com/tailwindlabs/tailwindcss/releases/latest

### 3. Build Tailwind CSS

**Development (watch mode)**:
```powershell
.\tailwindcss.exe -i src/input.css -o src/output.css --watch
```

**Production (minified)**:
```powershell
.\tailwindcss.exe -i src/input.css -o src/output.css --minify
```

### 4. Run the Application
```powershell
python main.py
```

## Project Structure
```
serverless_todo_app/
├── main.py                 # Flask backend
├── index.html              # Frontend HTML
├── requirements.txt        # Python dependencies
├── tailwind.config.js      # Tailwind configuration
├── tailwindcss.exe         # Tailwind CLI (downloaded)
└── src/
    ├── input.css          # Tailwind directives
    └── output.css         # Generated CSS (created by Tailwind)
```

## No npm Required!
This project uses Tailwind CSS's standalone CLI, so you don't need Node.js or npm installed.
