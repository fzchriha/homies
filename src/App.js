import * as React from "react";

import mainImage from "./imgMain.png";
import "./App.css";
import USMap from "./USMap";

function App() {
  return (
    <div className="App">
      <header className="App-header">HOMIES</header>

      <main>
        <section className="content">
          <p className="main-paragraph">
            Secure the <span className="pink-text">Right Spot</span> for the{" "}
            <span className="pink-text">Right Price</span>
          </p>
          {/* <label for="price">Enter your maximum price $</label>
          <input type="text" id="price" name="price"></input> */}

          <img src={mainImage} className="App-logo" alt="logo" />
        </section>
      </main>
      <USMap />

      {/* Table representing cheapest and most expansive cities */}

      {/* Prediction of prices in New jersey  */}
    </div>
  );
}

export default App;
