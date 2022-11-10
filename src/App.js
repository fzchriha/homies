import * as React from "react";
import Paper from "@mui/material/Paper";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";
import TextField from "@mui/material/TextField";
import Autocomplete from "@mui/material/Autocomplete";
import Divider from "@mui/material/Divider";
import CircularProgress from "@mui/material/CircularProgress";
import Fab from "@mui/material/Fab";
import SearchIcon from "@mui/icons-material/Search";
import mainImage from "./imgMain.png";
import { styled } from "@mui/material/styles";
import "./App.css";
import USMap from "./USMap";

function App() {
  const Item = styled(Paper)(({ theme }) => ({
    ...theme.typography.body2,
    textAlign: "center",
    color: "white",
    // height: 80,
    // lineHeight: "80px",
    margin: "auto",
    marginTop: "100px",
    width: "70%",
    backgroundColor: "#de90e3",
  }));
  const [price, setPrice] = React.useState("");
  const handleChange = (event) => {
    setPrice(event.target.value);
  };
  const states = [
    { value: "AK", name: "Alaska" },
    { value: "TX", name: "Texas" },
    { value: "AL", name: "Alabama" },
    { value: "AR", name: "Arkansas" },
    { value: "AZ", name: "Arizona" },
    { value: "CA", name: "California" },
    { value: "CO", name: "Colorado" },
    { value: "CT", name: "Connecticut" },
    { value: "DC", name: "DistrictofColumbia" },
    { value: "DE", name: "Delaware" },
    { value: "FL", name: "Florida" },
    { value: "GA", name: "Georgia" },
    { value: "HI", name: "Hawaii" },
    { value: "IA", name: "Iowa" },
    { value: "ID", name: "Idaho" },
    { value: "IL", name: "Illinois" },
    { value: "IN", name: "Indiana" },
    { value: "KS", name: "Kansas" },
    { value: "KY", name: "Kentucky" },
    { value: "LA", name: "Louisiana" },
    { value: "MA", name: "Massachusetts" },
    { value: "MD", name: "Maryland" },
    { value: "ME", name: "Maine" },
    { value: "MI", name: "Michigan" },
    { value: "MN", name: "Minnesota" },
    { value: "MO", name: "Missouri" },
    { value: "MS", name: "Mississippi" },
    { value: "MT", name: "Montana" },
    { value: "NC", name: "NorthCarolina" },
    { value: "ND", name: "NorthDakota" },
    { value: "NE", name: "Nebraska" },
    { value: "NH", name: "NewHampshire" },
    { value: "NJ", name: "NewJersey" },
    { value: "NM", name: "NewMexico" },
    { value: "NV", name: "Nevada" },
    { value: "NY", name: "NewYork" },
    { value: "OH", name: "Ohio" },
    { value: "OK", name: "Oklahoma" },
    { value: "OR", name: "Oregon" },
    { value: "PA", name: "Pennsylvania" },
    { value: "RI", name: "RhodeIsland" },
    { value: "SC", name: "SouthCarolina" },
    { value: "SD", name: "SouthDakota" },
    { value: "TN", name: "Tennessee" },
    { value: "TX", name: "Texas" },
    { value: "UT", name: "Utah" },
    { value: "VA", name: "Virginia" },
    { value: "VT", name: "Vermont" },
    { value: "WA", name: "Washington" },
    { value: "WI", name: "Wisconsin" },
    { value: "WV", name: "WestVirginia" },
    { value: "WY", name: "Wyoming" },
  ];
  const prices = [
    {
      value: "100000",
      label: "100k",
    },
    {
      value: "200000",
      label: "200k",
    },
    {
      value: "300000",
      label: "300k",
    },
    {
      value: "400000",
      label: "400k",
    },
    {
      value: "500000",
      label: "500k",
    },
  ];
  return (
    <div className="App">
      <header className="App-header">HOMIES</header>

      <main className="page">
        <section className="content">
          <p className="main-paragraph">
            Secure the <span className="pink-text">Right Spot</span> for the{" "}
            <span className="pink-text">Right Price</span>
            <Item
              elevation={3}
              className="content"
              sx={{ padding: 2, borderRadius: 5 }}
            >
              <Autocomplete
                freeSolo
                id="free-solo-2-demo"
                disableClearable
                sx={{ width: 400, borderRadius: 20 }}
                options={prices.map((option) => option.value)}
                renderInput={(params) => (
                  <TextField
                    {...params}
                    label="What is Your Budget?"
                    className="input"
                    color="secondary"
                    sx={{ borderRadius: 5 }}
                    InputProps={{
                      ...params.InputProps,
                      type: "Budget",
                    }}
                  />
                )}
              />
              <Fab color="secondary" aria-label="add">
                <SearchIcon />
              </Fab>
            </Item>
          </p>

          <img src={mainImage} className="App-logo" alt="logo" />
        </section>
        {/* <CircularProgress
          color="secondary"
          className="progress"
          sx={{ margin: 500 }}
        /> */}
        <Divider />
      </main>

      <USMap />

      {/* Table representing cheapest and most expansive cities */}

      {/* Prediction of prices in New jersey  */}
    </div>
  );
}

export default App;
