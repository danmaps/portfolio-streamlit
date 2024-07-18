
# Enhancing Spatial Analysis: Lessons Learned from Automating Proximity Analysis

I recently took on a work project that began with a simple goal: perform spatial proximity analysis for a user. Initially, this was a manual task using ArcGIS Pro, but I ended up turning it into a fully automated tool. Here's a detailed look at what I learned, how I refined user requirements, leveraged open-source tools, and ultimately turned this into a useful and flexible tool.

## The Manual Approach

Initially, I performed the analysis manually using ArcGIS Pro. This involved several time-consuming steps:

1. **Data Preparation**: Cleaning and organizing the data to ensure accuracy.
2. **Running Geoprocessing Tools**: Using ArcGIS Pro to perform spatial proximity analysis. This involves several ArcGIS geoprocessing tools, including the following:
    - **Near Table**: Identifying points within a specified distance of another point.
    - **Buffer**: Creating a buffer around each point.
    - **Dissolve**: Merging the buffers together to create distinct polygons representing each group.
    - **Spatial Join**: Joining the buffers with the original data to get the original attributes for each group and summing a field of interest.
3. **Creating a Web App**: Developing a web application in ArcGIS Online to display the results interactively.

While this approach worked, it was labor-intensive and required significant effort for each new dataset. It became clear that automating this process would save time and ensure consistency.

## Refining User Requirements

I first needed to understand the users' needs better. I decided that users would need:

- The ability to upload their own datasets.
- Dynamic selection of columns for latitude, longitude, and IDs.
- Interactive adjustment of proximity thresholds.
- Immediate visualization and downloadable results.

These choices guided the development of a more robust tool.

## Leveraging Open-Source Tools as an Alternative to Arcpy

In my professional experience, I've extensively used Arcpy for geospatial analysis. However, I had to explore open-source alternatives for this project. I chose Geopandas for the analysis and Folium inside Streamlit for the UI, which offered several benefits:

- **Geopandas**: Provides powerful data structures for working with geospatial data in Python, similar to how Pandas handles tabular data. It enabled seamless conversion between dataframes and geospatial dataframes. Figuring ou how to match the geoprocessing operations avilable in ArcGIS Pro was a breakthrough.
- **Folium**: Facilitates the creation of interactive maps directly from geospatial data. It integrates well with Streamlit, allowing for a smooth user experience. I also knew that Streamlit allows for easy upload and download of data files including Excel.

The choice of these tools was influenced by their flexibility and the growing ecosystem of geospatial libraries in the open-source community. They provide a cost-effective and versatile alternative to proprietary solutions, aligning with the broader movement towards open-source in geospatial analysis. Crucially, this allows the tool to be run anywhere (including here on `streamlit.app`) because it does not depend on proprietary software licensing.

## Self-Serve Tool vs. Delivering Analysis Results

One of the key decisions I face (often) is whether to provide a self-serve tool or to deliver analysis results directly to customers. Each approach has its merits:

- **Self-Serve Tool**: Empowers users to explore their data independently. It's flexible and scalable, allowing users to upload their datasets, configure analysis parameters, and obtain results instantly. This approach aligns well with the trend towards democratizing data analysis.
- **Delivering Analysis Results**: Suitable for users who need specific insights without the need to interact with the tool. It involves processing the data on behalf of the user and delivering a polished report.

For this project, I created a self-serve tool, leveraging Streamlit's capabilities to create an interactive and user-friendly interface. This decision was based on the goal of enabling users to perform their analysis independently, saving everyone time and effort. Whether they'll actually want to use it in the future remains to be seen... Either way, I'm glad I have this tool to use for myself, and to potentially repurpose it in the future.

## The Automated Tool: A practical utility with a lot going on under the hood

Here's a brief overview of some of the functionality implemented in the automated tool:

### File Upload and Data Handling:
```python
def handle_file_upload():
    uploaded_file = st.file_uploader("Choose a .xlsx file", type="xlsx")
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
    else:
        df = pd.DataFrame(sample_data)  # Use sample data if no file is uploaded
    return df, uploaded_file
```

### Proximity Analysis:
```python
def process_data(df, lat_col, lon_col, distance_threshold, id_col=None):
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df[lon_col], df[lat_col]))
    projected_gdf = gdf.to_crs(epsg=32611)
    # Spatial analysis logic here
    return processed_gdf
```

### Interactive Map Creation:
```python
def create_folium_map(gdf, distance_threshold_meters, lat_col, lon_col, id_col):
    m = folium.Map(tiles="cartodb-dark-matter", width='100%', height='100%')
    folium_static(m)
```

### User Interface with Streamlit:
```python
st.set_page_config(page_title="Spatial Proximity Excel Enrichment", layout="wide")
distance_threshold_feet = st.slider("Distance threshold in feet", 25, 800, 100)
distance_threshold_meters = feet_to_meters(distance_threshold_feet)
```

## Conclusion

This project was a significant learning experience. By refining user requirements, exploring open-source alternatives, and thoughtfully choosing the right delivery model, I developed a robust and flexible tool for spatial proximity analysis. This automation not only saves time but also ensures consistency and reproducibility, making this kind of analysis trivial in the future.

So, while the initial manual process was effective, the automated tool has proven to be a far more efficient and user-friendly solution. It’s a perfect example of how engineering a solution thoughtfully can lead to a genuinely useful product.
