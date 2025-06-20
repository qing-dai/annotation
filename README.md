# Expert Annotation Interface

An interactive web interface that makes expert data collection more engaging than spreadsheet work. Specialists simply open a browser page, view beautifully rendered formulas, and rate each question–paragraph pair on a 1–5 scale. All responses are bundled into a downloadable CSV for easy analysis.

---

## 🚀 Features

- **Welcome Screen**  
  A friendly “Let’s start annotation tasks!” prompt to kick things off.

- **Personalized Flow**  
  Enter your name and see only your tasks.

- **Task Types**  
  Separate batches for `uncertain` vs. `high_conf` questions, each with custom instructions.

- **Math Rendering**  
  Real-time formula rendering via KaTeX for clean, readable equations.

- **Back Button**  
  Fix mis-clicks by going back one item.

- **5-Point Scale**  
  Quick buttons labeled 1 – 5 (“Irrelevant” through “Relevant”).

- **Local Data Storage**  
  Annotations live in your browser until you download a combined CSV.

---

## 🏁 Getting Started

1. **Clone or download** this repo to your static host (e.g. GitHub Pages).  
2. Place your preprocessed Excel file (e.g. `high_confidence_for_annotation_latex_fixed.xlsx`) in the same folder.  
3. No build steps—just push to GitHub and your `index.html` serves the app.

---

## 📝 Workflow

1. **Open** the site in your browser.  
2. **Click** **Begin** on the welcome screen.  
3. **Enter** your **Name** (must match the Excel `Name` column).  
4. Read the **Instructions** for each task type, then click **Start Annotation**.  
5. **Rate** each question–paragraph pair; use **← Back** to correct mistakes.  
6. When all tasks are done, a CSV download is triggered containing all original fields plus `label` and `timestamp`.

---

---

## 🔧 Customization


- **Styling**  
Tweak colors, fonts, and sizes in the `<style>` block of `index.html`.  
Adjust `.card` and `.paragraph` dimensions to suit your preferences.

- **Instruction Text**  
Edit the two instruction strings for `uncertain` and `high_conf` tasks in the JS of `index.html`.

---

## 🛠 Troubleshooting

- **Name Not Found**  
- Ensure the `Name` in your Excel exactly matches your input (case-insensitive).  
- The site will list available names if no match is found.

- **Math Not Rendering**  
- Check that KaTeX scripts are loaded (open the browser console).  
- Verify your `chunk_text` uses proper `$$…$$`, `$begin:math:text$...$end:math:text$`, or `$…$` delimiters.

- **CORS or 404 Errors**  
- Confirm your `.xlsx` and `index.html` are correctly deployed and publicly accessible.

---

## 🎉 Enjoy!

This app transforms dry spreadsheet annotation into a playful, web-based experience—complete with colorful design, smooth math rendering, and a satisfying download at the end. Happy annotating!