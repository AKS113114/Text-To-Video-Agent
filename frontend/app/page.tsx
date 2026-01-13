// "use client";

// import { useState } from 'react';
// import { toast } from 'react-hot-toast';

// export default function Home() {
//   const [prompt, setPrompt] = useState('');
//   const [selectedStyle, setSelectedStyle] = useState('cinematic');
//   const [isGenerating, setIsGenerating] = useState(false);
//   const [currentVideo, setCurrentVideo] = useState<string | null>(null);

//   const styles = [
//     { id: 'cinematic', label: 'Cinematic' },
//     { id: 'animation', label: 'Animation' },
//     { id: 'realistic', label: 'Realistic' },
//     { id: 'artistic', label: 'Artistic' },
//   ];

//   const handleGenerate = async () => {
//     if (!prompt.trim()) {
//       toast.error('Please enter a prompt');
//       return;
//     }

//     setIsGenerating(true);
//     const loadingToast = toast.loading('Generating video...');

//     try {
//       const response = await fetch('http://127.0.0.1:8000/generate', {
//         method: 'POST',
//         headers: { 'Content-Type': 'application/json' },
//         body: JSON.stringify({ prompt, style: selectedStyle, duration: 4 })
//       });

//       const data = await response.json();
//       setCurrentVideo(data.video_url);
//       toast.success('Video generated!', { id: loadingToast });
      
//     } catch (error) {
//       console.error('Error:', error);
//       const videos = [
//         "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerJoyrides.mp4",
//         "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4",
//       ];
//       setCurrentVideo(videos[Math.floor(Math.random() * videos.length)]);
//       toast.success('Demo video loaded!', { id: loadingToast });
//     } finally {
//       setIsGenerating(false);
//     }
//   };

//   return (
//     <div className="min-h-screen bg-gradient-to-br from-gray-900 to-black p-8">
//       <div className="max-w-6xl mx-auto">
//         {/* Header */}
//         <header className="mb-8">
//           <div className="mb-4 p-4 bg-gradient-to-r from-blue-900/30 to-purple-900/30 rounded-2xl">
//             <p className="text-blue-300 text-center">
//               🚀 <strong>Text-to-Video Agent</strong> • Working Demo
//             </p>
//           </div>
//           <h1 className="text-4xl font-bold text-white mb-2">🎬 Text to Video Agent</h1>
//           <p className="text-gray-400">Transform text into videos with AI</p>
//         </header>

//         <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
//           {/* Left: Controls */}
//           <div className="bg-gray-800/50 backdrop-blur-lg rounded-2xl p-6 border border-gray-700">
//             <h2 className="text-xl font-semibold text-white mb-4">Describe Your Video</h2>
            
//             <textarea
//               value={prompt}
//               onChange={(e) => setPrompt(e.target.value)}
//               placeholder="Try: dog walking, car drifting, office work..."
//               className="w-full h-40 p-4 bg-gray-900/70 border border-gray-600 rounded-xl text-white placeholder-gray-500 resize-none mb-6"
//               disabled={isGenerating}
//             />
            
//             <div className="mb-6">
//               <h3 className="text-lg font-medium text-white mb-3">Video Style</h3>
//               <div className="grid grid-cols-2 gap-3">
//                 {styles.map((style) => (
//                   <button
//                     key={style.id}
//                     onClick={() => setSelectedStyle(style.id)}
//                     disabled={isGenerating}
//                     className={`p-4 rounded-xl transition-all ${
//                       selectedStyle === style.id
//                         ? 'bg-blue-600 text-white shadow-lg'
//                         : 'bg-gray-900 hover:bg-gray-800 text-gray-300'
//                     }`}
//                   >
//                     {style.label}
//                   </button>
//                 ))}
//               </div>
//             </div>
            
//             <button
//               onClick={handleGenerate}
//               disabled={isGenerating || !prompt.trim()}
//               className="w-full py-4 bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 disabled:opacity-50 rounded-xl font-bold text-lg text-white transition-all"
//             >
//               {isGenerating ? 'Generating...' : '🚀 Generate Video'}
//             </button>
            
//             <div className="mt-4 p-4 bg-blue-900/20 rounded-xl">
//               <p className="text-blue-300 text-sm">
//                 <span className="text-yellow-400">ℹ️</span>{' '}
//                 <strong>Backend Connected:</strong> http://127.0.0.1:8000
//               </p>
//             </div>
//           </div>

//           {/* Right: Video Player */}
//           <div className="bg-gray-800/50 backdrop-blur-lg rounded-2xl p-6 border border-gray-700">
//             <h2 className="text-xl font-semibold text-white mb-4">Generated Video</h2>
            
//             {isGenerating ? (
//               <div className="aspect-video bg-gray-900/50 rounded-xl flex items-center justify-center">
//                 <div className="text-center">
//                   <div className="animate-spin rounded-full h-16 w-16 border-t-2 border-b-2 border-blue-500 mx-auto mb-4"></div>
//                   <p className="text-gray-400">Generating video...</p>
//                   <p className="text-gray-500 text-sm mt-2">Connecting to AI backend</p>
//                 </div>
//               </div>
//             ) : currentVideo ? (
//               <div className="space-y-4">
//                 <div className="aspect-video bg-black rounded-xl overflow-hidden">
//                   <video
//                     key={currentVideo}
//                     className="w-full h-full"
//                     controls
//                     autoPlay
//                     preload="auto"
//                   >
//                     <source src={currentVideo} type="video/mp4" />
//                   </video>
//                 </div>
                
//                 <div className="flex justify-between items-center">
//                   <button
//                     onClick={() => window.open(currentVideo, '_blank')}
//                     className="px-6 py-3 bg-blue-600 hover:bg-blue-700 rounded-xl text-white font-medium"
//                   >
//                     ⬇️ Download Video
//                   </button>
                  
//                   <div className="text-right">
//                     <p className="text-green-500 text-sm">✅ Ready to play</p>
//                     <p className="text-gray-400 text-xs">
//                       {currentVideo.includes('ForBiggerFun') ? '🐶 Animal Video' :
//                        currentVideo.includes('ForBiggerJoyrides') ? '🏎️ Car Video' :
//                        '🎬 General Video'}
//                     </p>
//                   </div>
//                 </div>
//               </div>
//             ) : (
//               <div className="aspect-video bg-gradient-to-br from-gray-900 to-black rounded-xl border-2 border-dashed border-gray-700 flex items-center justify-center">
//                 <div className="text-center">
//                   <div className="w-24 h-24 bg-gray-800 rounded-full flex items-center justify-center mx-auto mb-4">
//                     <span className="text-4xl text-gray-600">🎬</span>
//                   </div>
//                   <p className="text-gray-500">Your video will appear here</p>
//                   <p className="text-gray-600 text-sm mt-2">Enter a prompt and click generate</p>
//                 </div>
//               </div>
//             )}
//           </div>
//         </div>

//         <div className="mt-8 grid grid-cols-1 md:grid-cols-3 gap-4">
//           <div className="bg-gray-800/30 p-4 rounded-xl">
//             <p className="text-green-400 font-semibold">✅ Backend Connected</p>
//             <p className="text-gray-400 text-sm">http://127.0.0.1:8000</p>
//           </div>
//           <div className="bg-gray-800/30 p-4 rounded-xl">
//             <p className="text-blue-400 font-semibold">🚀 Ready for AI APIs</p>
//             <p className="text-gray-400 text-sm">Replicate • RunwayML • Hugging Face</p>
//           </div>
//           <div className="bg-gray-800/30 p-4 rounded-xl">
//             <p className="text-purple-400 font-semibold">📦 Assignment Complete</p>
//             <p className="text-gray-400 text-sm">Full-stack working prototype</p>
//           </div>
//         </div>

//         <footer className="mt-8 pt-6 border-t border-gray-800 text-center text-gray-500">
//           <p>Text to Video Agent • Ready for Submission</p>
//         </footer>
//       </div>
//     </div>
//   );
// }


// new// import type { Metadata } from "next";

"use client";

import { useState } from "react";
import { toast } from "react-hot-toast";

export default function Home() {
  const [prompt, setPrompt] = useState("");
  const [style, setStyle] = useState("cinematic");
  const [isGenerating, setIsGenerating] = useState(false);
  const [videoURL, setVideoURL] = useState<string | null>(null);
  const [enhancedPrompt, setEnhancedPrompt] = useState<string | null>(null);

  const styles = [
    { id: "cinematic", label: "Cinematic 🎥" },
    { id: "animation", label: "Animation 🧸" },
    { id: "realistic", label: "Realistic 📷" },
    { id: "artistic", label: "Artistic 🎨" },
  ];

  const generateVideo = async () => {
    if (!prompt.trim()) return toast.error("Please enter a prompt!");

    setIsGenerating(true);
    const t = toast.loading("Generating... this may take a few seconds");

    try {
      const res = await fetch("http://127.0.0.1:8000/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt, style }),
      });

      const data = await res.json();

      if (!res.ok) throw new Error(data.detail || "Failed");

      setVideoURL(data.video_url);
      setEnhancedPrompt(data.enhanced_prompt);

      toast.success("Video Generated Successfully!", { id: t });
    } catch (err) {
      console.error(err);
      toast.error("Backend unavailable — playing a demo video", { id: t });

      // fallback demo video
      setVideoURL(
        "https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4"
      );
    } finally {
      setIsGenerating(false);
    }
  };

  return (
    <div className="min-h-screen p-8 bg-gray-950 text-white">
      <div className="max-w-6xl mx-auto">

        {/* HEADER */}
        <div className="text-center mb-10">
          <h1 className="text-4xl font-bold mb-2">🎬 Text-to-Video Generator</h1>
          <p className="text-gray-400">Turn your imagination into moving visuals.</p>
        </div>

        {/* GRID */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">

          {/* LEFT PANEL */}
          <div className="bg-gray-900 p-6 rounded-2xl border border-gray-700">
            <h2 className="text-xl font-semibold mb-4">Describe Your Scene</h2>

            <textarea
              className="w-full h-36 p-4 bg-gray-800 rounded-xl border border-gray-600 text-white mb-5"
              placeholder="Example: a golden retriever walking through a park during sunset"
              disabled={isGenerating}
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
            />

            <h3 className="text-lg font-medium mb-3">Select Style</h3>
            <div className="grid grid-cols-2 gap-3 mb-6">
              {styles.map((s) => (
                <button
                  key={s.id}
                  disabled={isGenerating}
                  onClick={() => setStyle(s.id)}
                  className={`p-3 rounded-xl border transition ${
                    style === s.id
                      ? "bg-blue-600 border-blue-500 text-white"
                      : "bg-gray-800 border-gray-700 text-gray-300 hover:bg-gray-700"
                  }`}
                >
                  {s.label}
                </button>
              ))}
            </div>

            <button
              disabled={isGenerating}
              onClick={generateVideo}
              className="w-full py-4 bg-blue-600 hover:bg-blue-700 rounded-xl font-bold disabled:opacity-50"
            >
              {isGenerating ? "Processing..." : "🚀 Generate Video"}
            </button>

            <p className="text-xs text-gray-500 mt-3">
              Connected to backend: <span className="text-green-400">http://127.0.0.1:8000</span>
            </p>
          </div>

          {/* RIGHT PANEL */}
          <div className="bg-gray-900 p-6 rounded-2xl border border-gray-700">
            <h2 className="text-xl font-semibold mb-4">Output</h2>

            {!videoURL ? (
              <div className="aspect-video flex items-center justify-center border-2 border-dashed border-gray-600 rounded-xl">
                <p className="text-gray-500">Your generated video will appear here</p>
              </div>
            ) : (
              <div className="space-y-4">
                <video className="w-full rounded-xl" controls autoPlay>
                  <source src={videoURL} type="video/mp4" />
                </video>

                {enhancedPrompt && (
                  <div className="text-xs bg-gray-800 p-3 rounded-lg border border-gray-700">
                    <span className="text-gray-400">Enhanced Prompt:</span><br />
                    <span className="text-blue-300">{enhancedPrompt}</span>
                  </div>
                )}

                <button
                  onClick={() => window.open(videoURL, "_blank")}
                  className="w-full py-3 bg-purple-600 rounded-xl hover:bg-purple-700 font-medium"
                >
                  ⬇️ Download Video
                </button>
              </div>
            )}
          </div>
        </div>

        {/* FOOTER */}
        <div className="text-center text-gray-500 mt-10">
          <p>Assignment • Full-Stack AI Demo • {new Date().getFullYear()}</p>
        </div>
      </div>
    </div>
  );
}
