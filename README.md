# audio_processing_app
An audio processing app that processes live microphone data and displays spectrograms, audio metrics, etc

## Accessing the webapp
The most up to date version of the webapp is hosted on this repository's website, [https://ccs-1l-f19.github.io/audio-processing-app/](https://ccs-1l-f19.github.io/audio-processing-app/). For now the landing page contains links to several demo pages. The current main project is the live spectrogram page. 

## Modifying the source code
All the webapp's files are stored in the docs folder of this repo. 

index.html is a simple page that contains links. The live spectrogram page is in spectrogram.html.



## [AudioContext-MonkeyPatch](https://github.com/cwilso/AudioContext-MonkeyPatch/)

This is an open source patch by Chris Wilson referenced in MDN documentation ([https://developer.mozilla.org/en-US/docs/Web/Guide/Audio_and_video_delivery/Web_Audio_API_cross_browser](https://developer.mozilla.org/en-US/docs/Web/Guide/Audio_and_video_delivery/Web_Audio_API_cross_browser)). It is required to offer compatibility with browsers including Safari which require the webkit prefix on Web Audio API to function. I have copied AudioContext-MonkeyPatch.js directly into my repository because the URL to include it from the web is not HTTPS, which some browsers do not like when allowing microphone access.

## [Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API)
This MDN API handles receiving microphone 
