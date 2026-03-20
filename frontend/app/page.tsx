'use client';

import { useState, useRef } from 'react';

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [uploading, setUploading] = useState(false);
  const [processingStatus, setProcessingStatus] = useState('');
  const [query, setQuery] = useState('');
  const [messages, setMessages] = useState<{ role: 'user' | 'ai'; text: string }[]>([]);
  const [loading, setLoading] = useState(false);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFile = e.target.files?.[0];
    if (!selectedFile) return;

    setFile(selectedFile);
    setUploading(true);
    setProcessingStatus('Uploading and processing PDF...');

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      const response = await fetch('http://localhost:8000/upload', {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();
      if (response.ok) {
        setProcessingStatus(data.message);
      } else {
        setProcessingStatus(`Error: ${data.detail}`);
      }
    } catch (error) {
      setProcessingStatus('Error connecting to backend.');
      console.error(error);
    } finally {
      setUploading(false);
    }
  };

  const handleAsk = async () => {
    if (!query.trim()) return;

    setMessages((prev) => [...prev, { role: 'user', text: query }]);
    const currentQuery = query;
    setQuery('');
    setLoading(true);

    try {
      const response = await fetch(`http://localhost:8000/ask?query=${encodeURIComponent(currentQuery)}`, {
        method: 'POST',
      });

      const data = await response.json();
      if (response.ok) {
        setMessages((prev) => [...prev, { role: 'ai', text: data.response }]);
      } else {
        setMessages((prev) => [...prev, { role: 'ai', text: `Error: ${data.detail}` }]);
      }
    } catch (error) {
      setMessages((prev) => [...prev, { role: 'ai', text: 'Error connecting to backend.' }]);
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main>
      <h1 style={{ marginBottom: '2rem', fontSize: '2.5rem', fontWeight: 'bold', background: 'linear-gradient(to right, #60a5fa, #3b82f6)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent' }}>
        AI PDF Navigator
      </h1>

      <div className="glass-card">
        <div className="upload-section" onClick={() => fileInputRef.current?.click()}>
          <input
            type="file"
            accept=".pdf"
            onChange={handleUpload}
            ref={fileInputRef}
            style={{ display: 'none' }}
          />
          <p>{file ? file.name : 'Click or Drag PDF to Upload'}</p>
          {processingStatus && (
            <p style={{ fontSize: '0.8rem', marginTop: '0.5rem', color: uploading ? '#60a5fa' : '#34d399' }}>
              {processingStatus}
            </p>
          )}
        </div>

        <div className="chat-history">
          {messages.length === 0 && (
            <p style={{ textAlign: 'center', opacity: 0.5, marginTop: '5rem' }}>
              Upload a PDF and start asking questions!
            </p>
          )}
          {messages.map((msg, index) => (
            <div key={index} className={`message ${msg.role}`}>
              {msg.text}
            </div>
          ))}
          {loading && (
            <div className="message ai">
              <div className="loading-dots">
                <span>.</span><span>.</span><span>.</span>
              </div>
            </div>
          )}
        </div>

        <div className="input-group">
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleAsk()}
            placeholder="Ask about the document..."
            disabled={!file || uploading}
          />
          <button onClick={handleAsk} disabled={!file || uploading || loading}>
            Ask
          </button>
        </div>
      </div>
    </main>
  );
}
