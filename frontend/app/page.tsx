"use client";

import { useEffect, useState } from "react";

type Season = {
  id: number;
  number: number;
};

export default function Home() {
  const [seasons, setSeasons] = useState<Season[]>([]);

  useEffect(() => {
    const fetchEpisodes = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8000/fetch-seasons/");
        const data = await response.json();
        setSeasons(data);
        console.log(data);
      } catch (error) {
        console.error("Error fetching episodes:", error);
      }
    };

    fetchEpisodes();
  }, []);

  return (
    <main>
      <h1>Jose</h1>
      <ul>
        {seasons.map((season) => (
          <li key={season.id}>{season.number}</li>
        ))}
      </ul>
    </main>
  );
}
