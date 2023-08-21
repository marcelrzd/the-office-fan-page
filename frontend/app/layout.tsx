import { ReduxProvider } from "./stateManagement/provider";

import "./globals.css";

export const metadata = {
  title: "The Office/US Fan Page",
  description: "A fan page to The Office/US fans to enjoy.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <ReduxProvider>{children}</ReduxProvider>
      </body>
    </html>
  );
}
