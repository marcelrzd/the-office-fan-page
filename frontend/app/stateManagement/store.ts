import { configureStore, ThunkAction, Action } from "@reduxjs/toolkit";
import randomQuoteReducer from "./features/randomQuoteSlice";

export const store = configureStore({
  reducer: {
    randomQuoteReducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
export type AppThunk<ReturnType = void> = ThunkAction<
  ReturnType,
  RootState,
  unknown,
  Action<string>
>;
