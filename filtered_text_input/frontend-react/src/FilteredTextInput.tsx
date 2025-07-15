import { relative } from "path"
import React, { useEffect, useRef } from "react"
import { Streamlit, withStreamlitConnection } from "streamlit-component-lib"
console.log("🧪 hi FilteredTextInput mounted")
const FilteredTextInput = () => {
  const editorRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    console.log("🧪 FilteredTextInput mounted")
    // Let Streamlit know about the height
    Streamlit.setFrameHeight(180)
  }, [])

  const processText = () => {
    let result = ""
    const editor = editorRef.current

    if (!editor) {
      console.warn("Editor not found")
      return
    }

    const processNode = (node: ChildNode) => {
      if (node.nodeType === Node.TEXT_NODE) {
        const font = window.getComputedStyle((node.parentElement || editor)).fontFamily
        if (!/courier new/i.test(font)) {
          result += node.textContent || ""
        }
      } else if (node.nodeType === Node.ELEMENT_NODE) {
        const font = window.getComputedStyle(node as HTMLElement).fontFamily
        if (/courier new/i.test(font)) return
        node.childNodes.forEach(processNode)
      }
    }

    editor.childNodes.forEach(processNode)

    const filtered = result.trim()
    console.log("🚀 Sending filtered content:", filtered)
    Streamlit.setComponentValue(filtered)
  }

 return (
    <div
      style={{
         position: "fixed",
  bottom: "15px",
  left: "50%",
  transform: "translateX(-50%)",
  width: "90%",
  maxWidth: "800px",
  border: "2px solid #ccc",
  borderRadius: "25px",
  minHeight: "120px",
  padding: "8px 50px 8px 12px",  // Space for the send button
  backgroundColor: "#fff",
  boxSizing: "border-box",
  zIndex: 9999,
      }}
    >
      <div
        ref={editorRef}
        contentEditable
        style={{
          fontSize: "16px",
          minHeight: "100px",
          outline: "none",
          overflowY: "auto",
        }}
        onInput={() => {}}
      />
      <button
        onClick={processText}
        style={{
          position: "absolute",
          bottom: "12px",
          right: "12px",
          backgroundColor: "transparent",
          border: "none",
          cursor: "pointer",
        }}
      >
        <img
          src="send-plane.png"
          alt="Send"
          style={{
            width: "30px",
            height: "30px",
            borderRadius: "50%",
            boxShadow: "0 1px 4px rgba(0,0,0,0.2)",
          }}
        />
      </button>
    </div>
  )
}
export default withStreamlitConnection(FilteredTextInput)
