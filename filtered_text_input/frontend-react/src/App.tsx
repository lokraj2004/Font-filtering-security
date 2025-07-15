import React, { useEffect } from "react";
import { Streamlit, withStreamlitConnection } from "streamlit-component-lib";

const MyComponent = () => {
  useEffect(() => {
    Streamlit.setFrameHeight(); // Just in case Streamlit needs it
    console.log("📦 Component mounted & height set");
  }, []);

  const sendFilteredText = () => {
    const editor = document.getElementById("editor");
    let result = "";

    if (!editor) {
      console.warn("❌ Editor div not found!");
      return;
    }

    const processNode = (node: any) => {
      if (node.nodeType === Node.TEXT_NODE) {
        const parentFont = window.getComputedStyle(node.parentElement!).fontFamily;
        if (!/courier new/i.test(parentFont)) {
          result += node.textContent;
        }
      } else if (node.nodeType === Node.ELEMENT_NODE) {
        const font = window.getComputedStyle(node as HTMLElement).fontFamily;
        if (/courier new/i.test(font)) return;
        node.childNodes.forEach(processNode);
      }
    };

    Array.from(editor.childNodes).forEach(processNode);

    const finalText = result.trim();
    console.log("📤 Sending filtered text to Streamlit:", finalText);
    Streamlit.setComponentValue(finalText);
  };

  return (
    <div
      style={{
        // position: "fixed",
        // bottom: "15px",
        // left: "50%",
        transform: "translateX(-50%)",
        width: "90%",
        maxWidth: "800px",
        zIndex: "9999",
        backgroundColor: "white",
        // borderRadius: "12px",
        // boxShadow: "0 2px 8px rgba(0,0,0,0.15)",
        // padding: "1em",
      }}
    >
      <div
        id="editor"
        contentEditable
        style={{
          minHeight: "100px",
          maxHeight: "160px",
          padding: "100px",
          fontSize: "16px",
          borderRadius: "8px",
          border: "1px solid #ccc",
          overflowY: "auto",
        }}
      />
      <div style={{ textAlign: "right", marginTop: "8px" }}>
        <button
          onClick={sendFilteredText}
          style={{
            // position:"fixed",
            padding: "6px 16px",
            background: "#4CAF50",
            color: "white",
            border: "none",
            borderRadius: "6px",
            cursor: "pointer",
            fontWeight: "bold",
          }}
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default withStreamlitConnection(MyComponent);
