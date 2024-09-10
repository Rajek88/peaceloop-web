import os
import requests

# List of URLs to download
urls = [
    
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A0v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C1v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Ds1v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Fs1v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A1v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C2v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Ds2v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Fs2v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A2v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C3v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Ds3v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Fs3v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A3v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C4v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Ds4v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Fs4v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A4v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C5v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Ds5v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Fs5v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A5v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C6v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Ds6v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Fs6v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A6v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C7v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Ds7v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Fs7v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A7v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C8v1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A0v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C1v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Ds1v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Fs1v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A1v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C2v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Ds2v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Fs2v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A2v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C3v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Ds3v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Fs3v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A3v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C4v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Ds4v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Fs4v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A4v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C5v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Ds5v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Fs5v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A5v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C6v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Ds6v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Fs6v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A6v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C7v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Ds7v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Fs7v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A7v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C8v5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A0v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C1v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Ds1v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Fs1v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A1v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C2v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Ds2v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Fs2v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A2v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C3v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Ds3v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Fs3v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A3v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C4v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Ds4v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Fs4v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A4v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C5v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Ds5v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Fs5v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A5v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C6v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Ds6v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Fs6v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A6v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C7v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Ds7v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Fs7v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A7v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C8v10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A0v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C1v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Ds1v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Fs1v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A1v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C2v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Ds2v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Fs2v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A2v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C3v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Ds3v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Fs3v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A3v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C4v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Ds4v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Fs4v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A4v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C5v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Ds5v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Fs5v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A5v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C6v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Ds6v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Fs6v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A6v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C7v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Ds7v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/Fs7v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/A7v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/C8v15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/pedalU1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/pedalD1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/harmLA0.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/harmLC1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/harmLDs1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/harmLFs1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/harmLA1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/harmLC2.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/harmLDs2.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/harmLFs2.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/harmLA2.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/harmLC3.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/harmLDs3.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/harmLFs3.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/harmLA3.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/harmLC4.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/harmLDs4.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/harmLFs4.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/harmLA4.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/harmLC5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/harmLDs5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/harmLFs5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/harmLA5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/harmLC6.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/harmLDs6.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel1.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel2.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel3.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel4.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel5.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel6.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel7.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel8.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel9.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel10.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel11.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel12.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel13.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel14.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel15.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel16.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel17.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel18.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel19.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel20.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel21.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel22.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel23.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel24.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel25.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel26.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel27.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel28.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel29.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel30.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel31.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel32.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel33.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel34.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel35.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel36.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel37.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel38.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel39.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel40.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel41.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel42.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel43.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel44.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel45.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel46.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel47.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel48.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel49.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel50.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel51.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel52.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel53.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel54.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel55.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel56.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel57.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel58.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel59.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel60.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel61.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel62.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel63.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel64.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel65.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel66.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel67.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel68.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel69.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel70.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel71.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel72.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel73.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel74.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel75.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel76.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel77.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel78.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel79.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel80.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel81.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel82.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel83.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel84.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel85.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel86.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel87.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/demos/SalamanderPiano/rel88.mp3",
"https://storage.googleapis.com/download.magenta.tensorflow.org/models/performance_rnn/tfjs/weights_manifest.json",
"https://storage.googleapis.com/download.magenta.tensorflow.org/models/performance_rnn/tfjs/group1-shard1of6",
"https://storage.googleapis.com/download.magenta.tensorflow.org/models/performance_rnn/tfjs/group1-shard2of6",
"https://storage.googleapis.com/download.magenta.tensorflow.org/models/performance_rnn/tfjs/group1-shard3of6",
"https://storage.googleapis.com/download.magenta.tensorflow.org/models/performance_rnn/tfjs/group1-shard4of6",
"https://storage.googleapis.com/download.magenta.tensorflow.org/models/performance_rnn/tfjs/group1-shard5of6",
"https://storage.googleapis.com/download.magenta.tensorflow.org/models/performance_rnn/tfjs/group1-shard6of6"
]

# Define the folder to save the files
download_folder = "downloads"

# Create the folder if it doesn't exist
os.makedirs(download_folder, exist_ok=True)

# Function to download a file
def download_file(url, folder):
    local_filename = os.path.join(folder, url.split("/")[-1])
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"Downloaded: {local_filename}")

# Download all files
for url in urls:
    try:
        download_file(url, download_folder)
    except Exception as e:
        print(f"Failed to download {url}: {e}")

print("All downloads completed.")
