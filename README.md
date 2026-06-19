# ML Task: Student Academic Performance Data Processing

## Project Overview
A Python-based data processing application that aggregates and transforms student academic performance records. The system processes raw student marks data, applies intelligent sorting and grouping logic, and generates consolidated performance summaries for academic analysis.

## Objective
Extract and consolidate the top 3 marks per student per subject from timestamped performance records, creating a normalized dataset suitable for academic reporting and performance tracking.

## Problem Statement
Students often take multiple assessments in different subjects at different times. This application:
- **Consolidates** multiple mark entries into structured records
- **Prioritizes** the most recent assessments
- **Normalizes** datasets with varying assessment counts
- **Generates** a clean, reportable output format

## 🔧 Technical Stack
- **Language**: Python 3
- **Core Dependency**: pandas >= 2.0.0
- **Data Processing**: ETL (Extract, Transform, Load) pipeline

## Project Structure
```
ML-Task/
├── main.py              # Primary processing script
├── requirements.txt     # Python dependency specifications
├── data/
│   ├── input.csv       # Raw student performance records
│   └── output.csv      # Processed performance summary
└── README.md           # Project documentation
```

## Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation
```bash
# Clone/Navigate to the project directory
cd ML-Task

# Install dependencies
pip install -r requirements.txt
```

### Execution
```bash
# Run the data processing pipeline
python main.py
```

## Input Data Format
The application expects `data/input.csv` with the following structure:

| Column | Type | Description |
|--------|------|-------------|
| Roll No | String/Integer | Student identifier |
| Subject | String | Subject name |
| Marks | Numeric | Assessment marks |
| Date | String | Assessment date (DD-MM-YYYY format) |

**Example:**
```
Roll No,Subject,Marks,Date
101,Mathematics,85,15-05-2026
101,Mathematics,92,18-05-2026
101,Physics,78,12-05-2026
```

## Output Data Format
The application generates `data/output.csv` with consolidated records:

| Column | Type | Description |
|--------|------|-------------|
| Roll No | String/Integer | Student identifier |
| Subject | String | Subject name |
| M1 | Numeric | Most recent mark |
| M2 | Numeric | Second most recent mark |
| M3 | Numeric | Third most recent mark |
| Date | String | Date of most recent assessment (DD-MM-YY format) |

**Example Output:**
```
Roll No,Subject,M1,M2,M3,Date
101,Mathematics,92,85,0,18-05-26
101,Physics,78,0,0,12-05-26
```

## Processing Logic

### Algorithm Overview
1. **Data Ingestion**: Read CSV file into pandas DataFrame
2. **Date Conversion**: Parse date strings to datetime objects
3. **Sorting**: Sort records by:
   - Roll Number (ascending)
   - Subject (ascending)
   - Date (descending - most recent first)
4. **Aggregation**: Group by (Roll No, Subject)
5. **Mark Extraction**: Retrieve top 3 marks per group
6. **Normalization**: Pad with zeros if fewer than 3 marks exist
7. **Output Generation**: Export to CSV format

### Key Features
- Handles students with varying assessment counts
- Preserves chronological sequence of assessments
- Automatic datetime format conversion
- Robust grouping and aggregation
- CSV-based I/O for data portability

## Use Cases
- **Academic Dashboard**: Consolidate student performance data for institutional reporting
- **Performance Analysis**: Track top assessments per subject
- **Data Migration**: Transform legacy assessment records
- **Reporting Pipeline**: Feed normalized data into BI tools

## Skills Demonstrated
- **Data Processing**: Pandas DataFrame manipulation and transformation
- **Software Development**: Clean, modular Python code structure
- **Problem Solving**: Logical algorithm design for data aggregation
- **Data Engineering**: ETL pipeline development
- **Format Handling**: Date/time parsing and CSV I/O operations

## Performance Characteristics
- **Time Complexity**: O(n log n) due to sorting operations
- **Space Complexity**: O(n) for output generation
- **Scalability**: Efficiently processes datasets with thousands of records



