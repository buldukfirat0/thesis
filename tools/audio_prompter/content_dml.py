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
                        "When we send a 1, we push the current up, and the optical output gets brighter.",
                        None,
                    ),
                    (
                        "When we send a 0, we pull the current down, but we stay above threshold, so the laser stays on and the output just gets dimmer.",
                        None,
                    ),
                    (
                        "This way, the binary data is written directly onto the intensity of the light.",
                        None,
                    ),
                    (
                        "We call this direct modulation because we modulate the laser source itself, through its drive current, rather than using a separate device after it.",
                        None,
                    ),
                ],
            ),
        ],
    },
    {
        "num": "3",
        "name": "The two problems",
        "sections": [
            (
                "THE TWO REASONS",
                [
                    (
                        "There are two reasons for this: chirp and speed.",
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
                "SPEED",
                [
                    (
                        "The second is speed.",
                        None,
                    ),
                    (
                        "This is the upper limit on how fast we can switch bits, and it happens because the carrier density and the photon density inside the cavity are coupled to each other, so when we suddenly change the current, the optical power doesn't settle instantly, it oscillates for a while before settling.",
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
                        "So both problems come from the same root cause: we're asking one single device to do two jobs at once, generate the light and carry the data.",
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
        "name": "Quantum-Confined Stark Effect",
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
    {
        "num": "8",
        "name": "F-K-E",
        "sections": [
            (
                "FUNDAMENTALS",
                [
                    (
                        "Before going into how my device actually operates, I want to give an introduction to the fundamentals we need.",
                        None,
                    ),
                    (
                        "Electroabsorption means that when we apply a voltage to a semiconductor, the way it absorbs light changes.",
                        None,
                    ),
                    (
                        "To see where that comes from, start with bulk material.",
                        None,
                    ),
                    (
                        "Bulk means the carriers move freely in all three dimensions.",
                        None,
                    ),
                    (
                        "There is no confinement anywhere, and the energy bands are continuous.",
                        None,
                    ),
                ],
            ),
            (
                "THE ABSORPTION RULE",
                [
                    (
                        "In such a material there is one rule for absorption.",
                        None,
                    ),
                    (
                        "A photon can only be absorbed if it carries at least the band gap energy, because that is what it takes to lift an electron from the valence band to the conduction band.",
                        None,
                    ),
                    (
                        "If the photon carries less than that, the semiconductor is transparent and the light passes straight through.",
                        None,
                    ),
                    (
                        "If it carries more, the photon is absorbed.",
                        None,
                    ),
                ],
            ),
            (
                "SLIDE 1: NO FIELD",
                [
                    (
                        "On the left you see exactly this situation.",
                        None,
                    ),
                    (
                        "No voltage is applied, so both band edges are flat lines across the material.",
                        None,
                    ),
                ],
            ),
            (
                "SLIDE 1: THE SPECTRUM",
                [
                    (
                        "On the right is the absorption spectrum of the same material.",
                        None,
                    ),
                    (
                        "The horizontal axis is the photon energy, but measured from the band gap.",
                        None,
                    ),
                    (
                        "Zero is exactly at the gap.",
                        None,
                    ),
                    (
                        "To the left the photon is weaker than the gap, to the right it is stronger.",
                        None,
                    ),
                    (
                        "The vertical axis is the absorption.",
                        None,
                    ),
                    (
                        "Zero means the light passes, high means the light is absorbed.",
                        None,
                    ),
                    (
                        "The grey dashed curve is the case with no field.",
                        None,
                    ),
                    (
                        "Look at the whole left half.",
                        None,
                    ),
                    (
                        "It lies flat on zero.",
                        None,
                    ),
                    (
                        "Nothing is absorbed anywhere below the gap.",
                        None,
                    ),
                ],
            ),
            (
                "SLIDE 2: THE TILT",
                [
                    (
                        "We apply a voltage, so there is now a field inside the material.",
                        None,
                    ),
                    (
                        "The field tilts both band edges. Both of them, by the same amount, so they stay parallel.",
                        None,
                    ),
                    (
                        "Pick any single position and measure between the two edges. You get the same band gap as before.",
                        None,
                    ),
                    (
                        "The field does not close the gap.",
                        None,
                    ),
                    (
                        "That is what this line says. At every position z, the conduction band edge minus the valence band edge is still the band gap.",
                        "That is what this line says. At every position zee, the conduction band edge minus the valence band edge is still the band gap.",
                    ),
                ],
            ),
            (
                "SLIDE 2: THE STATES",
                [
                    (
                        "This dashed line is the energy the electron would land on. One fixed energy, drawn across the whole material.",
                        None,
                    ),
                    (
                        "Because the band edge is tilted, this energy crosses it at one position.",
                        None,
                    ),
                    (
                        "To the left of the crossing the energy is above the band edge, so the electron is allowed there.",
                        None,
                    ),
                    (
                        "To the right it is below, so the electron is forbidden there.",
                        None,
                    ),
                    (
                        "And this is the electron state at that energy.",
                        None,
                    ),
                    (
                        "Without the field it was a plane wave, spread evenly through the crystal.",
                        None,
                    ),
                    (
                        "The field turned it into an Airy function.",
                        None,
                    ),
                    (
                        "On the allowed side it oscillates, and on the forbidden side it does not vanish, it decays.",
                        None,
                    ),
                    (
                        "The hole state does the same thing, mirrored. It oscillates on its own allowed side and decays toward the left.",
                        None,
                    ),
                ],
            ),
            (
                "SLIDE 2: THE SPECTRUM",
                [
                    (
                        "The purple curve shows the material with the field switched on.",
                        None,
                    ),
                    (
                        "Absorption now starts below the gap. This is the tunnelling, and it is a consequence of the band tilt we just saw on the left.",
                        None,
                    ),
                    (
                        "Second, above the gap the absorption no longer rises smoothly. It weaves around the old curve.",
                        None,
                    ),
                    (
                        "These are the Franz-Keldysh oscillations, and they come from the oscillating parts of the same Airy functions.",
                        None,
                    ),
                    (
                        "And the photon we send was sitting below the gap, where the material was transparent.",
                        None,
                    ),
                    (
                        "Now there is absorption at that energy. That is the effect we are after.",
                        None,
                    ),
                ],
            ),
        ],
    },
    # ---- parts 9-14: the full talk script, slide by slide -----------------
    # Source: thesis-draft/talk/FULL_SCRIPT.md. Only the spoken lines are
    # included; the point-at stage directions stay in the md file.
    {
        "num": "9",
        "name": "Talk: opening and direct modulation",
        "sections": [
            (
                "SLIDE 1, OPENING",
                [
                    (
                        "This thesis builds an electro-optical simulation chain for one fabricated electro-absorption modulator chip.",
                        None,
                    ),
                    (
                        "And it validates that chain against my own measurements of the same chip: optical, electrical, and RF.",
                        "And it validates that chain against my own measurements of the same chip: optical, electrical, and R F.",
                    ),
                ],
            ),
            (
                "STEP 1, THE DFB AT CONSTANT CURRENT",
                [
                    (
                        "A laser needs its drive current above a threshold value before it lases at all.",
                        None,
                    ),
                    (
                        "Above that threshold, the output power grows with the current.",
                        None,
                    ),
                    (
                        "Driven at a constant current, the output is constant, continuous wave light.",
                        None,
                    ),
                    (
                        "Constant power carries no information, and that is the problem this slide solves.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 2, THE DATA",
                [
                    (
                        "The data to be sent is a stream of ones and zeros.",
                        None,
                    ),
                    (
                        "It is drawn as a two-level electrical signal, still separate from the laser at this point.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 3, DIRECT MODULATION",
                [
                    (
                        "The current now has two parts.",
                        None,
                    ),
                    (
                        "A constant bias current that stays above threshold at all times, and a small data current added on top of it.",
                        None,
                    ),
                    (
                        "A one pushes the current above the bias, a zero pulls it below, never down to zero, and never below threshold.",
                        None,
                    ),
                    (
                        "Because the power current relation is linear above threshold, the current swing becomes a power swing of the same shape.",
                        None,
                    ),
                    (
                        "The photodiode at the far end converts the received optical power back into a current, and the bit stream is recovered.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 4, CHIRP",
                [
                    (
                        "This same current also disturbs the laser's carrier density.",
                        None,
                    ),
                    (
                        "Carrier density sets the refractive index inside the cavity, and the index sets the lasing wavelength.",
                        None,
                    ),
                    (
                        "So every time a bit switches, the wavelength shifts by a small amount.",
                        None,
                    ),
                    (
                        "Instead of one clean line, the laser emits at two slightly different wavelengths depending on the bit. This is chirp.",
                        None,
                    ),
                    (
                        "Different wavelengths travel at different speeds in a fiber, so chirp spreads a pulse out over distance and limits how far the signal can go.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 5, RELAXATION OSCILLATION",
                [
                    (
                        "Carrier density and photon density are coupled, so the optical power cannot jump instantly to its new level.",
                        None,
                    ),
                    (
                        "It overshoots and rings before settling.",
                        None,
                    ),
                    (
                        "This ringing caps how fast the current can be switched.",
                        None,
                    ),
                ],
            ),
            (
                "CLOSING",
                [
                    (
                        "All three problems come from the same root cause: one device is asked to both generate the light and carry the data.",
                        None,
                    ),
                    (
                        "The fix is to split those two jobs.",
                        None,
                    ),
                    (
                        "Keep the DFB at constant current, and put a second device after it whose only job is to let light through or block it.",
                        None,
                    ),
                    (
                        "That second device is the electro-absorption modulator.",
                        None,
                    ),
                ],
            ),
        ],
    },
    {
        "num": "10",
        "name": "Talk: the EAM, layer by layer",
        "sections": [
            (
                "STEP 1, THE EML CHIP",
                [
                    (
                        "The DFB laser and the EAM share one identical epitaxial stack.",
                        None,
                    ),
                    (
                        "They are grown together on the same chip, and only differ in doping and how they are driven.",
                        None,
                    ),
                    (
                        "The laser runs on forward bias, the modulator on reverse bias.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 2, THE SUBSTRATE",
                [
                    (
                        "The n-type indium phosphide substrate is the base the whole chip is grown on, with a common backside contact that grounds the entire chip.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 3, N-SIDE CONFINEMENT",
                [
                    (
                        "The n-side confinement layers form one side of the waveguide core.",
                        None,
                    ),
                    (
                        "Their refractive index is higher than the indium phosphide around them, which is what confines the light.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 4, THE INTRINSIC REGION",
                [
                    (
                        "This is the undoped layer, the i of the p-i-n diode.",
                        "This is the undoped layer, the I of the P I N diode.",
                    ),
                    (
                        "Everything the modulator does happens inside this one thin layer.",
                        None,
                    ),
                    (
                        "Its internal structure, the quantum wells, comes two slides later.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 5, P-SIDE CONFINEMENT",
                [
                    (
                        "The mirror image of the n side, now p-doped, completing the waveguide core.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 6, THE CLADDING",
                [
                    (
                        "The p-type indium phosphide cladding closes the waveguide optically and carries the current to the contact.",
                        None,
                    ),
                    (
                        "Doping is graded: low near the light, to keep loss down, higher near the top, for low series resistance.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 7, THE CONTACT",
                [
                    (
                        "The top electrode. Together with the backside contact, these are the two terminals the reverse bias is applied across.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 8, THE RIDGE",
                [
                    (
                        "A narrow ridge is etched down through the structure, confining one single optical mode centered on the intrinsic region.",
                        None,
                    ),
                    (
                        "This is the physical device the rest of the talk analyzes.",
                        None,
                    ),
                ],
            ),
        ],
    },
    {
        "num": "11",
        "name": "Talk: the Franz-Keldysh effect",
        "sections": [
            (
                "STEP 1, NO FIELD",
                [
                    (
                        "Bulk semiconductor, no voltage on it.",
                        None,
                    ),
                    (
                        "Both band edges are flat, and the distance between them is the band gap.",
                        None,
                    ),
                    (
                        "To absorb a photon below that gap, I need an electron and a hole on the two dashed levels.",
                        None,
                    ),
                    (
                        "Inside the gap those two states are flat. Zero amplitude, at every position in the crystal.",
                        None,
                    ),
                    (
                        "So nothing can be absorbed, and the material is transparent.",
                        None,
                    ),
                    (
                        "On the right is the absorption spectrum of the same material.",
                        None,
                    ),
                    (
                        "The horizontal axis is the photon energy, measured from the band gap. Zero is exactly at the gap.",
                        None,
                    ),
                    (
                        "The grey dashed curve is the case with no field. The whole left half lies flat on zero. Nothing is absorbed below the gap.",
                        None,
                    ),
                    (
                        "The orange line only marks the photon we chose. Follow it up, and the grey curve is at zero.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 2, THE FIELD TILTS THE BANDS",
                [
                    (
                        "Now a uniform electric field.",
                        None,
                    ),
                    (
                        "The potential energy of an electron changes linearly across the crystal, so both band edges tilt, by the same amount.",
                        None,
                    ),
                    (
                        "At any one position the distance between them is still exactly the band gap.",
                        None,
                    ),
                    (
                        "The field has not closed the gap. It has only changed the geometry.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 3, THE BARRIER BECOMES FINITE",
                [
                    (
                        "Follow the upper dashed level to the right. The conduction band edge rises to meet it.",
                        None,
                    ),
                    (
                        "Left of that crossing the electron is allowed, right of it, it is not.",
                        None,
                    ),
                    (
                        "The hole has its own crossing, and it is allowed only on the other side.",
                        None,
                    ),
                    (
                        "In between, neither carrier has a state. That is a barrier.",
                        None,
                    ),
                    (
                        "Without the field it was the whole crystal. Now it is finite.",
                        None,
                    ),
                    (
                        "Its width is the missing energy divided by the slope of the bands. The stronger the field, the thinner the barrier.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 4, THE STATES REACH EACH OTHER",
                [
                    (
                        "A quantum state does not stop dead at a barrier. It decays into it.",
                        None,
                    ),
                    (
                        "The electron leaks in from one side, the hole from the other, and inside the barrier they reach each other.",
                        None,
                    ),
                    (
                        "That overlap is small, but it is not zero. And that is all an absorbed photon needs.",
                        None,
                    ),
                    (
                        "The photon supplies most of the energy, and the carriers tunnel the rest of the way. This is photon assisted tunnelling.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 5, THE SPECTRUM",
                [
                    (
                        "Below the gap there is now an absorption tail where there used to be nothing.",
                        None,
                    ),
                    (
                        "Above the gap the absorption no longer rises smoothly. It oscillates, because these are wavefunctions and they interfere.",
                        None,
                    ),
                    (
                        "If I raise the field, the bands tilt more steeply, and the tail reaches further down.",
                        None,
                    ),
                    (
                        "So at one fixed wavelength I can change the absorption with a voltage. That is electroabsorption in bulk.",
                        None,
                    ),
                ],
            ),
        ],
    },
    {
        "num": "12",
        "name": "Talk: EAM physics, wells to data",
        "sections": [
            (
                "STEP 1, MULTI QUANTUM WELL",
                [
                    (
                        "The intrinsic region is not one uniform layer.",
                        None,
                    ),
                    (
                        "It alternates between thin wells of a smaller band gap material and barriers of a larger band gap material, repeated several times.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 2, E1 AND HH1",
                [
                    (
                        "A carrier confined to a layer this thin cannot take just any energy.",
                        None,
                    ),
                    (
                        "Zoom into a single well.",
                        None,
                    ),
                    (
                        "e1 is the lowest energy the confined electron can occupy.",
                        "e one is the lowest energy the confined electron can occupy.",
                    ),
                    (
                        "hh1 is the lowest energy state of the confined heavy hole.",
                        "h h one is the lowest energy state of the confined heavy hole.",
                    ),
                    (
                        "The transition between these two levels sets the absorption edge.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 3, THE EXCITON",
                [
                    (
                        "An absorbed photon lifts an electron from hh1 to e1.",
                        "An absorbed photon lifts an electron from h h one to e one.",
                    ),
                    (
                        "The empty state left behind is a hole, Coulomb bound to the electron that just left it. This bound pair is the exciton.",
                        None,
                    ),
                    (
                        "The binding lowers the transition energy slightly, so the exciton line sits just below the plain level to level energy.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 4, READING THE SPECTRUM",
                [
                    (
                        "Each bias voltage produces one absorption curve.",
                        None,
                    ),
                    (
                        "The device is only ever read out at one fixed wavelength, the operating wavelength, thirteen ten nanometers.",
                        None,
                    ),
                    (
                        "At zero volts the absorption edge sits to the left of that line, absorption there is close to zero, and the light passes through. This is the ON state.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 5, THE RED SHIFT",
                [
                    (
                        "Apply reverse bias. The field tilts the potential inside each well.",
                        None,
                    ),
                    (
                        "e1 moves down, hh1 moves up, so the energy between them shrinks.",
                        "e one moves down, h h one moves up, so the energy between them shrinks.",
                    ),
                    (
                        "The whole absorption edge shifts to longer wavelength. A red shift.",
                        None,
                    ),
                    (
                        "The edge now sits on the operating line, absorption there is large, and the light is absorbed. This is the OFF state.",
                        None,
                    ),
                    (
                        "This combined shift and weakening of the exciton transition under field is the quantum confined Stark effect, the mechanism the whole device is built on.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 6, WHAT THE LIGHT SEES",
                [
                    (
                        "The light travels through the device as one guided optical mode.",
                        None,
                    ),
                    (
                        "Only a fraction of that mode's energy overlaps the wells. That fraction is the confinement factor, Gamma.",
                        None,
                    ),
                    (
                        "Over the device length, the transmission follows an exponential law: e to the minus Gamma alpha L.",
                        None,
                    ),
                    (
                        "The ratio of the ON and OFF transmissions is the extinction ratio, the modulator's main figure of merit.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 7, THE DRIVE",
                [
                    (
                        "In operation the device is not switched between two fixed voltages.",
                        None,
                    ),
                    (
                        "A DC bias sets the resting point in the middle of the useful range, and an RF signal swings the voltage around it.",
                        "A D C bias sets the resting point in the middle of the useful range, and an R F signal swings the voltage around it.",
                    ),
                    (
                        "One level for a one, a more negative level for a zero. The RF signal is the data.",
                        "One level for a one, a more negative level for a zero. The R F signal is the data.",
                    ),
                ],
            ),
            (
                "STEP 8, THE LIGHT COPIES THE BITS",
                [
                    (
                        "Every instantaneous voltage places the absorption edge somewhere relative to the operating wavelength.",
                        None,
                    ),
                    (
                        "Less negative, the edge sits away from the line, and light passes. More negative, the edge sits on the line, and light is absorbed.",
                        None,
                    ),
                    (
                        "The laser feeds in constant light. The output copies the voltage waveform, one to one.",
                        None,
                    ),
                    (
                        "This is how the bit stream ends up written onto the light.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 9, WHAT LIMITS THE SPEED",
                [
                    (
                        "Two things cap how fast this can be driven.",
                        None,
                    ),
                    (
                        "First, the diode is a capacitor. Every voltage change has to charge it through the circuit resistance, and that takes time.",
                        None,
                    ),
                    (
                        "Second, absorption leaves real electron hole pairs in the wells.",
                        None,
                    ),
                    (
                        "Holes escape slowly, and if they pile up, their charge screens the applied field and weakens the modulation. This is saturation.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 10, WHY THE EXCITON MECHANISM",
                [
                    (
                        "The absorption edge only has to move a few tens of nanometres, driven by about a volt.",
                        None,
                    ),
                    (
                        "And that shift itself is essentially instantaneous. It is an electronic effect.",
                        None,
                    ),
                    (
                        "The real bottleneck is the circuit and the carrier escape time, not the physics of the shift.",
                        None,
                    ),
                ],
            ),
        ],
    },
    {
        "num": "13",
        "name": "Talk: the electrical model",
        "sections": [
            (
                "STEP 1, THE EQUIVALENT CIRCUIT",
                [
                    (
                        "Under reverse bias almost no current flows through the device, so electrically the EAM behaves as a load.",
                        None,
                    ),
                    (
                        "The ridge is a series resistance, the depleted quantum well region is a capacitor, and the photocurrent appears as a parallel resistance.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 2, THE CAPACITOR",
                [
                    (
                        "The undoped region has no free carriers under bias. It behaves as an insulator between two conductive doped layers.",
                        None,
                    ),
                    (
                        "That is exactly the geometry of a parallel plate capacitor, and its capacitance grows with the device length.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 3, THE PHOTOCURRENT",
                [
                    (
                        "Every absorbed photon leaves behind a swept out electron hole pair, and that current depends on the bias point.",
                        None,
                    ),
                    (
                        "In the circuit this shows up as the parallel resistance.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 4, THE SERIES RESISTANCE",
                [
                    (
                        "Between the probe and the capacitor, the current has to cross the p-type ridge and its contact. This is the series resistance.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 5, THE RC LOW-PASS",
                [
                    (
                        "The drive signal has to charge the capacitance through the source impedance and the ridge resistance in series.",
                        None,
                    ),
                    (
                        "That RC combination sets a first estimate of the modulator's electrical bandwidth.",
                        "That R C combination sets a first estimate of the modulator's electrical bandwidth.",
                    ),
                ],
            ),
            (
                "STEP 6, THE LENGTH",
                [
                    (
                        "Both the series resistance and the capacitance are set by the same design variable, the device length.",
                        None,
                    ),
                    (
                        "Resistance falls with length, capacitance grows with it.",
                        None,
                    ),
                    (
                        "This is one half of the length trade off. The optical model gives the other half.",
                        None,
                    ),
                ],
            ),
        ],
    },
    {
        "num": "14",
        "name": "Talk: the optical model",
        "sections": [
            (
                "STEP 1, THE EXPONENTIAL LAW",
                [
                    (
                        "Light crosses the modulator as a guided mode, and every slice along the length absorbs the same fraction of what enters it.",
                        None,
                    ),
                    (
                        "That per slice statement integrates into the exponential transmission law.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 2, ONE LAW, TWO STATES",
                [
                    (
                        "The applied voltage never touches the light directly. It only moves the absorption coefficient, through the Stark effect.",
                        None,
                    ),
                    (
                        "At low bias the absorption edge sits away from the operating wavelength. At high bias it sits on it.",
                        None,
                    ),
                    (
                        "Same transmission law, two different absorption values.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 3, THE EXTINCTION RATIO",
                [
                    (
                        "The figure of merit is the ratio of the two output powers, ON over OFF.",
                        None,
                    ),
                    (
                        "The device length multiplies directly into it. A longer device gives a larger extinction ratio.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 4, THE INSERTION LOSS",
                [
                    (
                        "Even in the ON state the device absorbs some light. It is never perfectly transparent.",
                        None,
                    ),
                    (
                        "This loss also grows with length.",
                        None,
                    ),
                ],
            ),
            (
                "STEP 5, THE TRADE-OFF",
                [
                    (
                        "Extinction ratio and insertion loss both grow with device length. Electrical bandwidth falls with it.",
                        None,
                    ),
                    (
                        "One design variable, three competing figures of merit.",
                        None,
                    ),
                    (
                        "Getting that trade off right is what the simulation chain is for.",
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
