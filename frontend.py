import streamlit as st
from PIL import Image
import os
from image import load_employee_graphs
from generate import generate_graph_insights_openai
from io import BytesIO
import base64
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"] 
API_KEY = os.environ["OPENAI_API_KEY"]
# Assume you already have these functions:
# - load_employee_graphs(base_dir, employee_name)
# - generate_employee_summary(api_key, employee_name, images)

BASE_DIR = "Employee Graphs"  # root folder containing employee subfolders
 # replace with your key

st.title("Employee Graph Insights Dashboard")

# Step 1: Select employee
employee_names = [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d))]
employee = st.selectbox("Select Employee", employee_names)

# Step 2: Generate button
if st.button("Generate Insights"):
    # Load graphs
    images = load_employee_graphs(BASE_DIR, employee)
    image_keys = list(images.keys())

    # Display graphs in 2x2 grid
    for i in range(0, len(image_keys), 2):
        cols = st.columns(2)
        for j in range(2):
            if i + j < len(image_keys):
                cols[j].image(images[image_keys[i + j]], caption=image_keys[i + j], width=300)
    
   
    # Generate insights using LLM
    summary = generate_graph_insights_openai(API_KEY,employee, images)

    # Display explanation below graphs
    st.subheader("LLM Insights")
    st.write(summary)



# import streamlit as st
# import os
# from PIL import Image

# # ---------- Helper Functions ----------

# def load_employee_graphs(base_dir: str, employee_name: str):
#     """
#     Load all graph images for a given employee.
#     Returns a dict {filename: PIL.Image}.
#     """
#     employee_dir = os.path.join(base_dir, employee_name)
#     image_files = [
#         f for f in os.listdir(employee_dir)
#         if f.lower().endswith((".png", ".jpg", ".jpeg"))
#     ]
#     images = {}
#     for img_file in sorted(image_files):
#         img_path = os.path.join(employee_dir, img_file)
#         images[img_file] = Image.open(img_path)
#     return images

# # ---------- Streamlit App ----------

# BASE_DIR = "employees"  # root folder containing employee subfolders

# st.title("📊 Employee Graph Insights Dashboard")

# # Employee selection
# employee_names = [d for d in os.listdir(BASE_DIR) if os.path.isdir(os.path.join(BASE_DIR, d))]
# employee = st.selectbox("Select Employee", employee_names)

# if st.button("Generate Insights"):
#     images = load_employee_graphs(BASE_DIR, employee)
#     image_keys = list(images.keys())

#     # Display graphs in 2x2 grid
#     for i in range(0, len(image_keys), 2):
#         cols = st.columns(2)
#         for j in range(2):
#             if i + j < len(image_keys):
#                 cols[j].image(images[image_keys[i + j]], caption=image_keys[i + j], width=300)

#     # Placeholder for LLM insights (replace with actual call)
#     summary = f"Insights generated for {employee}'s graphs will appear here."

#     # Styled insight box
#     st.markdown(
#         f"""
#         <div style="background-color:#f0f2f6; padding:15px; border-radius:8px; margin-top:20px;">
#             <h4 style="margin-top:0;">LLM Insights for {employee}</h4>
#             <p>{summary}</p>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )
