# Finding Signal From Noise

## Finding Signal From Noise

Our world is bathed in a variety of signals and spectrums: acoustic, electromagnetic, chemical. The increasing digitization of data, commoditization of advanced sensors, and the use of AI to parse through complexity in search of signal, is allowing for increasingly clever ways of uncovering patterns in noise, with implications for privacy and communication. This is my living repository of some creative ways of finding signal.

Acoustic

[Power grid](https://robertheaton.com/enf/): each power grid hums with a unique and fingerprintable acoustic signal, which can be used to timestamp any recording.

[Digital voiceprinting](https://spectrum.ieee.org/digital-forensics): is someone's voice a unique fingerprint? (a bit skeptical, as it gives me graphology vibes i.e. human personality from signatures, but I don't know enough to judge its validity)

[Animal translation](https://www.nytimes.com/2022/08/30/science/translators-animals-naked-mole-rats.html): AI is being used to tackle the most difficult problems in linguistics - speaking to animals

Some of the most creative analyses in terms of extracting signal from noise are cybersecurity researchers who work on side-channel attacks e.g.

[Using phone vibrations](https://www.allaboutcircuits.com/news/eavesdropping-side-channel-attack-can-spy-through-phone-vibrations/) or [computer fans](https://arxiv.org/abs/1606.05915) from air-gapped devices

[Using infrared lasers to input commands into smart home speakers like Alexa](https://arstechnica.com/information-technology/2019/11/researchers-hack-siri-alexa-and-google-home-by-shining-lasers-at-them/)

[Use ground-based seismometers to track atmospheric re-entry of satellite debris](https://nautil.us/i-track-space-debris-as-it-crashes-to-earth-1263197/).

Electromagnetic

[Using AI to estimate human pose from Wifi](https://www.ri.cmu.edu/publications/dense-human-pose-estimation-from-wifi/), with obvious implications for surveillance e.g. tracking someone in a crowded mall using ubiquitous Wifi or special operations e.g. knowing what position everyone is standing or sitting in inside of a room

[See around walls](https://www.pnas.org/doi/10.1073/pnas.2024468118): non-line-of-sight imaging allows one to indirectly image what is "around the corner" through extracting signal from diffuse light reflections

[A mere photograph of someone's face can reveal what they're looking at through their retina reflection](https://world-from-eyes.github.io/) (using NERF techniques)

[We can remotely sense temperature through high-precision timestamps associated with internet packets.](http://caia.swin.edu.au/talks/CAIA-TALK-080728A.pdf)

[With a single photo, AI models (and top Geoguessr players) can determine your location to a high degree of accuracy](https://arxiv.org/abs/2307.05845)

[Measuring acoustically driven optical phase shifts in pulses sent through subsea cables to detect ships passing overhead](https://x.com/yohaniddawela/status/2031705951552647195).

[Covertly transmit information by rapidly switching a photodiode between forward-bias electroluminescence and reverse-bias negative luminescence](https://www.nature.com/articles/s41377-025-02119-y), so that the time-averaged emission exactly matches the thermal background — invisible to any detector lacking sufficient bandwidth.

Biological

Environmental DNA: [everyone is shedding microscopic amounts of DNA everywhere they go](https://www.nytimes.com/2023/05/15/science/environmental-dna-ethics-privacy.html). Researchers are increasingly able to extract population-scale and individual-scale information, with surveillance implications. Funny enough, it originally originated from environmental sciences trying to study animal populations and movements

[Finding the Golden State Killer](https://www.science.org/content/article/we-will-find-you-dna-search-used-nab-golden-state-killer-can-home-about-60-white): well-reported already but still worth emphasizing how biological information is a commons problem and just because you haven't played into the system, doesn't mean the system isn't playing with you. Pretty incredible the inferences we can make once we hit critical mass of population-scale data c.f. [China](https://www.nytimes.com/2020/06/17/world/asia/China-DNA-surveillance.html)

Fingerprinting agricultural products for supply chain integrity: [using microscopic DNA strands as "physically unclonable functions" to verify the authenticity of seeds, cotton products, etc](https://ambrook.com/research/technology/counterfeit-seeds-soybeans-maize-africa) which is just the physically instantiated version of public key encryption from cybersecurity [[NYT](https://www.nytimes.com/2023/04/07/business/economy/ai-tech-dna-supply-chain.html)]

[Measuring heart rate from cameras by detecting blood flow i.e. photoplethysmography](https://x.com/Zebo_Furqatzoda/status/1952171796716982469)

[Recovering audio from crumpling chip bag through pixel fluctuations](https://x.com/bzogrammer/status/1952179437002481809)

Plants as surveillance: [DARPA program exploring using plants as chemical sensors e.g. nuclear non-proliferation, chemical warfare](https://www.darpa.mil/news-events/2017-11-17). Benefits include that plants can be easily inserted via seed drops, blend in as sensors with actual plants, and can provide detection signals easily e.g. through dying, leaf color change, etc

Unrelatedly, I just want to say plants are very cool. They have a variety of signalling and networking mechanisms that we barely understand to communicate with another and not enough has been done to explore these abilities. They [scream in ultrasound](https://www.sciencenews.org/article/plant-stress-ultrasonic-click-noise-sound), communicate through the [emission of volatile organic compounds](https://www.sciencenews.org/article/plant-stress-ultrasonic-click-noise-sound), and have networks of fungi connecting them to each other in unknown ways. Also, we can use certain [plants to mine for critical minerals](https://charlesxjyang.github.io/assets/phytomining%20RFI%20response.pdf) aka phytomining.
