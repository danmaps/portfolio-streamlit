from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Streamlining GIS Data Cleanup")

st.markdown("""

# Streamlining GIS Data Cleanup
#### A Balanced Approach to Automation

Data cleanup is one of the most repetitive yet crucial tasks in GIS workflows. A clean dataset ensures accurate analysis and reliable results. In my experience at Southern California Edison, I’ve tackled numerous data cleaning challenges. Today, I want to share a Python function that semi-automates the cleanup process, striking a balance between efficiency and control.

The `autofill_selected` function I’ve developed is a practical example of this approach. It iterates over specified fields in a given layer, checks for unique values, and fills in empty or null values with a consistent value. Here's a closer look at the function and how it works.

```python
def autofill_selected(layer, fields):
    for field in fields:
        print(f"Looking at field: {field}")
        
        # Create a set to store unique values
        unique_values = set()
        
        # Use a search cursor to iterate through the rows
        with arcpy.da.SearchCursor(layer, field) as cursor:
            for row in cursor:
                if row[0] is not None:
                    unique_values.add(row[0])
        
        print(f"Unique values: {unique_values}")

        if len(unique_values) > 1:
            print(f"{field} has more than one non-null value: {unique_values}")
        else:
            # Construct a query to find null or empty values
            query = f"{field} IS NULL OR {field} = ''"
            
            # Use an update cursor to update null or empty values
            with arcpy.da.UpdateCursor(layer, field, query) as update_cursor:
                for row in update_cursor:
                    row[0] = list(unique_values)[0]
                    update_cursor.updateRow(row)
    
    return True
```

## How It Works

1. **Iterating Over Fields:** The function starts by iterating over each field in the provided list. It prints the name of the field being checked, which is helpful for tracking progress.

2. **Collecting Unique Values:** Using a search cursor, it goes through each row of the layer and collects unique, non-null values in a set. This set gives a quick view of the data distribution within the field.

3. **Evaluating Field Values:** After collecting the unique values, the function prints them out. If the field has more than one unique non-null value, it flags this for further inspection. If there’s only one unique non-null value, it proceeds to fill null or empty entries with this value.

4. **Updating Null Values:** It constructs a query to find null or empty values and uses an update cursor to fill these entries with the consistent value found. This step ensures that the data is standardized.

## The Balance Between Automation and Control
            
 There’s a continuum of automation from manual all the way to fully automatic, and this one lies directly in the middle, offering a thoughtful balance of control and efficiency.
""")

st.image(r"assets/automation_continuum.png")

st.markdown("""

While the `autofill_selected` function automates a significant portion of the cleanup process, it’s designed to run under supervision. This semi-automatic approach ensures that critical decisions are still made by a human, maintaining data integrity while saving time—estimated at about 50%.

## Practical Application

In my work, functions like `autofill_selected` have been invaluable for tasks such as ensuring consistent attribute data across large datasets. This function can be easily integrated into larger workflows in ArcGIS Pro, offering a flexible and efficient solution to common data quality issues.

By adopting such semi-automated tools, we can achieve a balance between quality and efficiency in GIS data management, making our workflows more productive without sacrificing accuracy. If you’re handling repetitive data cleaning tasks, consider implementing a similar approach. It could save you significant time and effort while maintaining high data standards.

## Running in an ArcGIS Pro Project

I run this function in the context of an ArcGIS Pro project with a Jupyter Notebook open in the app alongside a map. This setup allows for a smooth integration of code execution and visual inspection of the data.
""")