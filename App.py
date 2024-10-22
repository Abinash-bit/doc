import os
import cv2
import streamlit as st
from paddleocr import PPStructure, save_structure_res, draw_structure_result
from PIL import Image

# Define the function for 'Image orientation + Table recognition + layout analysis'
def process_image_orientation_table_layout(img_path, save_folder, font_path):
    table_engine = PPStructure(show_log=True, image_orientation=True)
    img = cv2.imread(img_path)
    result = table_engine(img)
    save_structure_res(result, save_folder, os.path.basename(img_path).split('.')[0])

    for line in result:
        line.pop('img')
        st.write(line)
    
    image = Image.open(img_path).convert('RGB')
    im_show = draw_structure_result(image, result, font_path=font_path)
    im_show = Image.fromarray(im_show)
    im_show.save(os.path.join(save_folder, 'result.jpg'))
    st.image(im_show, caption="Processed Image")

# Define the function for 'Table recognition'
def process_table_recognition(img_path, save_folder):
    table_engine = PPStructure(layout=False, show_log=True)
    img = cv2.imread(img_path)
    result = table_engine(img)
    save_structure_res(result, save_folder, os.path.basename(img_path).split('.')[0])

    for line in result:
        line.pop('img')
        st.write(line)

# Define the function for 'Layout analysis'
def process_layout_analysis(img_path, save_folder):
    table_engine = PPStructure(table=False, ocr=False, show_log=True)
    img = cv2.imread(img_path)
    result = table_engine(img)
    save_structure_res(result, save_folder, os.path.basename(img_path).split('.')[0])

    for line in result:
        line.pop('img')
        st.write(line)

# Streamlit app
st.title("Table Recognition and Layout Analysis App")

# Sidebar menu
option = st.sidebar.radio("Choose a Process", 
                              ('Image orientation + Table recognition + layout analysis', 
                               'Table recognition', 
                               'Layout analysis'))

# Upload an image file
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    img_path = os.path.join('./', uploaded_file.name)
    with open(img_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    save_folder = './output'
    os.makedirs(save_folder, exist_ok=True)
    
    font_path = '/home/zclap/research/Abinash/timesbd.ttf'  # Update font path as necessary

    # Process based on the selected option
    if option == 'Image orientation + Table recognition + layout analysis':
        process_image_orientation_table_layout(img_path, save_folder, font_path)
    elif option == 'Table recognition':
        process_table_recognition(img_path, save_folder)
    elif option == 'Layout analysis':
        process_layout_analysis(img_path, save_folder)

    st.success(f"Process complete. Output saved in {save_folder}.")
else:
    st.warning("Please upload an image.")
