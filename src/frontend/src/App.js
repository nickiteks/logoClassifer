import "./App.css";
import { Routes, Route } from "react-router-dom";
import { useState } from "react";
import Results from "./Blocks/Results";
import Home from "./Blocks/Home";

function App() {
  const [predictionData, setPredictionData] = useState([]);
  return (
    <div className="App">
      <Routes>
        <Route path="/" exact element={<Home setPredictionData={setPredictionData}/>} />
        <Route path="/results" exact element={<Results predictionData={predictionData}/>} />
      </Routes>
    </div>
  );
}

export default App;
