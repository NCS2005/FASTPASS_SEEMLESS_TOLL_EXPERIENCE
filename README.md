# FastPass: Seamless Toll Experience

An automated toll management prototype that reads vehicle number plates from car images using computer vision and OCR, looks up the vehicle's account, and decides in real time whether the vehicle passes automatically, is redirected for manual payment, or is fined.

Developed as a Data Science internship project at **Osmania Technology Business Incubator (OTBI), Osmania University, Hyderabad** (June 2025), under the guidance of **Dr. T. Harinarayana**, Advisor, OTBI.

---

## Problem

Toll plazas suffer from congestion caused by manual payment, human error, and slow processing, which leads to long queues, fuel wastage, and commuter frustration. FastPass explores how image processing, OCR, and simple decision logic can automate the toll decision with minimal human intervention.

## Features

- **Number plate detection** from full car images using OpenCV (grayscale, bilateral filtering, edge detection, contour analysis)
- **OCR plate recognition** with Tesseract (alphanumeric whitelist, `--oem 3 --psm 6`) and regex-based cleanup
- **Fallback OCR**: if no plate contour is found, the full image is read so the workflow doesn't stop
- **Account lookup** against user and toll datasets stored as CSV files
- **Rule-based toll decision engine**: auto pass, manual payment, or fine
- **Real-time balance and fine updates** written back to the CSV database
- **Tkinter GUI** for selecting a car image and running the whole pipeline in one click, with an image preview

## How It Works

```
Car image ──► Preprocessing ──► Plate contour detection ──► OCR ──► Text cleanup
                                        │ (fails)
                                        └──► Full-image OCR fallback
                                                         │
                     Plate number ──► Lookup in DATA_USER.csv + DATA_TOLL.csv
                                                         │
                                              Toll decision engine
                                                         │
                          Instruction + updated balance/fine written to CSV
```

### Toll Decision Logic

| Condition | Instruction | Deduction |
|---|---|---|
| `balance ≥ toll_fee` | **GO STRAIGHT** (auto pass) | `toll_fee` |
| `balance < ₹50`, driver turns left | **MANUAL PAYMENT** | None |
| `balance < ₹50`, driver goes straight anyway | **FINE IMPOSED** | `toll_fee + ₹200` fine |

- Low-balance threshold: **₹50**
- Fixed fine for bypassing the instruction: **₹200**
- `toll_fee` depends on the vehicle

### Output Shown

- Name, gender, age, vehicle type
- Current balance, fine, and applicable toll fee
- Instruction (GO STRAIGHT / MANUAL PAYMENT / FINE IMPOSED)
- New balance and updated fine

## Datasets

**`DATA_USER.csv`**: personal and vehicle details, keyed by number plate

```
number_plate, name, gender, age, vehicle_type, contact
```

**`DATA_TOLL.csv`**: toll account details for each vehicle

```
number_plate, balance, fine, date_of_birth, toll_fee
```

Sample vehicle images were collected from nearby parked cars to test OCR on real-world plates.

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core logic |
| OpenCV | Image preprocessing and plate detection |
| Tesseract OCR (`pytesseract`) | Plate text extraction |
| EasyOCR | Alternative OCR engine |
| pandas | Reading and updating CSV data |
| NumPy | Array and image operations |
| Tkinter | GUI for image selection |
| Pillow (PIL) | Displaying the selected image |

## Installation

### 1. Install Tesseract OCR (system dependency)

- **Windows:** install from the [UB Mannheim Tesseract builds](https://github.com/UB-Mannheim/tesseract/wiki) and note the install path (usually `C:\Program Files\Tesseract-OCR\tesseract.exe`)
- **Linux:** `sudo apt install tesseract-ocr`
- **macOS:** `brew install tesseract`

On Windows, point pytesseract to the executable if it isn't on your PATH:

```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

### 2. Clone the repo and install Python packages

```bash
git clone https://github.com/NCS2005/FASTPASS_SEEMLESS_TOLL_EXPERIENCE.git
cd FASTPASS_SEEMLESS_TOLL_EXPERIENCE
pip install opencv-python pytesseract easyocr pandas numpy pillow
```

Tkinter ships with standard Python installs on Windows and macOS. On Linux: `sudo apt install python3-tk`.

## Usage

<!-- TODO: replace with the actual entry-point script name -->

```bash
python <main_script>.py
```

1. A file dialog opens. Select a car image.
2. The system detects and reads the number plate.
3. The matched user and toll details are printed along with the routing instruction.
4. Balance and fine changes are saved to the CSV files.

## Project Structure

<!-- TODO: update to match the final repository contents -->

```
├── setup_db.py          # Database / CSV setup
├── <main_script>.py     # Main pipeline: GUI, OCR, decision logic
├── DATA_USER.csv        # User and vehicle details
├── DATA_TOLL.csv        # Toll balance, fine, and fee data
└── README.md
```

## Challenges and Solutions

| Challenge | Solution |
|---|---|
| Plate contour not found in some full-car images | Full-image OCR fallback plus resizing and thresholding |
| OCR misreads, extra spaces, noise | Tesseract alphanumeric whitelist and regex cleanup |
| OCR output not matching dataset format | Normalized plate text, stripped whitespace, standardized column names |
| Multiple payment paths | Branching decision engine with immediate CSV updates |
| Keeping the GUI simple | Minimal Tkinter interface with image preview; internals hidden from the user |

## Results

- Tested with 5 vehicle plates covering different balances and toll conditions
- Decisions matched the expected rules in every scenario tested
- CSV balance and fine values stayed consistent after each transaction

## Future Scope

- Live camera feed instead of uploaded images
- Deep-learning plate detection (e.g., YOLO) for better accuracy in poor lighting
- A real database (SQLite / PostgreSQL) instead of CSV files
- Transaction logging with timestamps for every toll event
- Integration with payment gateways and SMS/email alerts

## Team

- C. Rithika
- N. Chaitanya Sandeep
- K. Rajeswari

B.E. Computer Science (Data Science & Cyber Security), Maturi Venkata Subba Rao (MVSR) Engineering College, Hyderabad

## Acknowledgements

We thank **Dr. T. Harinarayana** (Advisor, OTBI) for his mentorship, **Dr. E. Vidya Sagar** (Director, OTBI) for the opportunity, and **Osmania Technology Business Incubator (OTBI)** for supporting this internship.
