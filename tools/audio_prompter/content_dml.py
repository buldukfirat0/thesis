# DML.txt -> item list.
# Each item: (display_text, spoken_text or None)
# Wording is kept from /home/firat/Desktop/thesis/thesis-draft/talk/DML.txt.
# Long sentences are split at clause boundaries only; no meaning is changed.

PARTS = [
 {
  "num": "1",
  "name": "What a DFB laser is",
  "sections": [
    ("THE DEVICE", [
      ("Distributed feedback lasers, abbreviated as DFB lasers, are semiconductor light sources that emit optical power at a single wavelength and maintain a stable continuous wave output.", None),
      ("The device is built as a p-i-n structure.", "The device is built as a P I N structure."),
      ("The lower layers are doped n type and therefore carry free electrons.", None),
      ("The upper layers are doped p type and therefore carry holes.", None),
      ("Between these two doped regions there is an undoped region containing a multiple quantum well structure, abbreviated as MQW.", None),
    ]),
    ("GAIN", [
      ("When a forward bias is applied across the structure, electrons are injected from the n side and holes are injected from the p side, and both are confined within the undoped region in the middle.", None),
      ("Inside that region an electron recombines with a hole, and the energy released by this recombination is emitted as a photon.", None),
      ("If a photon that is already travelling through the region triggers this recombination, then the newly emitted photon is identical to it in wavelength, in phase and in direction of propagation.", None),
      ("This process is known as stimulated emission, and its consequence is that light leaves the region with greater power than it possessed on entering.", None),
      ("This amplification of the optical field is what is meant by gain.", None),
    ]),
    ("WHY GAIN IS NOT ENOUGH", [
      ("Gain by itself is not sufficient to produce a laser, because the light must be returned through the amplifying region repeatedly so that its power can accumulate over many passes.", None),
      ("The mechanism that returns the light in this way is called feedback.", None),
      ("Gain is also available over a broad range of wavelengths, typically several tens of nanometres, so that the multiple quantum well region amplifies many wavelengths simultaneously.", None),
      ("In a conventional laser diode the feedback is provided by the two cleaved end facets of the crystal, and because these facets reflect all wavelengths with equal strength, they are unable to distinguish between them.", None),
    ]),
    ("THE BRAGG GRATING", [
      ("A distributed feedback laser resolves this problem by generating the feedback inside the waveguide itself, and by making that feedback dependent on wavelength.", None),
      ("The refractive index of a material, written as n, determines the speed at which light propagates within it, since that speed is equal to c divided by n.", None),
      ("The grating is constructed from a difference in this quantity.", None),
      ("Along the direction in which the light travels the structure alternates between two materials whose refractive indices differ slightly from one another.", None),
      ("This alternation repeats at a fixed spacing over the entire length of the waveguide.", None),
      ("The light propagating through the device therefore does not encounter a constant refractive index, but rather a value that alternates continually between two levels.", None),
      ("The spacing at which this alternation repeats is called the period and is written as Lambda.", None),
      ("It is smaller than the wavelength of the light itself, so that a laser only a few hundred micrometres in length contains many thousands of periods.", None),
      ("A periodic variation of the refractive index constructed in this manner is called a Bragg grating.", None),
    ]),
    ("THE BRAGG WAVELENGTH", [
      ("Only the wavelength that matches this period returns in step with itself and therefore receives feedback.", None),
      ("That wavelength is given by lambda_B = 2 * n_eff * Lambda.",
       "That wavelength is given by lambda B equals two times n effective times Lambda."),
      ("Every other wavelength cancels itself out and consequently never reaches the lasing condition, so that a single wavelength alone leaves the device.", None),
    ]),
  ],
 },
 {
  "num": "2",
  "name": "Direct modulation",
  "sections": [
    ("THRESHOLD AND BIAS", [
      ("The device does not emit laser light until the injected current exceeds a particular value known as the threshold current.", None),
      ("Above that value the optical output power increases steadily and predictably with every further increase in current.", None),
      ("The laser is supplied with a constant bias current that lies above the threshold, so that it remains in the lasing regime at all times and never has to be started from rest.", None),
    ]),
    ("WRITING THE DATA ONTO THE CURRENT", [
      ("The binary data is then superimposed on that bias current as a smaller alternating component.", None),
      ("The total injected current rises whenever a 1 is transmitted and falls whenever a 0 is transmitted, while remaining above the threshold in both cases.", None),
      ("Because the optical output power follows the injected current, the emitted light becomes brighter during a 1 and dimmer during a 0, and the binary sequence is therefore written directly onto the intensity of the optical signal.", None),
    ]),
    ("RECEIVER AND NAMING", [
      ("The photodetector at the far end of the optical fibre measures the received optical power and reconstructs the original sequence from the difference between the two levels.", None),
      ("No additional component is required anywhere in this process, since the device that generates the light is also the device that carries the information.", None),
      ("This is precisely why a laser operated in this manner is described as directly modulated and is abbreviated as a DML.", None),
    ]),
  ],
 },
 {
  "num": "3",
  "name": "The problems",
  "sections": [
    ("THE COMMON ORIGIN", [
      ("This method of encoding data is simple and requires no additional components, but it brings three problems with it.", None),
      ("All three originate in the same fact, which is that the injected current controls considerably more than the optical output power alone.", None),
    ]),
    ("PROBLEM 1 - CHIRP", [
      ("The first problem is chirp.", None),
      ("Changing the injected current also changes the refractive index inside the laser.", None),
      ("Since the emitted wavelength is fixed by that refractive index through the relation lambda_B = 2 * n_eff * Lambda, the wavelength shifts every time a bit changes.",
       "Since the emitted wavelength is fixed by that refractive index through the relation lambda B equals two times n effective times Lambda, the wavelength shifts every time a bit changes."),
      ("Because different wavelengths propagate through an optical fibre at different speeds, this shifting causes the transmitted bits to spread out in time and to interfere with one another, which limits the distance over which the signal can be sent.", None),
    ]),
    ("PROBLEM 2 - LIMITED MODULATION SPEED", [
      ("The second problem is the limited modulation speed.", None),
      ("The optical field inside the cavity cannot follow an abrupt change in the injected current instantaneously, because it requires a finite time to build up and to decay.", None),
      ("Above a certain frequency the optical output can no longer follow the electrical input, and this places an upper bound on the bit rate at which the device can be operated.", None),
    ]),
    ("PROBLEM 3 - WEAK EXTINCTION", [
      ("The third problem is the weak extinction.", None),
      ("The current cannot be switched off in order to represent a 0, because restarting the laser from rest would take far longer than the duration of a single bit, and the current is therefore only reduced rather than removed.", None),
      ("The 0 level consequently still carries significant optical power, so that the difference between the two levels, known as the extinction ratio, remains small.", None),
    ]),
  ],
 },
 {
  "num": "4",
  "name": "Transition to the EML",
  "sections": [
    ("ONE DEVICE, TWO TASKS", [
      ("Every one of these limitations arises because a single device is being asked to perform two different tasks at the same time, namely generating the optical carrier and imposing the data upon it.", None),
      ("The solution is to separate the two tasks.", None),
    ]),
    ("THE SEPARATED ARCHITECTURE", [
      ("The distributed feedback laser is operated at a constant current, under which condition it produces exactly the clean single-wavelength continuous wave output that it is designed to produce.", None),
      ("A second element is placed in the optical path after it whose only function is to transmit or to block the light that reaches it.", None),
      ("That second element is an electro-absorption modulator, abbreviated as an EAM.", None),
      ("A device in which the laser and the modulator are fabricated together on a single chip is called an electro-absorption modulated laser, abbreviated as an EML.", None),
    ]),
  ],
 },
]

VOICES = {
  "steffan": "en-US-SteffanNeural",
  "guy": "en-US-GuyNeural",
  "christopher": "en-US-ChristopherNeural",
  "eric": "en-US-EricNeural",
  "ava": "en-US-AvaNeural",
}
