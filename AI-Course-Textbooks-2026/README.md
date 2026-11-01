# AI Course Textbooks (2026)

This folder stores the safe Windows uploader for the 110 files of our AI course. **The textbook files have not yet been uploaded to GitHub.**

## Expected layout after successful upload

- `Course-Libraries/01_הכנה`: 4 foundation chapters, their Word/PDF/Colab files, and an assembled book.
- `Course-Libraries/02_נושאי_ליבה`: 16 core chapters and their assembled book.
- `Course-Libraries/03_למידה_עמוקה_ופרויקט_גמר`: 12 deep learning chapters and their assembled book.
- `Course-Libraries/`: complete 32-chapter PDF and DOCX, manifest, README.

The uploaded source ZIP must be named `AI_Course_2026_All_3_Libraries.zip` and contains exactly 110 files.

## Windows PowerShell 5.1 upload

Download **the latest** [UPLOAD_FULL_COLLECTION.ps1](./UPLOAD_FULL_COLLECTION.ps1) and the course ZIP to your Downloads folder, then run:

```powershell
cd "$env:USERPROFILE\Downloads"
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/samiabo75/Data-Science-ML-Course/main/AI-Course-Textbooks-2026/UPLOAD_FULL_COLLECTION.ps1" -OutFile "UPLOAD_FULL_COLLECTION.ps1"
powershell -ExecutionPolicy Bypass -File ".\UPLOAD_FULL_COLLECTION.ps1" -ZipPath ".\AI_Course_2026_All_3_Libraries.zip"
```

The script is written in ASCII so Windows PowerShell 5.1 does not misread Hebrew literals. The source ZIP retains all Hebrew folder and file names. It refuses to overwrite an existing destination and uses a fresh fast-forward pull before committing to `main`.

The final repository destination is `AI-Course-Textbooks-2026/Course-Libraries`.
