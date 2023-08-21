"use client";

import { useDispatch, useSelector } from "react-redux";
import { fetchRandomQuote } from "../stateManagement/features/randomQuoteSlice";
import { AppDispatch } from "../stateManagement/store";
import { useEffect, useState } from "react";

export default function Quote() {
  const dispatch = useDispatch<AppDispatch>();
  const quote = useSelector((state) => state.randomQuoteReducer.value.quote);

  useEffect(() => {
    dispatch(fetchRandomQuote());
  }, []);

  //   Check if quote is not empty
  if (quote.length === 0) {
    return <p></p>;
  }

  return (
    <div>
      <h1>{quote.character.name}</h1>
      <h2>{quote.quote}</h2>
    </div>
  );
}
