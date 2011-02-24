## Project Description

### Lets build an SEM from scratch!

The field of SEM means big bucks. The cheapest SEM just came on the market a few years ago and costs \$70,000 US. The accelerating voltage is limited to 5kV and the sample chamber is micro-miniature. On the other end of things a full sized SEM is going to run you millions of dollars. Let's laugh a lot and make our own unit with a generous sample chamber and whatever accelerating voltage that we want (20kV would be more than enough). -Jasper

Here's the recorded stream from Brandon's and Jasper's presentations (sorry for the crappy quality!):

<http://www.ustream.tv/recorded/12763200>

![](files/560px-Schema_MEB_(en).svg.png)

*X-ray detector might come after everything else ;)*

## Vacuum Information

A tungsten filament will burn out at 10^-2 Torr or higher. Therefore, it is absolutely neccesary that we get our vacuum system working to a sufficient degree that we reach the mreasurement limit of our DV-6M thermocouple gauge (10^-3 Torr).

### B-A Gauge

The gauge we have has a 3/4" glass interface. Reccomend we weld a KF25-HN (KF25 half nipple, \$15) to the chamber and use a KF25-CP75 (KF25 Flange To 3/4” Compression Port, \$68) as a glass to metal interface. See [Duniway Stockroom](http://www.duniway.com/images/pdf/pg/p-06-to-08-hard-kf-fit-quick-flange.pdf) for cheap prices.

## Parts Needed

- Vacuum Chamber(Acquired)
  - 23"x11"
  - Aluminum
- Vacuum Pump, Dual-Stage Dual-Vane Rotary, Welch 1402, 10^-4 mTorr (Acquired)
  - Belt Drive Vacuum Pump Oil
- Basic Hose for testing(Acquired)
- Fittings for feed-throughs
  - 1/2" to ~1" fittings, 1"x1" desired "playroom" for filling with epoxies etc
  - Large feedthrough flanges welded on eventually
- Vacuum hose, clear is ok, reddish is better (6 feet, 1" ID)
- Material for lenses (silicon steel? permeable iron/steel alloy? must be available in round stock)
- Electron Emitters (Acquired)
  - HT power supply (1-20kVDC, 1-5kVDC OK for now)
    - Flyback transformer with variable duty cycle (to vary output voltage) and output capacitor to smooth waveform
    - Digital interface for varying the duty cycle
- Hose Clamps(Acquired)
- Webcam + White LED to mount inside of chamber
- Vacuum Gauges (Acquired)
  - Driver/meter for the DV-6M thermocouple gauge (Jasper)
  - Driver/meter for the Bayard-Alpert hot cathode ionization gauge

## Completed

### Feb 20th

We created a vacuum with the Pump, Chamber, and Hose setup that we purchased the other day. The DV-6M thermocouple gauge is strange, but we managed to figure out how to get a useful reading out of it. It still has some weird parts that we need to figure out in order to correlate against a known vacuum level, but for now we have a relative baseline established of [198.207.0.5](Special-Contributions-198.207.0.5)1 Torr. Looks like we have a bit of leakage from the hose connections at the moment.

### Feb 21st

Upon discovery of the leak using the water pour and vacuum gauge method, and an attempt was made to reseal the threads. Unfortunately a crack was discovered which caused the main valve (Swagelok Whitey Ball Valve SS 45S8) to shear off leaving half of the adapter fitting inside of the chamber and the other half in the valve.

### Feb 22nd

Bayard-Alpert hot cathode ionization gauge came in the mail today. Looks pretty sexy. We will need two more power supplies (+200VDC, -50VDC) a pico-amp meter, and a way to attach the glass tube to a metal flange. Looks like this will probably require some TIG welding, hopefully the MCC welding shop can help us out here.

## Next Steps

- Fix the vacuum hose fitting which broke off and attempt to get a better vacuum
- Build permanent circuit and enclosure for driving the gauge heater to 20mA.
- Provide a digital readout of the thermocouple voltage as well as output the data onto a digital interface line for future incorporation.
