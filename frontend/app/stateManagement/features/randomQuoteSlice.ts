import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import axios from "axios";
import { AppThunk } from "../store";

type InitialState = {
  value: RandomQuoteState;
};

type RandomQuoteState = {
  quote: string[];
};

const initialState: InitialState = {
  value: {
    quote: [],
  },
};

export const randomQuoteSlice = createSlice({
  name: "randomQuote",
  initialState,
  reducers: {
    getQuote(state, action: PayloadAction<string[]>) {
      state.value.quote = action.payload;
    },
  },
});

export const { getQuote } = randomQuoteSlice.actions;

export const fetchRandomQuote = (): AppThunk => async (dispatch) => {
  try {
    const response = await axios.get(
      "http://127.0.0.1:8000/fetch-random-quote/"
    );
    dispatch(getQuote(response.data));
  } catch (error) {
    // Handle error if necessary
  }
};

export default randomQuoteSlice.reducer;
