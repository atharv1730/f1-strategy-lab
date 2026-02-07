"use client"; // runs the file in the browser and not the server

import { useEffect, useState } from "react";

export default function Home() {
  const [status, setStatus] = useState("loading...");

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_URL}/health`)
      .then((res) => res.json())
      .then((data) => setStatus(data.status))
      .catch(() => setStatus("error"));
  }, []);

  return (
    <main style={{ padding: 24 }}>
      <h1>F1 Strategy Lab</h1>
      <p>Backend status: {status}</p>
    </main>
  );
}
