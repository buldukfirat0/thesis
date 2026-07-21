# önemliydi.txt / önemliydi2.txt -> item list.
# Each item: (display_text, spoken_text or None)
# Wording is kept from /home/firat/Desktop/thesis/thesis-draft/learn/önemliydi.txt
# and /home/firat/Desktop/thesis/thesis-draft/learn/önemliydi2.txt.
# Long sentences are split at clause boundaries only; no meaning is changed.

PARTS = [
    {
        "num": "1",
        "name": "What a DFB laser is",
        "sections": [
            (
                "THE DEVICE",
                [
                    (
                        "DFB laser is a semiconductor light source that operates under forward bias, to generate stable continuous wave light.",
                        None,
                    ),
                    (
                        "The device is basically built as a p-i-n structure.",
                        "The device is basically built as a P I N structure.",
                    ),
                    (
                        "We doped the p layers with p type semiconductor materials, which have an excess of holes, and n layers with n type semiconductors, which have an excess of electrons.",
                        None,
                    ),
                    (
                        "\"i\" means intrinsic, and we do not have any impurities there, no doping is introduced in this region.",
                        None,
                    ),
                    (
                        "Here, the DFB laser has a MQW structure in the intrinsic region.",
                        "Here, the DFB laser has a multiple quantum well structure in the intrinsic region.",
                    ),
                ],
            ),
            (
                "INJECTING CARRIERS",
                [
                    (
                        "Let's apply a forward bias to this junction and inject electrical carriers into the device.",
                        None,
                    ),
                    (
                        "Specifically, this forward bias reduces the electric field barrier at the junction, which lets electrons diffuse in from the n side and holes diffuse in from the p side, injecting them into the intrinsic region.",
                        None,
                    ),
                    (
                        "Once these carriers enter the intrinsic region, they are captured by the quantum wells.",
                        None,
                    ),
                    (
                        "Here electrons and holes find themselves confined to quantized energy states.",
                        None,
                    ),
                ],
            ),
            (
                "GAIN",
                [
                    (
                        "In these wells, the electrons and holes recombine and release energy in the form of photons, and it's specifically the stimulated emission part of this recombination that creates the optical gain.",
                        None,
                    ),
                ],
            ),
            (
                "FEEDBACK",
                [
                    (
                        "But gain alone is not enough to generate laser beams, so we need feedback.",
                        None,
                    ),
                    (
                        "In conventional lasers, this feedback effect comes from mirrors, but here we use diffraction grating, and this diffraction grating provides wavelength selective feedback based on the Bragg condition.",
                        None,
                    ),
                ],
            ),
            (
                "THE GRATING",
                [
                    (
                        "The Bragg condition is a formulation that determines which precise wavelength of light is reflected.",
                        None,
                    ),
                    (
                        "To prevent competing modes and guarantee stable single-mode lasing, a quarter-wave phase shift is placed at the center of the cavity.",
                        None,
                    ),
                ],
            ),
        ],
    },
    {
        "num": "2",
        "name": "Direct modulation",
        "sections": [
            (
                "THE STABLE BEAM",
                [
                    (
                        "OK, we get a stable laser beam at a specific wavelength, which in our case is thirteen ten nanometers.",
                        None,
                    ),
                ],
            ),
            (
                "HOW TO SEND DATA",
                [
                    (
                        "Now we want to use this laser to send data.",
                        None,
                    ),
                    (
                        "How do we do that?",
                        None,
                    ),
                ],
            ),
            (
                "MODULATING THE CURRENT",
                [
                    (
                        "One method is to modulate the laser directly.",
                        None,
                    ),
                    (
                        "We keep the injected current above the threshold current at all times, so the laser never actually turns off.",
                        None,
                    ),
                    (
                        "On top of this bias, we add a smaller current, and we change that extra current depending on the bit we want to send.",
                        None,
                    ),
                ],
            ),
            (
                "WRITING THE BITS",
                [
                    (
                        "When we send a 1, we push the current up a bit, and the optical output gets brighter.",
                        None,
                    ),
                    (
                        "When we send a 0, we pull the current down a bit, but we stay above threshold, so the laser stays on and the output just gets dimmer.",
                        None,
                    ),
                    (
                        "This way, the binary data is written directly onto the intensity of the light, and this is why we call this method direct modulation.",
                        None,
                    ),
                ],
            ),
        ],
    },
    {
        "num": "3",
        "name": "The three problems",
        "sections": [
            (
                "THE THREE REASONS",
                [
                    (
                        "There are three reasons for this: chirp, extinction ratio, and speed.",
                        None,
                    ),
                ],
            ),
            (
                "CHIRP",
                [
                    (
                        "The first is chirp.",
                        None,
                    ),
                    (
                        "Chirp is the unwanted shift in the laser's wavelength while we modulate it, and it happens because changing the current changes the density of carriers in the active region, and the refractive index of the semiconductor depends on that carrier density, so the wavelength shifts every time we switch bits.",
                        None,
                    ),
                ],
            ),
            (
                "EXTINCTION RATIO",
                [
                    (
                        "The second is extinction ratio.",
                        None,
                    ),
                    (
                        "Extinction ratio is the ratio of the optical power in our 1 level to the optical power in our 0 level, P1 divided by P0.",
                        "Extinction ratio is the ratio of the optical power in our 1 level to the optical power in our 0 level, P one divided by P zero.",
                    ),
                    (
                        "Optical power is the rate at which electromagnetic energy flows through a surface, measured in watts.",
                        None,
                    ),
                    (
                        "It stays small because restarting the laser from below threshold takes a finite time, set by the carrier lifetime, which is longer than a single bit period, so we can only lower the current, never remove it, and the 0 level still carries significant power.",
                        None,
                    ),
                ],
            ),
            (
                "SPEED",
                [
                    (
                        "The third is speed.",
                        None,
                    ),
                    (
                        "This is the upper limit on how fast we can switch bits, and it happens because the carrier density and the photon density inside the cavity are coupled to each other, so when we suddenly change the current, the optical power doesn't settle instantly, it oscillates for a while before settling.",
                        None,
                    ),
                    (
                        "This oscillation is called the relaxation oscillation, and its frequency sets an upper bound on the bit rate we can use.",
                        None,
                    ),
                ],
            ),
        ],
    },
    {
        "num": "4",
        "name": "From DML to EML",
        "sections": [
            (
                "ONE DEVICE, TWO JOBS",
                [
                    (
                        "So all three problems come from the same root cause: we're asking one single device to do two jobs at once, generate the light and carry the data.",
                        None,
                    ),
                    (
                        "The fix is to split these two jobs apart.",
                        None,
                    ),
                ],
            ),
            (
                "THE EAM AND EML",
                [
                    (
                        "We run the DFB laser at a constant current, so it just does what it does best, produce a clean, stable, single-wavelength beam.",
                        None,
                    ),
                    (
                        "Then we place a second device right after it, whose only job is to let the light through or block it.",
                        None,
                    ),
                    (
                        "That second device is called an electro-absorption modulator, an EAM, and when we put the laser and the EAM together on the same chip, we call the whole thing an electro-absorption modulated laser, an EML.",
                        None,
                    ),
                ],
            ),
            (
                "MY THESIS",
                [
                    (
                        "This is where my own thesis fits in.",
                        None,
                    ),
                    (
                        "For the last six months, the part I've been working on is exactly this second section, the EAM.",
                        None,
                    ),
                    (
                        "So from here on, we zoom into just that piece.",
                        None,
                    ),
                    (
                        "We'll look at what's physically inside it, what happens there when we apply a voltage, and what I've actually done with it in my simulations.",
                        None,
                    ),
                ],
            ),
        ],
    },
    {
        "num": "5",
        "name": "The EAM, layer by layer",
        "sections": [
            (
                "SLIDE 1 - THE TWO SECTIONS",
                [
                    (
                        "Here we have our two sections side by side, the DFB laser and the EAM, before they're combined onto one chip.",
                        None,
                    ),
                    (
                        "They're grown from exactly the same layer stack, the same n doped indium phosphide base, the same active multiple quantum well region, everything identical.",
                        None,
                    ),
                ],
            ),
            (
                "SLIDE 2 - THE SUBSTRATE",
                [
                    (
                        "We start from a single crystal wafer of indium phosphide, doped n type.",
                        None,
                    ),
                    (
                        "This is the substrate everything else grows on.",
                        None,
                    ),
                    (
                        "On top of it we grow an n doped indium phosphide buffer layer, about 800 nanometers thick, which gives us a clean starting surface for the rest of the growth.",
                        None,
                    ),
                    (
                        "On the back of the wafer we deposit a gold contact, and both the DFB section and the EAM section share this common ground.",
                        None,
                    ),
                ],
            ),
            (
                "SLIDE 3 - THE N-SIDE WAVEGUIDE LAYERS",
                [
                    (
                        "Next we grow four thin layers of aluminum gallium indium arsenide, 20 nanometers each, on top of the buffer.",
                        None,
                    ),
                    (
                        "This is the n-side separate confinement heterostructure.",
                        None,
                    ),
                    (
                        "Aluminum gallium indium arsenide has a higher refractive index than indium phosphide, so this is actually where our optical waveguide core begins to form.",
                        None,
                    ),
                    (
                        "We change the composition gradually across these four layers instead of jumping straight from indium phosphide to the active region, so we avoid one abrupt heterojunction.",
                        None,
                    ),
                ],
            ),
            (
                "SLIDE 4 - THE INTRINSIC REGION",
                [
                    (
                        "Now the intrinsic region, the key part of the device.",
                        None,
                    ),
                    (
                        "We'll look into this more deeply in the following slides, but simply, this part consists of eight wells and nine barriers, with a total thickness of one hundred and forty six nanometers.",
                        None,
                    ),
                ],
            ),
            (
                "SLIDE 5 - THE P-SIDE CONFINEMENT LAYERS",
                [
                    (
                        "On top of the intrinsic region we grow the p-side confinement layers, the mirror of what we did on the n side, but now p doped.",
                        None,
                    ),
                    (
                        "One of these layers is different: it's aluminum indium arsenide, with a wider bandgap than the layers around it, and this wider bandgap creates an energy barrier that blocks electrons from leaking out of the active region into the p side.",
                        None,
                    ),
                ],
            ),
            (
                "SLIDE 6 - THE P-DOPED CLADDING",
                [
                    (
                        "Above that we grow the p doped indium phosphide cladding, four separate indium phosphide layers, and the doping level changes as we go up.",
                        None,
                    ),
                    (
                        "Right next to the active region we keep the doping low, because heavily doped material there would absorb some of our light through free holes.",
                        None,
                    ),
                    (
                        "Close to the contact, we raise the doping a lot, because that's what gives us low series resistance.",
                        None,
                    ),
                    (
                        "This thick indium phosphide layer is also what closes off our waveguide from the top.",
                        None,
                    ),
                ],
            ),
            (
                "SLIDE 7 - THE P-SIDE CONTACT",
                [
                    (
                        "Finally we need an electrical contact on the p side.",
                        None,
                    ),
                    (
                        "Metal placed directly on indium phosphide would form a Schottky junction, a rectifying contact, and that's not what we want, we want current to pass freely in both directions.",
                        None,
                    ),
                    (
                        "So we add an aluminum gallium indium arsenide band-step layer, then a heavily doped indium gallium arsenide layer, and only then the gold contact pad on top.",
                        None,
                    ),
                    (
                        "This gives us the ohmic contact we need, matching the backside ground on the n side.",
                        None,
                    ),
                ],
            ),
            (
                "SLIDE 8 - THE RIDGE ETCH",
                [
                    (
                        "The last step isn't growth, it's etching.",
                        None,
                    ),
                    (
                        "We etch the structure down into a narrow ridge, and this etch cuts all the way through the multiple quantum well.",
                        None,
                    ),
                    (
                        "This ridge confines our light laterally, so we end up with a single guided optical mode centered right on our intrinsic region.",
                        None,
                    ),
                ],
            ),
        ],
    },
    {
        "num": "6",
        "name": "EAM physics under reverse bias",
        "sections": [
            (
                "THE FIELD",
                [
                    (
                        "So far, we've only built the physical structure, layer by layer.",
                        None,
                    ),
                    (
                        "We haven't actually connected any voltage to it yet.",
                        None,
                    ),
                    (
                        "Now let's do that, and see what happens when we apply a reverse bias.",
                        None,
                    ),
                    (
                        "When we apply a reverse bias to the EAM, several things happen, in this order.",
                        None,
                    ),
                    (
                        "Under reverse bias, almost no current flows through the device.",
                        None,
                    ),
                    (
                        "Because there's no current, the intrinsic region becomes fully depleted, meaning there are no free carriers left inside it to screen the applied voltage.",
                        None,
                    ),
                    (
                        "Since nothing screens it, the entire voltage we apply drops across that one thin intrinsic layer.",
                        None,
                    ),
                    (
                        "And because that layer is only about 146 nanometers thick, even a few volts across it produces an enormous electric field, on the order of 80 to 130 kilovolts per centimeter.",
                        None,
                    ),
                    (
                        "So the first thing reverse bias does is turn a small, ordinary voltage into a huge electric field, simply because the layer it's dropped across is so thin.",
                        None,
                    ),
                ],
            ),
            (
                "WELLS AND THE EXCITON",
                [
                    (
                        "Now, that intrinsic region isn't a single uniform layer, it's the multiple quantum well we built earlier, alternating thin layers of a smaller-bandgap material, the wells, and a larger-bandgap material, the barriers.",
                        None,
                    ),
                    (
                        "Because the wells are so thin, an electron trapped inside one can only occupy certain discrete energy levels, quantum confinement forces this.",
                        None,
                    ),
                    (
                        "The same applies to a hole.",
                        None,
                    ),
                    (
                        "Now, an electron and a hole attract each other electrostatically, and inside a well they can actually bind together into a pair, we call this pair an exciton.",
                        None,
                    ),
                    (
                        "This exciton produces a sharp, well-defined peak in the absorption spectrum, right at the edge where absorption begins, and this peak is the feature the entire modulator is built around.",
                        None,
                    ),
                    (
                        "In a bulk semiconductor this exciton peak is weak, and a field destroys it easily.",
                        None,
                    ),
                    (
                        "But inside a quantum well, the barriers keep the electron and the hole pinned close together, so the exciton survives even under the strong field we just built up.",
                        None,
                    ),
                    (
                        "That's exactly why we use a multiple quantum well here instead of a bulk layer.",
                        None,
                    ),
                ],
            ),
            (
                "THE QUANTUM CONFINED STARK EFFECT",
                [
                    (
                        "So now we have this large field, and we have excitons living inside these wells, tied to a sharp absorption peak.",
                        None,
                    ),
                    (
                        "What does the field actually do to them?",
                        None,
                    ),
                    (
                        "It tilts the potential energy inside every well, so the well is no longer flat, one side becomes lower in energy than the other.",
                        None,
                    ),
                    (
                        "Because of this tilt, the electron's energy level moves down, and the hole's energy level moves up, so the energy difference between them, the transition energy, gets smaller.",
                        None,
                    ),
                    (
                        "A smaller energy difference corresponds to a longer wavelength, so the absorption edge shifts towards longer wavelengths, we call this a red shift.",
                        None,
                    ),
                    (
                        "At the same time, the tilted potential pushes the electron and the hole toward opposite sides of the well, so their wavefunctions no longer overlap as much, and this weakens the transition, the absorption peak becomes lower and broader.",
                        None,
                    ),
                    (
                        "These two effects together, the red shift of the edge and the weakening of the peak, are what we call the quantum confined Stark effect, and it's the physical mechanism this entire device is built on.",
                        None,
                    ),
                ],
            ),
            (
                "THE RESULT",
                [
                    (
                        "We operate this device at 1310 nanometers, and we deliberately choose this wavelength to sit just below the absorption edge when there's no bias applied.",
                        "We operate this device at thirteen ten nanometers, and we deliberately choose this wavelength to sit just below the absorption edge when there's no bias applied.",
                    ),
                    (
                        "At low reverse bias, the edge hasn't shifted onto our operating wavelength yet, so the absorption at 1310 nanometers stays low, and light passes through, this is our on state.",
                        "At low reverse bias, the edge hasn't shifted onto our operating wavelength yet, so the absorption at thirteen ten nanometers stays low, and light passes through, this is our on state.",
                    ),
                    (
                        "As we increase the reverse bias, the quantum confined Stark effect pulls that edge further, until it moves onto 1310 nanometers, the absorption there rises sharply, and the light gets absorbed instead, this is our off state.",
                        "As we increase the reverse bias, the quantum confined Stark effect pulls that edge further, until it moves onto thirteen ten nanometers, the absorption there rises sharply, and the light gets absorbed instead, this is our off state.",
                    ),
                    (
                        "But the field isn't the only thing that decides how much light we actually lose.",
                        None,
                    ),
                    (
                        "The light travels through the device as a guided optical mode, and only part of that mode physically overlaps with the wells, we call that fraction the confinement factor.",
                        None,
                    ),
                    (
                        "So the transmitted power in the end depends on three things together: the absorption coefficient at that bias point, the confinement factor, and the physical length of the device.",
                        None,
                    ),
                    (
                        "The ratio between how much power gets through in the on state versus the off state is what we call the extinction ratio, and this is the actual figure of merit for the whole modulator.",
                        None,
                    ),
                ],
            ),
            (
                "PHOTOCURRENT",
                [
                    (
                        "There's one more piece to this.",
                        None,
                    ),
                    (
                        "When a photon actually gets absorbed inside a well, it doesn't just vanish, it creates a new electron-hole pair right there.",
                        None,
                    ),
                    (
                        "And since we're already under reverse bias, that same large field is present, and it sweeps this new electron and hole out of the well in opposite directions.",
                        None,
                    ),
                    (
                        "They leave the device as current, and we call this the photocurrent.",
                        None,
                    ),
                    (
                        "Every photon that gets absorbed becomes a measurable piece of charge, so the photocurrent ends up proportional to how much light was actually absorbed.",
                        None,
                    ),
                    (
                        "This is useful, it means we can measure the absorption electrically, without ever measuring optical power directly, and this is exactly how the simulation gets checked against the real device.",
                        None,
                    ),
                    (
                        "But there's a catch too: those carriers need to leave the wells quickly, before the next bit arrives.",
                        None,
                    ),
                    (
                        "If the optical power is high and the escape is too slow, the carriers pile up inside the wells instead.",
                        None,
                    ),
                    (
                        "Once charge accumulates there, it screens the field we worked so hard to build up.",
                        None,
                    ),
                    (
                        "The field inside the wells drops, the absorption drops with it, and the modulator saturates.",
                        None,
                    ),
                    (
                        "So the photocurrent is both our measurement tool and the origin of a real limitation, and that limitation is about timing, not about absorption itself.",
                        None,
                    ),
                ],
            ),
        ],
    },
    {
        "num": "7",
        "name": "Electrical and optical side",
        "sections": [
            (
                "ELECTRICAL SIDE",
                [
                    (
                        "Now let's look at this device from the electrical side.",
                        None,
                    ),
                    (
                        "We'll come back to the optical side afterward.",
                        None,
                    ),
                    (
                        "Electrically, the reverse-biased active region behaves as a capacitor: it's a depletion region with no free carriers, sitting between two conductive doped layers, exactly the geometry of a parallel-plate capacitor.",
                        None,
                    ),
                    (
                        "We call this the EAM capacitance, C EAM.",
                        None,
                    ),
                    (
                        "We already said absorbed photons generate a photocurrent.",
                        None,
                    ),
                    (
                        "The photocurrent also depends on voltage.",
                        None,
                    ),
                    (
                        "We represent that with a resistance in parallel with the capacitance, the photocurrent resistance, R pho, since resistance is just the ratio between a voltage change and the current change it causes.",
                        None,
                    ),
                    (
                        "It's just a way to describe how the photocurrent reacts to changes in voltage.",
                        None,
                    ),
                    (
                        "Strictly speaking, R pho isn't purely an electrical quantity.",
                        None,
                    ),
                    (
                        "It comes from the same absorption coefficient, alpha of V, that we'll use on the optical side, just expressed here in units of current instead of optical power.",
                        None,
                    ),
                    (
                        "The ridge itself isn't a perfect conductor, so it has some resistance to current flowing through it, the series resistance, R ser.",
                        None,
                    ),
                    (
                        "And the device isn't measured in isolation either: it connects through a contact pad and a transmission line to an RF probe, which has its own fifty-ohm termination, a DC blocking capacitor, and parasitic capacitance and inductance.",
                        None,
                    ),
                    (
                        "From just the device part of this circuit, we get a simple, first estimate of the bandwidth: the three dB bandwidth, f 3dB, equals one over two pi times R ser times C EAM.",
                        "From just the device part of this circuit, we get a simple, first estimate of the bandwidth: the three dee bee bandwidth, f three dee bee, equals one over two pi times R ser times C EAM.",
                    ),
                    (
                        "A smaller, lower-capacitance device is faster.",
                        None,
                    ),
                    (
                        "Both of these quantities depend on the device length, L.",
                        None,
                    ),
                    (
                        "The series resistance goes as R ser equals R zero over L, so it falls as we make the device longer.",
                        None,
                    ),
                    (
                        "But the capacitance goes as C EAM equals C zero times L, since it behaves like a parallel-plate capacitor whose area grows with length, so it rises.",
                        None,
                    ),
                    (
                        "Overall, a shorter device wins on bandwidth.",
                        None,
                    ),
                ],
            ),
            (
                "OPTICAL SIDE",
                [
                    (
                        "Now let's look at the optical side.",
                        None,
                    ),
                    (
                        "We already know the absorption coefficient inside the wells, alpha of V, changes with voltage, through the quantum confined Stark effect.",
                        None,
                    ),
                    (
                        "The relationship between that absorption coefficient and how much optical power actually gets through the device is exponential: T of V equals e to the minus alpha of V, times L.",
                        None,
                    ),
                    (
                        "We call T of V the transmission coefficient.",
                        None,
                    ),
                    (
                        "From this, the extinction ratio, in decibels, equals ten times the log of T at the off voltage over T at the on voltage, and if you work through the exponentials, this reduces to a clean form: E R equals four point three four three, times the difference between alpha at the on voltage and alpha at the off voltage, times L.",
                        None,
                    ),
                    (
                        "So a longer device gives more extinction ratio, for the same change in voltage.",
                        None,
                    ),
                    (
                        "But a longer device also costs us more mean insertion loss, this is how much optical power we lose overall just by having the device in the path, averaged between the on and off states.",
                        None,
                    ),
                    (
                        "It's defined as eta mean equals minus ten log of the average of T at the on voltage and T at the off voltage.",
                        None,
                    ),
                    (
                        "Since a longer device absorbs more overall, this loss grows with length too.",
                        None,
                    ),
                    (
                        "So now we have all three numbers on the table: extinction ratio and insertion loss both grow with length, from the optical side, and bandwidth falls with length, from the electrical side we just covered.",
                        None,
                    ),
                    (
                        "All three are governed by this one design choice, and none of them can be optimized in isolation.",
                        None,
                    ),
                ],
            ),
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
