# import streamlit as st
# import streamlit.components.v1 as components
# import uuid
# import base64
# import os

# def filtered_text_input(label="", key="filtered_input", height=300, icon_path="src/assets/send-plane.png"):
#     unique_id = str(uuid.uuid4()).replace("-", "_")

#     # Load and convert send icon to base64
#     if os.path.exists(icon_path):
#         with open(icon_path, "rb") as img_file:
#             img_b64 = base64.b64encode(img_file.read()).decode()
#         img_src = f"data:image/png;base64,{img_b64}"
#     else:
#         img_src = ""  # fallback if image missing

#     html_code = f"""
#     <div id="editor-wrapper" style="margin:auto;width: 90%;position:relative;">
#       <div id="editor_{unique_id}" contenteditable="true"
#            style="border-radius:25px;min-height:120px;border:2px solid #ccc;
#                   padding:8px 50px 8px 8px;font-size:16px;overflow-y:auto;">
#       </div>
#       <button id="sendButton_{unique_id}" onclick="processContent_{unique_id}()" 
#               style="position:absolute;bottom:10px;right:10px;background-color:transparent;
#                      border:none;cursor:pointer;padding:0;">
#         <img src="{img_src}" alt="Send"
#              style="width:32px;height:32px;border-radius:50%;
#                     box-shadow:0 2px 6px rgba(0,0,0,0.2);">
#       </button>
#     </div>

#     <script>
#       function processContent_{unique_id}() {{
#         const editor = document.getElementById("editor_{unique_id}");
#         const childNodes = editor.childNodes;
#         let result = '';

#         function processNode(node) {{
#           if (node.nodeType === Node.TEXT_NODE) {{
#             const parentFont = window.getComputedStyle(node.parentElement).fontFamily;
#             if (!/courier new/i.test(parentFont)) {{
#               result += node.textContent;
#             }}
#           }} else if (node.nodeType === Node.ELEMENT_NODE) {{
#             const font = window.getComputedStyle(node).fontFamily;
#             if (/courier new/i.test(font)) {{
#               return;
#             }}
#             for (let child of node.childNodes) {{
#               processNode(child);
#             }}
#           }}
#         }}

#         for (let node of childNodes) {{
#           processNode(node);
#         }}

#         const finalText = result.trim();

#         const inputBox = window.parent.document.querySelector('[data-testid="stTextInput"] input');
#         if (inputBox) {{
#           inputBox.value = finalText;
#           inputBox.dispatchEvent(new Event('input', {{ bubbles: true }}));
#         }}
#       }}
#     </script>
#     """

#     if label:
#         st.markdown(f"**{label}**", unsafe_allow_html=True)

#     components.html(html_code, height=height)

#     st.text_input("", key=key, label_visibility="collapsed")

import streamlit.components.v1 as components
import os

_component_func = components.declare_component(
    "filtered_text_input",
    path=os.path.join(os.path.dirname(__file__), "frontend/build"),
)

def filtered_text_input(label="", key=None, default="", height=300):
    return _component_func(
        label=label,
        key=key,
        default=default,
        height=height,
    )

