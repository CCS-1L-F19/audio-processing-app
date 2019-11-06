# audio_processing_app
An audio processing app that processes live microphone data and displays spectrograms, audio metrics, etc

## Accessing the webapp
The most up to date version of the webapp is hosted on a Github Pages site, [https://ccs-1l-f19.github.io/audio-processing-app/](https://ccs-1l-f19.github.io/audio-processing-app/). For now the landing page contains links to several demo pages. The current main project is the live spectrogram page. 

## Modifying the source code
All the webapp's files are stored in the docs folder of this repo. 

index.html is a simple page that contains links. The page under active development is in spectrogram.html. The HTML body is currently contains only several elements and is layed out with Bootstrap (in progress). The script block is mostly contained in an asyncronous block that depends on the getUserMedia call, which requests microphone data from the device through the browser. The script then initializes a Google chart and updates it periodically with a setInterval() call to updateSpectrogram().

generate-scales is a simple Python script that generates a javascript object containing 2 parallel arrays of frequencies and the names of the corresponding notes.



## [AudioContext-MonkeyPatch](https://github.com/cwilso/AudioContext-MonkeyPatch/)

This is an open source patch by Chris Wilson referenced in MDN documentation ([https://developer.mozilla.org/en-US/docs/Web/Guide/Audio_and_video_delivery/Web_Audio_API_cross_browser](https://developer.mozilla.org/en-US/docs/Web/Guide/Audio_and_video_delivery/Web_Audio_API_cross_browser)). It is required to offer compatibility with browsers including Safari which require the webkit prefix on Web Audio API to function. I have copied AudioContext-MonkeyPatch.js directly into my repository because the URL to include it from the web is not HTTPS, which some browsers do not like when allowing microphone access.

## [Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)
This MDN API provides a stream of microphone data and includes an Analyser Node which performs a Fast Fourier Transform on the raw audio to calculate frequency data. 
