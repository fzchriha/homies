import * as React from "react";
import { styled } from "@mui/material/styles";
import Card from "@mui/material/Card";
import CardHeader from "@mui/material/CardHeader";
import CardMedia from "@mui/material/CardMedia";
import CardContent from "@mui/material/CardContent";
import CardActions from "@mui/material/CardActions";
import Collapse from "@mui/material/Collapse";
import Autocomplete from "@mui/material/Autocomplete";
import IconButton from "@mui/material/IconButton";
import Typography from "@mui/material/Typography";
import TextField from "@mui/material/TextField";
import FavoriteIcon from "@mui/icons-material/Favorite";
import ShareIcon from "@mui/icons-material/Share";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import MoreVertIcon from "@mui/icons-material/MoreVert";
import cn from "classnames";
import { states } from "./App";
import "./App.css";
import { format } from "date-fns";

// Add rest of states
const predictions = [
  {
    state: "AL",
    coef: [-6.3 / 100, 2.24 - 33.2, 261.9, -1147.1, 2461.9, 726.05, 161246.9],
  },
  {
    state: "AK",
    coef: [
      2.35 / 10,
      -11.19,
      201.7,
      -1825.6,
      8844,
      5,
      -21624.1,
      22835.9,
      266192.3,
    ],
  },
  {
    state: "AZ",
    coef: [1.5 / 10, -3.95, 40.5, -216.6, 553.4, -329.5, 5762.98, 345465.2],
  },
  {
    state: "AR",
    coef: [-1.7 / 10, 5.7, -74.5, 499.99, -1792.1, 3067.63, 316.55, 126197.6],
  },
  {
    state: "CA",
    coef: [7.3 / 10, -23.6, 312.22, -2113, 7147.2, -9993.2, 144670.8, 773128.5],
  },
  {
    state: "CO",
    coef: [-8.3 / 1000, 1.54, -38.8, 390.62, -1882.3, 3954.5, 5807.5, 4.93],
  },
  {
    state: "DE",
    coef: [2.74 / 10, -8.5, 105.4, -650.02, 1953.6, -2095.7, 5001.03, 400903.8],
  },
];
const predictPrice = (s, m) => {
  const prediction = predictions.find((p) => {
    return p.state === s;
  });

  if (!prediction) return;

  return (
    prediction.coef[0] * m ** 7 +
    prediction.coef[1] * m ** 6 +
    prediction.coef[2] * m ** 5 +
    prediction.coef[3] * m ** 4 +
    prediction.coef[4] * m ** 3 +
    prediction.coef[5] * m ** 2 +
    prediction.coef[6] * m +
    prediction.coef[7]
  ).toLocaleString("end-US", { style: "currency", currency: "USD" });
};

export const stateMatches = (m, budget) => {
  const monthValue = months.findIndex((month) => month.value === m) + 1;

  console.log({ monthValue });

  return predictions.filter((p) => {
    const price =
      p.coef[0] * monthValue ** 7 +
      p.coef[1] * monthValue ** 6 +
      p.coef[2] * monthValue ** 5 +
      p.coef[3] * monthValue ** 4 +
      p.coef[4] * monthValue ** 3 +
      p.coef[5] * monthValue ** 2 +
      p.coef[6] * monthValue +
      p.coef[7];
    console.log({ price, budget });

    return price <= budget;
  });
};

const ExpandMore = styled((props) => {
  const { expand, ...other } = props;
  return <IconButton {...other} />;
})(({ theme, expand }) => ({
  transform: !expand ? "rotate(0deg)" : "rotate(180deg)",
  marginLeft: "auto",
  transition: theme.transitions.create("transform", {
    duration: theme.transitions.duration.shortest,
  }),
}));

function USMap({ highlightedStates }) {
  const [expanded, setExpanded] = React.useState(false);
  const [state, setState] = React.useState("");
  const handleExpandClick = () => {
    setExpanded(!expanded);
  };
  // Add info of each state: Data Analysis, Increase percentage, Graph, Prediction of Prices in December

  const [month, setMonth] = React.useState(null);

  console.log({ highlightedStates });

  return (
    <section className="content">
      <svg
        id="usa-map"
        viewBox="0 0 959 593"
        preserveAspectRatio="xMidYMid"
        className="content"
      >
        <g>
          {states.map((state) => {
            return (
              <path
                pointerEvents="all"
                id={state.value}
                d={state.d}
                onClick={() => setState(state.value)}
                className={cn("ng-star-inserted", {
                  selected: !!highlightedStates.find(
                    (hs) => hs.state === state.value
                  ),
                })}
              >
                <title>{state.name}</title>
              </path>
            );
          })}
        </g>
      </svg>

      {!!state && (
        <Card sx={{ bgcolor: "#de8fe3b5" }}>
          <CardHeader
            action={
              <IconButton aria-label="settings">
                <MoreVertIcon />
              </IconButton>
            }
            title={states.find((s) => s.value === state)?.name} // I need the name of state I have states
            subheader={format(new Date(), "MMMM d, yyyy")}
          />
          <CardMedia
            component="img"
            height="194"
            image={state + ".png"}
            alt={state + "State"}
            id="stateAnalysis"
            width="90%"
          />

          <CardActions disableSpacing>
            <IconButton aria-label="add to favorites">
              <FavoriteIcon />
            </IconButton>
            <IconButton aria-label="share">
              <ShareIcon />
            </IconButton>
            <ExpandMore
              expand={expanded}
              onClick={handleExpandClick}
              aria-expanded={expanded}
              aria-label="show more"
            >
              <ExpandMoreIcon />
            </ExpandMore>
          </CardActions>
          <Collapse in={expanded} timeout="auto" unmountOnExit>
            <CardContent>
              <Typography paragraph>Prediction:</Typography>
              <Typography paragraph>{state}</Typography>
              <Autocomplete
                freeSolo
                id="free-solo-2-demo"
                disableClearable
                sx={{ width: 250, borderRadius: 20 }}
                options={months.map((option) => option.value)}
                onChange={(_, chosenMonth) => {
                  const monthValue =
                    months.findIndex((m) => m.value === chosenMonth) + 1;

                  setMonth(monthValue);
                }}
                renderInput={(params) => (
                  <TextField
                    {...params}
                    label="Choose month you want to move in:"
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
              {!!month && (
                <Typography paragraph>{predictPrice(state, month)}</Typography>
              )}
            </CardContent>
          </Collapse>
        </Card>
      )}
    </section>
  );
}

export const months = [
  {
    value: "January",
    label: "Jan",
  },
  {
    value: "February",
    label: "Feb",
  },
  {
    value: "March",
    label: "Mar",
  },
  {
    value: "April",
    label: "Apr",
  },
  {
    value: "May",
    label: "May",
  },
  {
    value: "June",
    label: "Jun",
  },
  {
    value: "July",
    label: "Jul",
  },
  {
    value: "August",
    label: "Aug",
  },
  {
    value: "September",
    label: "Sep",
  },
  {
    value: "October",
    label: "Oct",
  },
  {
    value: "November",
    label: "Nov",
  },
  {
    value: "December",
    label: "Dec",
  },
];

export default USMap;
