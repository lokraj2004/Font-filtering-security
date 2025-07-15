import React from "react"
import ReactDOM from "react-dom/client"
import FilteredTextInput from "./FilteredTextInput"
console.log("✅ index.tsx loaded")
const container = document.getElementById("root")!

if (!container) {
  console.error("❌ Root container not found")
} else {
  const root = ReactDOM.createRoot(container)
  console.log("✅ React root created")



root.render(
  <React.StrictMode>
    <FilteredTextInput />
  </React.StrictMode>
)
}
