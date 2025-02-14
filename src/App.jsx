import { useState } from "react";
import * as RadixDialog from "@radix-ui/react-dialog";

export default function ManimGenerator() {
  const [prompt, setPrompt] = useState("");
  const [videoUrl, setVideoUrl] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const generateManim = async () => {
    setLoading(true);
    setError(null);
    setVideoUrl(null);

    try {
      const response = await fetch("http://127.0.0.1:5000/api/generate_manim", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ prompt }),
      });

      const data = await response.json();
      if (response.ok) {
        setVideoUrl(`http://127.0.0.1:5000${data.video_url}`);
      } else {
        setError(data.error || "Failed to generate animation");
      }
    } catch (err) {
      setError("An error occurred while processing your request.");
    }
    setLoading(false);
  };

  return (
    <div className="flex flex-col items-center p-4 space-y-4">
      <RadixDialog.Root>
        <RadixDialog.Trigger asChild>
          <button className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600">
            Open Generator
          </button>
        </RadixDialog.Trigger>
        <RadixDialog.Portal>
          <RadixDialog.Overlay className="fixed inset-0 bg-black bg-opacity-50" />
          <RadixDialog.Content className="fixed top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 bg-white p-6 rounded-lg shadow-lg">
            <input
              type="text"
              placeholder="Enter prompt..."
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              className="w-full p-2 border rounded mb-2"
            />
            <button
              onClick={generateManim}
              disabled={loading}
              className="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600 disabled:bg-gray-400"
            >
              {loading ? "Generating..." : "Generate Animation"}
            </button>
          </RadixDialog.Content>
        </RadixDialog.Portal>
      </RadixDialog.Root>

      {error && <p className="text-red-500">{error}</p>}
      {videoUrl && (
        <div className="mt-4">
          <video controls width="500">
            <source src={videoUrl} type="video/mp4" />
            Your browser does not support the video tag.
          </video>
        </div>
      )}
    </div>
  );
}