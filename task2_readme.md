# CodeAlpha Data Analytics - Task 2: Data Cleaning and Preparation

## Project Overview
This task demonstrates systematic pipeline construction for data cleaning and preparation using Python and Pandas. The implementation tackles standard data discrepancies found in enterprise analytics pipelines.

## Cleaned Framework Modules

### 1. Duplicate Invalidation
* **Issue Identified:** Repeated row records for the same profile entity (`PassengerId: 104`).
* **Resolution Action:** Applied `.drop_duplicates()` filtering to preserve rows unique to the identity map.

### 2. Format Standardization & Type Transformation
* **Issue Identified:** The `Salary` metrics contained currency markers (`₹`) and string-based punctuation. `Join_Date` variations caused index alignment issues.
* **Resolution Action:** Isolated alphanumeric text using regex string replacements, casting financial targets into numeric `float` values, and normalising structural logs via `pd.to_datetime()`.

### 3. Missing Structural Value Treatment
* **Issue Identified:** Missing observations (`NaN`) present across the `Age` attributes block.
* **Resolution Action:** Imputed the structural statistical column median to stabilize the dataset balance without generating mean skewness.

### 4. Outlier Filtering Limits
* **Issue Identified:** Logical entry error found in demographic data (`Age: 150`) alongside an extreme data skew in salary scales.
* **Resolution Action:** Implemented static parameter capping for structural age limits and leveraged Interquartile Range ($IQR$) threshold boundaries to smooth out major capital outliers.
* 
